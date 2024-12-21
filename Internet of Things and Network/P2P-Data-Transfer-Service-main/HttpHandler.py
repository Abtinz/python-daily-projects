from utils import *
from http.server import BaseHTTPRequestHandler , HTTPServer
from urllib.parse import urlparse, parse_qs
import redis
import json


class HTTP_Requests_Handler(BaseHTTPRequestHandler):

    def do_POST(self):
            
            #this is our no sql cache that will used in authorization and ip address finding ...
            redis_cache = redis.Redis(host=REDIS_HOST , port= REDIS_PORT)

            PATH = self.path
        
            #this section will work with Client Register Stun Server Protocol ...
            if "authorization" in PATH:

                try:
                    print(f"[STUN-SERVER]: {self.client_address} Requested")
                    content_length = int(self.headers['Content-Length'])
                    body = self.rfile.read(content_length)
                    data = json.loads(body.decode())
        
                    # Check if the 'username' and 'ip' fields are not null or blank
                    if not data['username'] or not data['ip']:
                        response_data = {"message": "Username and IP address cannot be null or blank."}
                        response_code = BAD_REQUEST
                    # Check if the username or IP address is already registered
                    elif redis_cache.get(data['username']) == data['ip']:
                        response_data = {"message": "Username or IP address already registered."}
                        response_code = BAD_REQUEST
                    #lets register user
                    else:
                        redis_cache.set(data['username'], data['ip'])
                        response_data = {"message": "Authorization is approved."}
                        response_code = ACCEPTED_CODE

                    # Send the response
                    self.send_response(response_code)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(response_data).encode(ENCODE_STANDARD))

                #redis exception error
                except redis.exceptions.ConnectionError:
                    response_data = {"message": "Redis server is down or cannot be reached."}
                    self.send_response(SERVER_ERROR_CODE)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(response_data).encode(ENCODE_STANDARD))

                #timeout error
                except TimeoutError:
                    response_data = {"message": "Authorization request timed out."}
                    self.send_response(REQUEST_TIMEOUT)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(response_data).encode(ENCODE_STANDARD))

                except Exception as error:
                    #this is server error, for some reasons stun server is down
                    print(error)
                    response_data = {"message": "Authorization request failed due to an internal server error."}
                    self.send_response(SERVER_ERROR_CODE)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(response_data).encode(ENCODE_STANDARD))
                    print(f"[STUN-SERVER]: {self.client_address} Requested")
            else:
                #not found request
                print(f"[STUN-SERVER]: {self.client_address} Requested not found request!")
                self.send_response(NOT_FOUND_CODE)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'404 Not Found --> your POST options: peer/list/')
    
    def do_GET(self):
        
        #this is our no sql cache that will used in authorization and ip address finding ...
        redis_cache = redis.Redis(host=REDIS_HOST , port= REDIS_PORT)

        PATH = self.path
        
        if 'peer/list/' in PATH:
            try:
                print(f"[STUN-SERVER]: {self.client_address} requested peer list")
                peers = str(redis_cache.keys('*'))
                if len(peers) > 0:
                    # Send an OK_CODE status code and a JSON response containing the list of registered peers
                    self.send_response(ACCEPTED_CODE)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response_data = {'peers': peers}
                    self.wfile.write(json.dumps(response_data).encode(ENCODE_STANDARD))
                else:
                    # Send a NOT_FOUND status code and an error message indicating that the list is empty
                    self.send_response(NOT_FOUND_CODE)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response_data = {'message': 'The list of registered peers is empty!'}
                    self.wfile.write(json.dumps(response_data).encode(ENCODE_STANDARD))
            except redis.exceptions.RedisError as error:
                # Send a SERVER_ERROR_CODE status code and an error message indicating that the server is down or there is a mistake
                self.send_response(SERVER_ERROR_CODE)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response_data = {'error': 'The STUN server encountered an error while processing your request.'}
                self.wfile.write(json.dumps(response_data).encode(ENCODE_STANDARD))
                print(f"[STUN-SERVER]: {self.client_address} encountered an error while processing the request: {error}")
            except Exception as error:
                # Send a BAD_REQUEST status code and an error message indicating that the request is invalid
                self.send_response(BAD_REQUEST)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response_data = {'error': 'The request is invalid.'}
                self.wfile.write(json.dumps(response_data).encode(ENCODE_STANDARD))
                print(f"[STUN-SERVER]: {self.client_address} encountered an error while processing the request: {error}")

        elif "get/ip" in PATH:

            try:
                print(f"[STUN-SERVER]: {self.client_address} Requested")
                query = parse_qs(urlparse(self.path).query)
                print(query)
                username = query.get('username', [''])[0]
                if not username :
                 # sending BAD_REQUEST state code if username or address are null or blank
                    self.send_response(BAD_REQUEST)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    message = {'error': 'Username is required parameters.'}
                    self.wfile.write(json.dumps(message).encode(ENCODE_STANDARD))
                else:
                    ip = redis_cache.get(username)
                    print(ip)
                    if not ip:
                        # handle the state where username is not found in Redis
                        self.send_response(NOT_FOUND_CODE)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        message = {'error': 'Username not found in the database.'}
                        self.wfile.write(json.dumps(message).encode(ENCODE_STANDARD))
                    else:
                        # handle the state where the username and address match
                        self.send_response(ACCEPTED_CODE)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        message = {'ip': ip.decode(ENCODE_STANDARD)}
                        self.wfile.write(json.dumps(message).encode(ENCODE_STANDARD))
                   
            except redis.exceptions.ConnectionError:
                # sending SERVER_ERROR_CODE code for Redis server connection error
                self.send_response(SERVER_ERROR_CODE)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                message = {'error': 'Redis server is down or cannot establish a connection.'}
                self.wfile.write(json.dumps(message).encode(ENCODE_STANDARD))

            except Exception as error:
                print(error)
                # sending REQUEST_TIMEOUT state code for a time
                self.send_response(REQUEST_TIMEOUT)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                message = {'error': 'Request timed out.'}
                self.wfile.write(json.dumps(message).encode(ENCODE_STANDARD))

            print(f"[STUN-SERVER]: {self.client_address} Requested")

        else:
            print(f"[STUN-SERVER]: {self.client_address} Requested")
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found --> your GET options: peer/list/ or get/ip')