import sqlite3


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
                    user_id INTEGER FOREIGN KEY,
                    site TEXT,
                    username TEXT,
                    password TEXT,
                    FOREIGN KEY user_id REFERENCES users (user_id))''')
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
    if choix := input() == 1:
        usrn = input("Please create a username: ")
        pw = input("Please create your master password: ")
        cur.execute('''INSERT INTO users (users, pw)''')
    elif choix == 2:
        pass
    else:
        pass
