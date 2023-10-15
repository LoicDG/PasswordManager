import sqlite3
import sys
import PwEncryption
from pyperclip import copy as ctrlc
from PwHashing import hash_pass

from cryptography.fernet import Fernet
from sys import exit
from time import sleep

nomDB = "NameD1B"
conn = sqlite3.connect(nomDB)
cur = conn.cursor()
def launch():
    creerDatabase()
    connect()

def creerDatabase():
    conn = sqlite3.connect(nomDB)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users ( 
                    user_id INTEGER PRIMARY KEY, 
                    username TEXT, 
                    pw TEXT, 
                    EncryptKey TEXT)''')  #Créer tableau avec utilisateurs
    conn.commit()
    cur.execute('''CREATE TABLE IF NOT EXISTS endpass (
                    password_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    site TEXT,
                    username TEXT,
                    password TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (user_id))''')  #Créer tableau avec les encrypted passwords
    conn.commit()
    cur.close()
    conn.close()

def connect():
    conn = sqlite3.connect(nomDB)
    cur = conn.cursor()

# def menu():
#     print("-" * 15)
#     print("1. Create account\n"
#           "2. Sign in\n"
#           "3. Quit")
#     print("-" * 15)
#
#
# def menuPw():
#     print("-" * 15)
#     print("Choose an option:")
#     print("1. Add a new password\n"
#           "2. Get an existing password\n"
#           "3. Delete a password\n"
#           "4. Quit")
#     print("-" * 15)

def createAccount(user, pw):
    conn = sqlite3.connect(nomDB)
    cur = conn.cursor()
    cur.execute('''SELECT EXISTS(SELECT * FROM users WHERE username == ?)''', (user,))
    pw = hash_pass(pw.encode())
    key = Fernet.generate_key()
    cur.execute('''INSERT INTO users (username, pw, EncryptKey) VALUES (?, ?, ?)
                                ''', (user, pw, key)) #inserting the info into the first tableau
    conn.commit()
    cur.execute('''SELECT user_id FROM users WHERE username == ?''', (user,))
    user_id = cur.fetchone()[0]
    conn.close()
    return key, user_id
