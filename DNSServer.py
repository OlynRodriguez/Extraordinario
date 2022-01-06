import socket

dns_table = {"www.google.com":"192.165.1.1", "www.youtube.com":"192.165.2","www.gmail.com":"192.165.1.3"}
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Iniciando servidor...")
s.bind(("127.0.0.1" ,1234))

while True:
    data, address = s.recvfrom(1024)
    print(f"{address} desea recuperar datos")
    data = data.decode()
    ip = dns_table.get(data, "No encontrado").encode()
    send = s.sendto(ip, address)
