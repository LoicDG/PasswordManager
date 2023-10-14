import sqlite3
import sys
import PwEncryption

from cryptography.fernet import Fernet
from sys import exit


def creerDatabase(nomDB):
    conn = sqlite3.connect(nomDB)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY, 
                    username TEXT, 
                    pw TEXT, 
                    EncryptKey TEXT)''')
    conn.commit()
    cur.execute('''CREATE TABLE IF NOT EXISTS endpass (
                    password_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    site TEXT,
                    username TEXT,
                    password TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (user_id))''')
    conn.commit()
    cur.close()
    conn.close()


def connect(nomDB):
    conn = sqlite3.connect(nomDB)
    cur = conn.cursor()
    print("Welcome to your password manager!")
    choisirOption(conn, cur)


def menu():
    print("-" * 15)
    print('''1. Create account\n2. Sign in\n3. Quit''')
    print("-" * 15)


def menuPw():
    print("-" * 15)
    print("Choose an option:")
    print("1. Add a new password\n2. Get an existing password\n3. Quit")
    print("-" * 15)


def createUser(cur, conn):
    exists = 1
    while exists != 0:
        usrn = input("Please create a username or enter 'quit' to exit: ")
        if usrn == "quit":
            sys.exit()
        cur.execute('''SELECT EXISTS(SELECT * FROM users WHERE username == ?)''',
                    (usrn,))
        exists = cur.fetchone()[0]
        if exists == 1:
            print("This user already exists")
    pw = input("Please create your master password: ")
    key = Fernet.generate_key()
    cur.execute('''INSERT INTO users (username, pw, EncryptKey) VALUES (?, ?, ?) 
                                ''', (usrn, pw, key))
    conn.commit()
    cur.execute('''SELECT user_id FROM users WHERE username == ?''', (usrn,))
    user_id = cur.fetchone()[0]
    return key, user_id


def signIn(cur):
    exists = 0
    while exists != 1:
        usrn = input("Please enter your username or enter 'quit' to exit: ")
        if usrn == "quit":
            sys.exit()
        cur.execute('''SELECT EXISTS(SELECT * FROM users WHERE username == ?)''',
                    (usrn,))
        exists = cur.fetchone()[0]
        if exists == 0:
            print("This user does not exist")
    cur.execute('''SELECT pw, EncryptKey FROM users WHERE username == ? ''',
                (usrn,))
    pw, encryptKey = cur.fetchmany(1)[0]
    password = ""
    tries = 0
    while password != pw and tries < 3:
        password = input("Enter your password: ")
        if password != pw:
            if tries < 2:
                print("Password incorrect, please try again")
            tries = tries + 1
    if tries == 3:
        print("Too many tries, the password manager will now close")
        sys.exit()
    cur.execute('''SELECT user_id FROM users WHERE username == ?''', (usrn,))
    user_id = cur.fetchone()[0]
    return encryptKey, user_id


def choisirOption(conn, cur):
    menu()
    choix = input()
    if choix == "1":
        encryptKey, user_id = createUser(cur, conn)
        choisirQuoiFaire(user_id, encryptKey, conn, cur)
    elif choix == "2":
        encryptKey, user_id = signIn(cur)
        choisirQuoiFaire(user_id, encryptKey, conn, cur)
    elif choix == "3":
        cur.close()
        conn.close()
        exit()
    else:
        print("Please enter a valid option")
        choisirOption(conn, cur)


def choisirQuoiFaire(user_id, key, conn, cur):
    menuPw()
    choix = input()
    if choix == "1":
        site = input("For what site do you want to create a password: ")
        name = input("What is the username used for this website: ")
        pw = input("Please enter a password for this website: ")
        pw = PwEncryption.encrypt(key, pw)
        cur.execute('''INSERT INTO endpass (user_id, site, username, password) VALUES(?,?,?,?)''',
                    (user_id, site, name, pw))
        conn.commit()
        print("Your password has been saved!")
    elif choix == "2":
        pass
    elif choix == "3":
        pass
    else:
        print("Please enter a valid option")
        choisirQuoiFaire(user_id, key, conn, cur)
