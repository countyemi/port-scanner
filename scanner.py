import socket

def scan(host, port_range=6000):
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Cannot resolve {host}")
        return
    
    print(f"Scanning host {ip}...")
    
    for port in range(1, port_range + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()
        except socket.error:
            pass

host = input("Enter host to scan: ")
scan(host)

