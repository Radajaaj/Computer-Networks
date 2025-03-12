from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

# Geração de chave pública e privada
chave = RSA.generate(2048)
chave_publica = chave.publickey()
chave_privada = chave
print("Chave Pública eh: \n", chave_publica.exportKey())
print("Chave Privada eh: \n", chave_privada.exportKey())

# Função de criptografia com a chave pública
def criptografar_com_publica(mensagem, chave_publica):
    cipher = PKCS1_OAEP.new(chave_publica)
    return base64.b64encode(cipher.encrypt(mensagem.encode())).decode()

# Função de descriptografia com a chave pública
def descriptografar_com_publica(mensagem, chave_publica):
    cipher = PKCS1_OAEP.new(chave_publica)
    return cipher.decrypt(base64.b64decode(mensagem)).decode()

# Função de criptografia com a chave privada
def criptografar_com_privada(mensagem, chave_privada):
    cipher = PKCS1_OAEP.new(chave_privada)
    return base64.b64encode(cipher.encrypt(mensagem.encode())).decode()

# Função de descriptografia com a chave privada
def descriptografar_com_privada(mensagem, chave_privada):
    cipher = PKCS1_OAEP.new(chave_privada)
    return cipher.decrypt(base64.b64decode(mensagem)).decode()

# Teste 1
mensagem_original = "Mensagem secreta Criptografada com Pública"
criptografada = criptografar_com_publica(mensagem_original, chave_publica)
print(f"Criptografada:\n{criptografada}")
descriptografada = descriptografar_com_privada(criptografada, chave_privada)
print(f"Descriptografada:\n{descriptografada}")

print("\n\n----------------------------------\n\n")
# Teste 2
mensagem_original = "Mensagem secreta Criptografada com Privada"
criptografada = criptografar_com_privada(mensagem_original, chave_publica)
print(f"Criptografada:\n{criptografada}")
descriptografada = descriptografar_com_publica(criptografada, chave_privada)
print(f"Descriptografada:\n{descriptografada}")
