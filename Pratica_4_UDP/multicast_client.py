import socket
import struct

# CriaÃ§Ã£o do socket UDP
multicast_group = '224.1.1.1'  # Mesmo grupo do servidor
server_address = ('', 12345)

# ConfiguraÃ§Ã£o do socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular o socket Ã  porta do servidor
sock.bind(server_address)

# Informar que o cliente quer se juntar ao grupo multicast
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receber mensagens do grupo multicast
try:
    while True:
        print("Aguardando mensagem multicast...")
        data, address = sock.recvfrom(1024)
        print(f"Recebido: {data.decode()} de {address}")
finally:
    sock.close()