import socket

while(True):
    # CriaÃ§Ã£o do socket UDP
    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # EndereÃ§o do servidor
    server_address = ('10.81.24.86', 12345)
    
    # Mensagem a ser enviada ao servidor
    message = input()
    
    udp_client_socket.sendto(message.encode(), server_address)
    
    # Recebe resposta do servidor
    data, server = udp_client_socket.recvfrom(1024)
    print(f"Resposta do servidor: {data.decode()}")
    
    # Fechando o socket do cliente
    udp_client_socket.close()