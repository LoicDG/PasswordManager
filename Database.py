import sqlite3
from cryptography.fernet import Fernet

def creerDatabase(nomDB):
    conn = sqlite3.connect(nomDB)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY, 
                    users TEXT, 
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
    print("-" * 15)
    print('''1. Create account\n2. Sign in''')
    print("-" * 15)
    if choix := input() == "1":
        exists = 1
        while exists != 0:
            usrn = input("Please create a username: ")
            cur.execute('''SELECT EXISTS(SELECT * FROM users WHERE users == ?)''',
                        (usrn,))
            exists = cur.fetchone()[0]
            if exists == 1:
                print("This user already exists")
        pw = input("Please create your master password: ")
        key = Fernet.generate_key()
        cur.execute('''INSERT INTO users (users, pw, EncryptKey) VALUES (?, ?, ?) 
                            ''', (usrn, pw, key))
        conn.commit()
        cur.close()
        conn.close()
    elif choix == "2":
        pass
    else:
        pass
