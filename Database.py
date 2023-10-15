import sqlite3
import sys
import PwEncryption
from pyperclip import copy as ctrlc
from PwHashing import hash_pass

from cryptography.fernet import Fernet
from sys import exit
from time import sleep


def launch(nomDB):
    creerDatabase(nomDB)
    connect(nomDB)


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
    print("1. Create account\n"
          "2. Sign in\n"
          "3. Quit")
    print("-" * 15)


def menuPw():
    print("-" * 15)
    print("Choose an option:")
    print("1. Add a new password\n"
          "2. Get an existing password\n"
          "3. Delete a password\n"
          "4. Quit")
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
    pw = hash_pass(pw.encode())
    key = Fernet.generate_key()
    cur.execute('''INSERT INTO users (username, pw, EncryptKey) VALUES (?, ?, ?) 
                                ''', (usrn, pw, key))
    conn.commit()
    cur.execute('''SELECT user_id FROM users WHERE username == ?''', (usrn,))
    user_id = cur.fetchone()[0]
    return key, user_id


def signIn(cur, conn):
    exists = 0
    while exists != 1:
        usrn = input("Please enter your username or enter 'quit' to exit: ")
        if usrn == "quit":
            sys.exit()
        cur.execute('''SELECT EXISTS(SELECT * FROM users WHERE username == ?)''',
                    (usrn,))
        exists = cur.fetchone()[0]
        if exists == 0:
            changeMind = input("This user does not exist, if you want to create an new account please enter 'create'"
                               "or 'quit' to exit\n")
            if changeMind == "create":
                createUser(cur, conn)
            elif changeMind == "quit":
                sys.exit()

    cur.execute('''SELECT pw, EncryptKey FROM users WHERE username == ? ''',
                (usrn,))
    pw, encryptKey = cur.fetchmany(1)[0]
    password = ""
    tries = 0
    while password != pw and tries < 3:
        password = input("Enter your password: ")
        password = hash_pass(password.encode())
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
        encryptKey, user_id = signIn(cur, conn)
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
        site = site.lower().capitalize()
        name = input("What is the username used for this website: ")

        cur.execute('''SELECT EXISTS(SELECT * FROM endpass WHERE user_id == ? AND username == ? AND site ==?)''',
                    (user_id, name, site))
        exists = cur.fetchone()[0]
        if exists == 1:
            yesNo = input("A password exists already for this site and this username, "
                          "do you want to change it?\nY/N >>")
            while yesNo != "Y" or yesNo != "N":
                if yesNo == "Y":
                    newPw = input("Please enter your new password: ")
                    newPw = PwEncryption.encrypt(key, newPw)
                    cur.execute('''UPDATE endpass SET password == ? WHERE 
                    user_id == ? AND username == ? AND site ==?''', (newPw, user_id, name, site))
                    conn.commit()
                    print("Your password has been updated!")
                    sleep(2)
                    break
                elif yesNo == "N":
                    break
                else:
                    print("Please type Y or N to confirm your choice")
        else:
            pw = input("Please enter a password for this website: ")
            pw = PwEncryption.encrypt(key, pw)
            cur.execute('''INSERT INTO endpass (user_id, site, username, password) VALUES(?,?,?,?)''',
                        (user_id, site, name, pw))
            conn.commit()
            print("Your password has been saved!")
            sleep(2)

    elif choix == "2":
        listUsers, site = getWebsites(cur, user_id, "What site do you want to get the password to?\n")
        if listUsers is None:
            print("There are no passwords yet")
            sleep(2.5)
            choisirQuoiFaire(user_id, key, conn, cur)
        print("Website: " + site)
        print("Username: Password")
        index = 1
        nbUsers = len(listUsers)
        for entry in range(len(listUsers)):
            listUsers[entry] = list(listUsers[entry])
            listUsers[entry][1] = PwEncryption.decrypt(key, listUsers[entry][1])
            print(str(index) + ". " + listUsers[entry][0] + ": " + listUsers[entry][1])
            index = index + 1
        doCopy = input("If you want to copy a password to your clipboard enter the corresponding number, or press "
                       "enter to continue\n")
        try:
            doCopy = int(doCopy)
        except ValueError:
            pass
        else:
            if 0 < doCopy <= nbUsers:
                ctrlc(str(listUsers[doCopy - 1][1]))
                print("The password has been copied to your clipboard!")
                sleep(2.5)
            else:
                pass

    elif choix == "3":
        listUsers, site = getWebsites(cur, user_id, "From what website do you want to delete a password?\n")
        if listUsers is None:
            print("There are no passwords to delete")
            sleep(2)
            choisirQuoiFaire(user_id, key, conn, cur)
        nbUsers = len(listUsers)
        print("Website: " + site)
        index = 1
        print("Users:")
        for i in listUsers:
            print(str(index) + ". " + i[0])
        doCopy = input("Select the user you want to delete, or press enter to continue\n")
        try:
            doCopy = int(doCopy)
        except ValueError:
            pass
        else:
            if 0 < doCopy <= nbUsers:
                confirm = input("Are you sure? Y/N\n")
                if confirm == "Y":
                    username = listUsers[doCopy-1][0]
                    cur.execute('''DELETE FROM endpass WHERE user_id == ? AND site == ? AND username == ?''',
                                (user_id, site, username))
                    conn.commit()
                    print("Your password has been successfully deleted!")
                    sleep(2.5)
                elif confirm == "N":
                    pass
    elif choix == "4":
        sys.exit()
    else:
        print("Please enter a valid option")
        sleep(2)
    choisirQuoiFaire(user_id, key, conn, cur)


def getWebsites(cur, user_id, request):
    cur.execute('''SELECT site FROM endpass WHERE user_id == ?''', (user_id,))
    listSites = cur.fetchall()
    nbSites = len(listSites)
    if nbSites == 1:
        site = listSites[0][0]
    elif nbSites == 0:
        return None, None
    else:
        sites = "Websites:\n"
        index = 1
        for i in range(len(listSites)):
            sites += str(index) + ". " + listSites[i][0] + "\n"
            index = index + 1
        number = False
        while not number:
            print(sites)
            site = input(request)
            try:
                site = int(site)
            except ValueError:
                print("Please enter a number between 1 and " + str(nbSites))
                sleep(2)
            else:
                if 0 < site <= nbSites:
                    site = listSites[site - 1][0]
                    number = True
                else:
                    print("Please enter a number between 1 and " + str(nbSites))
                    sleep(2)
    cur.execute("SELECT username, password FROM endpass WHERE site == ? AND user_id == ?", (site, user_id))
    return cur.fetchall(), site
