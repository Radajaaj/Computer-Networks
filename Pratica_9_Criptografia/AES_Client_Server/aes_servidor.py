import socket
from Crypto.Cipher import AES
import base64

# Chave secreta compartilhada (deve ter 16, 24 ou 32 bytes)
chave_simetrica = b"chave_secreta123"  # 16 bytes

def descriptografar(mensagem_cifrada):
    dados = base64.b64decode(mensagem_cifrada)
    nonce, tag, ciphertext = dados[:16], dados[16:32], dados[32:]

    cipher = AES.new(chave_simetrica, AES.MODE_EAX, nonce=nonce)
    try:
        mensagem = cipher.decrypt_and_verify(ciphertext, tag)
        return mensagem.decode()
    except ValueError:
        return "Erro: Mensagem adulterada!"

# Configuração do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))  # Escuta na porta 12345
server.listen(1)

print("Aguardando conexão...")
conn, addr = server.accept()
print(f"Conectado a {addr}")

while True:
    dados = conn.recv(1024)
    if not dados:
        break
    mensagem_decifrada = descriptografar(dados.decode())
    print(f"Mensagem recebida: {mensagem_decifrada}")

conn.close()
server.close()

