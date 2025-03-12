import socket
import struct
import time

# CriaÃ§Ã£o do socket UDP
multicast_group = '244.1.1.1'  # EndereÃ§o de multicast (224.0.0.0 a 239.255.255.255)
server_address = ('', 12345)

# ConfiguraÃ§Ã£o do socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Definindo TTL (Time to Live) para o pacote multicast
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Enviando mensagens ao grupo multicast
try:
    while True:
        message = "amogus"
        print(f"Enviando: {message}")
        sent = sock.sendto(message.encode(), (multicast_group, 12345))
        time.sleep(0)  # Enviar a cada 2 segundos
finally:
    sock.close()