import hashlib
def hash_pass(pw):
    hash_pw = hashlib.sha256(pw).hexdigest()
    return hash_pw


