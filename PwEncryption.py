from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)

def encrypt(pw):
    return fernet.encrypt(pw.encode())

def decrypt(encoded_msg):
    return fernet.decrypt(encoded_msg).decode()

def get_key():
    return key