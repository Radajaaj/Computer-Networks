import socket

# CriaÃ§Ã£o do socket UDP
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# LigaÃ§Ã£o do socket ao endereÃ§o e porta
server_address = ('10.81.166.112', 12345)
udp_server_socket.bind(server_address)

print("Servidor UDP aguardando mensagens...")

# Recebe dados do cliente
while True:
    data, address = udp_server_socket.recvfrom(1024)  # Buffer de 1024 bytes
    #print(address)
    if(address[0] != '0'):
        print(f"Mensagem recebida: {data.decode()} de {address}")
    
    # Enviar uma resposta opcional para o cliente
    response = "Mensagem recebida com sucesso"
    udp_server_socket.sendto(response.encode(), address)
    #print(f"Resposta enviada para {address}")