import socket

ip_address = '192.168.1.5'

def port_scanner(start_port, end_port, protocol,file_root):
    ''' this function will scan ports of 192.168.1.5 ip and save them in scanning given protocol files
    params:
        start_ip -> this int number will show starting range of scanning process 
        end_ip -> this int number will show ending range of scanning process 
        protocol -> scanning port on udp or tcp protocols?
        file_root -> saving root of scanning results
    '''
    open_ports = []
    closed_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, protocol)
            sock.settimeout(1)
            is_open = sock.connect_ex((ip_address, port)) != 0
            if is_open:
                closed_ports.append(port)
                print(f"closed Port:{port}")
            else:
                open_ports.append(port)
                print(f"open Port:{port}")

            sock.close()
        except socket.error as error:
           print(error)
    
     
    with open(file_root, 'a') as file:
        file.write("OPEN PORTS:\n")
        for ip in open_ports:
            file.write(str(ip)+"\n")

        file.write("CLOSED PORTS:\n")
        for ip in closed_ports:
            file.write(str(ip)+"\n")
    
    print("IP Scanning process is finished") 