from utils import *
from http.server import HTTPServer
from HttpHandler import HTTP_Requests_Handler

#here we are starting our http server and passing HTTP_Requests_Handler
def stun_server_main_handler():
    
    try:
        http_stun_server = HTTPServer(('',REQUEST_HANDLER_POST), HTTP_Requests_Handler)
        http_stun_server.serve_forever()

    except:
        choice = input("sorry, something went wrong! would you try to run the server again?\n1. Yse\netc. EXIT")
        if choice == "1": stun_server_main_handler()

stun_server_main_handler() 