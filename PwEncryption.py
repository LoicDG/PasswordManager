from cryptography.fernet import Fernet

class PwEncryption:
    def __init__(self, pw):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.pw = pw

    def encrypt(self):
        return self.fernet.encrypt(self.pw.encode())

    def decrypt(self, encoded_msg):
        return self.fernet.decrypt(encoded_msg).decode()

    def get_key(self):
        return self.key