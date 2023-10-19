import hashlib
def hash_pass(pw, salt):
    #Code to check if user is the same, then execute de following code:
    pw = pw + salt
    hash_pw = hashlib.sha256(pw).hexdigest()
    return hash_pw


