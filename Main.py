from PwHashing import PwHashing
from PwEncryption import PwEncryption

user = input("User: ")
pw = input("Pass: ")
pw_hasher = PwHashing(user, pw)

pw_hasher.hash_pass()

print("This is the hashed pw: ", pw_hasher.hash_pass())


# Sonia tests
pw_encrypter = PwEncryption(pw)
encrypted_msg = (pw_encrypter.encrypt())
decrypted_msg = (pw_encrypter.decrypt(encrypted_msg))
print("Encrypted: ", encrypted_msg)
print("Decrypted: ", decrypted_msg)

