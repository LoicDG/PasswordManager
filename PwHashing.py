import hashlib
def hash_pass(user, pw):
    #Code to check if user is the same, then execute de following code:
    hash_pw = hashlib.sha256(pw).hexdigest()
    return hash_pw


