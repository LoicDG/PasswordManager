from cryptography.fernet import Fernet
def encrypt(key, pw):
    return Fernet(key).encrypt(pw.encode())

def decrypt(key, encoded_msg):
    return Fernet(key).decrypt(encoded_msg).decode()
