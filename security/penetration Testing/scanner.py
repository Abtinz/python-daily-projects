import argparse
from ip_scanner import *
from port_scanner import *

def scanner_engine():
      ''' 
            this function will implement our scanner engine and will get our user given arguments for scanning process
    
      '''
      parser = argparse.ArgumentParser(description='IP Scanner TurboV.2000')
      parser.add_argument("--ipscan", action="store_true", help="Ip scanning", required=False)
      parser.add_argument("-ip", required=False, help="starting and ending range of ip", nargs=2)
      parser.add_argument("-portscan", action="store_true", help="Port scanning", required=False)
      parser.add_argument("-m", type=int, help="Subnet mask", required=False)
      parser.add_argument("-tcp", required=False, nargs=2, type=int)
      parser.add_argument("-udp", required=False, nargs=2, type=int)
      args = parser.parse_args()
      if args.ipscan:
            if args.m is not None:
                  scanner(
                        start_ip =args.ip[0], 
                        end_ip = args.ip[1],
                        address_counts = 2 ** (32 - args.m)
                  )
            else:
                simple_scanner(
                      start= args.ip[0],
                      end = args.ip[1]
                  )  
                
      if args.portscan:
            if args.tcp:
                  port_scanner(
                        start_port= args.tcp[0], 
                        end_port= args.tcp[1], 
                        protocol= socket.SOCK_STREAM,
                        file_root= "TCP_ports_result.txt"
                  )
            elif args.udp:
                  port_scanner(
                        start_port= args.udp[0], 
                        end_port= args.udp[1], 
                        protocol= socket.SOCK_DGRAM,
                        file_root= "UDP_ports_result.txt"
                  )
            
            else:
                  print("INVALID PROTOCOL ...")
   
scanner_engine()
