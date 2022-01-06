import socket
hostname = socket.gethostname()
ipaddr = "127.0.0.1"
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = (ipaddr, 1234)
c = "Y"
while c.upper()=="Y":
    req_domain = input ("Ingresa el nombre del dominio: ")
    send = s.sendto(req_domain.encode(), addr)
    data, address = s.recvfrom(1024)
    reply_ip = data.decode().strip()
    print(f"La ip del dominio es: {req_domain}:{reply_ip}")
    c = (input("Continuar (y/n)"))
    s.close()
