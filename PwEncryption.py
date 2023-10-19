from cryptography.fernet import Fernet
from passlib.hash import argon2
import base64


def encrypt(key, pw):
    key = base64.urlsafe_b64encode(key)
    return Fernet(key).encrypt(pw.encode())


def decrypt(key, encoded_msg):
    key = base64.urlsafe_b64encode(key)
    return Fernet(key).decrypt(encoded_msg).decode()


def generateKey(pw, salt):
    pw = pw + salt
    key = argon2.using(rounds=16).hash(pw)
    key = base64.urlsafe_b64encode(key.encode())
    key = key[:32]
    return key
