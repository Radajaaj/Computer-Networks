import socket
import struct

def checksum(msg):
    s = 0
    # Somar as palavras de 16 bits
    for i in range(0, len(msg), 2):
        w = (msg[i] << 8) + (msg[i+1])
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = s + (s >> 16)
    return ~s & 0xffff

# EndereÃ§o IP e porta do destino
dest_ip = '10.81.21.86'    # Altere para o IP de destino
source_ip = '10.81.166.112'  # IP de origem

# Criar socket UDP usando IPPROTO_UDP (apenas cabeÃ§alho UDP)
raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

# ConstruÃ§Ã£o do cabeÃ§alho UDP
source_port = 1234  # Porta de origem
dest_port = 12345   # Porta de destino
data = b"Amogus"     # Dados a serem enviados
udp_len = 8 + len(data)  # Comprimento do cabeÃ§alho UDP + dados
udp_check = 0  # Inicialmente, checksum Ã© 0

# CabeÃ§alho UDP sem checksum
udp_header = struct.pack('!HHHH', source_port, dest_port, udp_len, udp_check)

# Pseudo-cabeÃ§alho para calcular o checksum UDP
pseudo_header = struct.pack('!4s4sBBH', socket.inet_aton(source_ip), socket.inet_aton(dest_ip), 0, socket.IPPROTO_UDP, udp_len)
pseudo_packet = pseudo_header + udp_header + data

# Calculando o checksum UDP
udp_check = checksum(pseudo_packet)

# Atualizando o cabeÃ§alho UDP com o checksum correto
udp_header = struct.pack('!HHHH', source_port, dest_port, udp_len, udp_check)

# Pacote final: cabeÃ§alho UDP + dados
packet = udp_header + data

# Enviando o pacote
raw_socket.sendto(packet, (dest_ip, dest_port))
print(f"Pacote UDP enviado para {dest_ip}")

# Fechando o socket do cliente
raw_socket.close()