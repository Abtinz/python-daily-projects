import ipaddress
import socket
import struct



def scanner(start_ip, end_ip, address_counts):
    
    '''
        this function will get starting and ending range of scanning ip for 
        checking if they are alive or not and will save them is their result files...
        params:
           start_ip -> this ip will show starting range of scanning process 
           end_ip -> this ip will show ending range of scanning process ,
           address_counts -> this parameter value will show range of addresses in special network addresses using subnetmask
    '''

    print("IP Scanning process is started")   

    #we will need this classes for saving ip scanning results
    active_devices = []
    not_active_devices = []

    network_address = struct.unpack("!I", socket.inet_aton(start_ip))[0] & struct.unpack("!I", socket.inet_aton(end_ip))[0]

    with open('scanner_result.txt', 'a') as file:
        for i in range(address_counts):

            current_ip = socket.inet_ntoa(struct.pack("!I", network_address + i))

            try:

                socket.setdefaulttimeout(1)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((current_ip, 80))

                active_devices.append(current_ip)
                print(f"active IP:{str(current_ip)} ...")
                file.write(f"active IP:{str(current_ip)} ...\n")

            except Exception as error:
           
                not_active_devices.append(current_ip)
                file.write(f"not active IP:{str(current_ip)} ...\n")
                print(f"not active IP:{str(current_ip)} ...")
    

    with open('active_list.txt', 'a') as file:
        for ip in active_devices:
            file.write(str(ip)+"\n")

     
    with open('not_active_list.txt', 'a') as file:
        for ip in not_active_devices:
            file.write(str(ip)+"\n")
    
    print("IP Scanning process is finished")   



def simple_scanner(start, end):
    '''
        this function will get starting and ending range of scanning ip for without subnet mask
        checking if they are alive or not and will save them is their result files...
        params:
           start_ip -> this ip will show starting range of scanning process 
           end_ip -> this ip will show ending range of scanning process 
    '''

    print("IP Scanning process is started")   

    #finding the starting and ending ip addresses
    start, end = int(ipaddress.IPv4Address(start)), int(ipaddress.IPv4Address(end))
    ip_range = [str(ipaddress.IPv4Address(ip)) for ip in range(start, end + 1)]

    #we will need this classes for saving ip scanning results
    active_devices = []
    not_active_devices = []
    with open('scanner_result.txt', 'a') as file:
    
        for current_ip in ip_range:
            
            #checking that if ip is alive or not
            try:

                socket.setdefaulttimeout(1)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((current_ip, 80))

                active_devices.append(current_ip)
                print(f"active IP:{str(current_ip)} ...")
                file.write(f"active IP:{str(current_ip)} ...\n")

            except Exception as error:
           
                not_active_devices.append(current_ip)
                file.write(f"not active IP:{str(current_ip)} ...\n")
                print(f"not active IP:{str(current_ip)} ...")

    
    with open('active_list.txt', 'a') as file:
        for ip in active_devices:
            file.write(str(ip)+"\n")

     
    with open('not_active_list.txt', 'a') as file:
        for ip in not_active_devices:
            file.write(str(ip)+"\n")
    
    print("IP Scanning process is finished")   
