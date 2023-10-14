from PwHashing import PwHashing


user = input("User: ")
pw = input("Pass: ")
pw_hasher = PwHashing(user, pw)

pw_hasher.hash_pass()

print("This is the hashed pw: ", pw_hasher.hash_pass())

