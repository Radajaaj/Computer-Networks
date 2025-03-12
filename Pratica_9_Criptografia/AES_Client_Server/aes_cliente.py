import socket
from Crypto.Cipher import AES
import base64

# Chave secreta compartilhada (deve ser igual à do servidor)
chave_simetrica = b"chave_secreta123"  # 16 bytes

def criptografar(mensagem):
    cipher = AES.new(chave_simetrica, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(mensagem.encode())

    return base64.b64encode(nonce + tag + ciphertext).decode()

# Configuração do cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))  # Conecta ao servidor

mensagem_original = "Olá, servidor! Aqui é o cliente!"
mensagem_cifrada = criptografar(mensagem_original)

client.send(mensagem_cifrada.encode())  # Envia a mensagem criptografada
client.close()

