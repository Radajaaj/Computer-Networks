from Crypto.Cipher import Salsa20

#Encriptando
print("Insira a mensagem a ser codificada")
plaintext = input()
plaintext = plaintext.encode()

print("Insira a chave (Deve conter 32 caracteres)")
secret = input()
secret = secret.encode()
#secret = b'*Thirty-two byte (256 bits) key*'
cipher = Salsa20.new(key=secret)
msg = cipher.nonce + cipher.encrypt(plaintext)

print("Encriptado: ", msg)

#Desencriptando
secret = secret
msg_nonce = msg[:8]
ciphertext = msg[8:]
cipher = Salsa20.new(key=secret, nonce=msg_nonce)
plaintext = cipher.decrypt(ciphertext)
print("Decriptado: ", plaintext.decode())