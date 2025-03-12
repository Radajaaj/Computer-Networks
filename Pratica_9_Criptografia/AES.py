from Crypto.Cipher import AES

# Criptografia
print("Insira uma mensagem a ser criptografada (Apenas caracteres ASCII)")
data = input()
data = data.encode()

print("Insira uma chave (Deve conter 16 caracteres ASCII)")
key = input()
key = key.encode()

cipher = AES.new(key, AES.MODE_EAX)

nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)

print("Mensagem criptografada: ", ciphertext)
print("Tag?: ", tag)

# Decriptografia
print("\n--------------------------\nHora de decriptografar!")
print("Insira a chave de decriptografia (Deve conter 16 caracteres ASCII)")
key = input()
key = key.encode()

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
try:
    cipher.verify(tag)
    print("The message is authentic:", plaintext)
except ValueError:
    print("Key incorrect or message corrupted")