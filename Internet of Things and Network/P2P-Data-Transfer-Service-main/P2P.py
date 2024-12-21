import random
import requests #we will use it for HTTP requests
from PIL import Image #we will use PIL image for Loading Image Files
import socket
import threading
from utils import *
def get_file_from_peer(receiver_ip, sender_ip, file_route, reciever_port):
    
    try:
        # Open a TCP connection to the sender's IP address on port 10000
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.connect((sender_ip, TCP_HANDSHAKE_PORT))
        # Send a message that includes the receiver's IP address, the port number of an available UDP socket, and the file route to the sender
        message = f"{receiver_ip}:{reciever_port}:{file_route}"
        tcp_socket.sendall(message.encode())
        # Find an available port number to bind the UDP socket
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind((receiver_ip, reciever_port))
        udp_socket.settimeout(2)

        #DIMENTION OF IMAGE
        dimention , __= udp_socket.recvfrom(BUFFER_SIZE)
        width, height = dimention.decode(ENCODE_STANDARD).split(":")
        width, height = int(width), int(height)

        #GETTING CHUNKS
        chunks = []
        while True:
            try:
                # Receive data chunks from the sender using the UDP socket until an empty byte string is received
                chunk, _ = udp_socket.recvfrom(BUFFER_SIZE)
                if not chunk:  break # no chunck any more ...

                chunks.append(chunk)
                # Send an acknowledgment to the sender after receiving each chunk
                udp_socket.sendto(chunk , (sender_ip, TCP_HANDSHAKE_PORT))
            except Exception as error:
                continue
        tcp_socket.close()
        udp_socket.close()
        # Join the received data chunks into a single byte string
        data = b''.join(chunks)
        print(chunks)
        # Write the received data to a file
        try: 
            Image.frombytes("RGB", (width, height), data).save(f"{reciever_port}:{file_route}")

        except Exception as error:
                print(error)
                return
        
    except TimeoutError:  
        print("\nmessage: Error! request timed out. please try again later...")

    except Exception as error:  
        print(f"\nmessage: something went wrong!please try again later...\nerror code:{error}")
                    

def send_file_to_peer(destination_peer, destination_peer_port , file_route):
        
    image = Image.open(file_route)
    data = image.tobytes()
    width, height =str(image.size[0]) , str(image.size[1])
    dimention =  width+ ":" + height 
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(0, len(data), BUFFER_SIZE):
        chunk = data[i:i + BUFFER_SIZE]
        udp_socket.sendto(chunk, (destination_peer , int(destination_peer_port)))
        # wait for an acknowledgment from the receiver
        isAcked = False
        while not isAcked:
            try:
                acknowledgment, _ = udp_socket.recvfrom(BUFFER_SIZE)

                if acknowledgment == chunk:
                    isAcked = True
            except:
                # if there is no acknowledgment,we hve to resend the packet
                udp_socket.sendto(chunk, (destination_peer , int(destination_peer_port)))
        
    udp_socket.sendto(b'', (destination_peer, int(destination_peer_port)))
    udp_socket.close()
    

def live_peer(peer_address,peer_port):
    while True:
        listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address_and_tcp_port = (peer_address, TCP_HANDSHAKE_PORT)
        listener_socket.bind(address_and_tcp_port)
        listener_socket.listen()
        client_sock, client_address = listener_socket.accept()
        data = client_sock.recv(BUFFER_SIZE).decode(ENCODE_STANDARD)
        print(data)
        data = data.split(':')
        dest_ip = data[0]
        dest_port = data[1]
        dest_filename = data[2]
        print(f"new request from peer(ip ={dest_ip}:{dest_port}) fot {dest_filename}")
        threading.Thread(target=send_file_to_peer, args=(dest_ip, dest_port, dest_filename)).start()
        requestAccess = input(f'peer(ip ={dest_ip}:{dest_port}) wants {dest_filename},do you have it and do you like to share it? 1.YES\n etc.NO')
        if(requestAccess == "1"):
            listener_socket.sendall(f"this message is for peer(ip ={dest_ip}:{dest_port}), your request is accepted by:{peer_address}:{peer_port}".encode())
            threading.Thread(target=send_file_to_peer, args=(dest_ip, dest_port, dest_filename)).start()
        else:
            listener_socket.sendall(f"this message is for peer(ip ={dest_ip}:{dest_port}), your request is denied by:{peer_address}:{peer_port}".encode())

        listener_socket.close()

# main handler 
# this function will show main menu and execute threads and post and get http requests for peer ...
def p2p_main_handler():

   peer_address = socket.gethostbyname(socket.gethostname())
   peer_port = random.randint(10000,10100)
   print(f"your host id and Port")
   thread = threading.Thread(target=live_peer, args=(peer_address, peer_port))
   thread.start()
   while True:
        
        choice = input('P2P File Distribution Application:\n1.authorization \n2.all usernames list\n3.ip from username\n4.connection request\ninput:')
        #sending post request to AUTHORIZATION_URL for STUN-server and getting response for demonstration
        if choice == '1':

            username = input("[STUN-Server]Please write your username:")
            response = ""
            try:
                
                response = requests.post(
                   url= AUTHORIZATION_URL, 
                    json= {
                            "username": username,
                            "ip": peer_address
                        }

                ).text

                print('[STUN-Server] Response:', response)

            except:
                print('[STUN-Server] ERROR!, Response:', response)
                

        #sending a GET request to achieving all usernames from STUN-server.
        elif choice == '2':
            response = ""
            try:
                
                response = requests.get( url = GET_USERNAMES_URL).text
                print('STUN-Server] username lists:', response)

            except:
                print('[STUN-Server] ERROR!, Response:', response)

        #sending a GET request to get a specific peer ip from STUN-server.
        elif choice == '3':
            peer_username = input('[STUN-Server]:Please Enter Your Peer username:')
            response = ""
            try:
                response = requests.get( url = GET_USER_IP + peer_username ).text
                print('[STUN-Server] Response:', response)

            except:
                print('[STUN-Server] ERROR!, Response:', response)
            
            
        elif choice == '4':
            sender_ip = input('Please Enter Your Peer Ip:')
            file_route = input('Please Enter file route:')
            threading.Thread(target= get_file_from_peer, args=(peer_address,sender_ip, file_route,peer_port)).start()

p2p_main_handler()