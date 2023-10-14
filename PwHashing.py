import hashlib


class PwHashing:
    def __init__(self, user, pw):
        self.user = user
        self.pw = pw

    def hash_pass(self):
        hash_pw = hashlib.sha256()
        hash_pw_hex = hash_pw.hexdigest()
        return hash_pw_hex


