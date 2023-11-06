import sqlite3

from PwHashing import hash_pass
from os import urandom
import base64

nomDB = "DatabaseBB"

def launch():
    creerDatabase()

def creerDatabase():
    connection = sqlite3.connect(nomDB)
    curseur = connection.cursor()
    # Créer le tableau "user"
    curseur.execute('''CREATE TABLE IF NOT EXISTS users (
                    userID INTEGER PRIMARY KEY, 
                    username TEXT, 
                    masterPassword TEXT, 
                    salt TEXT)''')
    connection.commit()
    # Créer le tableau "endpass"
    curseur.execute('''CREATE TABLE IF NOT EXISTS endpass (
                    passwordID INTEGER PRIMARY KEY,
                    userID INTEGER,
                    site TEXT,
                    username TEXT,
                    password TEXT,
                    FOREIGN KEY (userID) REFERENCES users (userID))''')
    connection.commit()
    curseur.close()


def addNewUserToTable(nouveauUsername, nouveauMasterPassword, confirmPW):
    connection = sqlite3.connect(nomDB)
    curseur = connection.cursor()
    if confirmPW != nouveauMasterPassword and nouveauMasterPassword.strip() and confirmPW.strip():
        return "The passwords do not match"
    elif not nouveauMasterPassword.strip():
        return "Please enter a password"
    elif not confirmPW.strip():
        return "Please confirm your password"
    salt = base64.urlsafe_b64encode(urandom(16)).decode()
    hashedMasterPassword = hash_pass(nouveauMasterPassword.encode(), salt.encode())

    query = "INSERT INTO users (username, masterPassword, salt) VALUES (?, ?, ?)"
    curseur.execute(query, (nouveauUsername, hashedMasterPassword, salt))
    connection.commit()
    print("execution worked!") #TODO: Test

    curseur.close()

def createUser(nouveauUsername, nouveauMasterPassword, confirmPW):
    connection = sqlite3.connect(nomDB)
    curseur = connection.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    curseur.execute(query, (nouveauUsername,))

    # fetchone() retourne une rangée si le username exist, sinon elle va retournée "None"
    resultat = curseur.fetchone()
    if resultat is None:
        error = addNewUserToTable(nouveauUsername, nouveauMasterPassword, confirmPW)
        if error is not None: return error
    else:
        return "That username is already taken!"
    curseur.close()

def checkPasswordMatch(salt, storedPassword, givenPassword):
    hashedPassword = hash_pass(givenPassword.encode(), salt.encode())
    if (hashedPassword != storedPassword):
        return False


#TODO: Chui rendu icite :OP
def logIn(givenUsername, givenPassword):
    connection = sqlite3.connect(nomDB)
    curseur = connection.cursor()

    #Finding the info base on the username
    query = "SELECT masterPassword, salt FROM users WHERE username == ?"
    curseur.execute(query,(givenUsername,))

    #If the username given doesn't exist:
    resultat = curseur.fetchone()
    if resultat is None:
        return "This user doesn't exist!"

    #All of the following code executes if the user does exist
    hashedMasterPassword, salt = curseur.fetchmany(1)[0]

    #Seeing if the password matches
    count = 0
    while ((checkPasswordMatch(salt, hashedMasterPassword, givenPassword) == False) & (count < 3)):
        count+=1



    # fetchone() retourne une rangée si le username exist, sinon elle va retournée "None"


    curseur.close()

# def signIn(givenUsername, givenMasterPassword):
#     curseur = connection.cursor()
#
#     query = "SELECT password, salt FROM users WHERE username == ?"
#     curseur.execute(query, (givenUsername,))
#
#     passwordDB = ""
#     saltDB = ""
#
#     resultat = curseur.fetchone()
#     if resultat is None:
#         pass
#     else:
#         passwordDB, salt = curseur.fetchmany(1)[0]
#
#     cur.execute('''SELECT pw, salt FROM users WHERE username == ? ''',
#                 (usrn,))
#     pw, salt = cur.fetchmany(1)[0]
#
#
#
#     cur.execute('''SELECT user_id FROM users WHERE username == ?''', (usrn,))
#     user_id = cur.fetchone()[0]
#     encryptKey = PwEncryption.generateKey(pw, salt)
#     return encryptKey, user_id
#
#
# def mainMenu():
#     cur = connection.cursor()
#     afficherOptionMainMenu()
#     choix = input()
#     if choix == "1":
#         encryptKey, user_id = createUser(cur, connection)
#         menuPassword(user_id, encryptKey, connection, cur)
#     elif choix == "2":
#         encryptKey, user_id = signIn(cur, connection)
#         menuPassword(user_id, encryptKey, connection, cur)
#     elif choix == "3":
#         cur.close()
#         connection.close()
#         exit()
#     else:
#         print("Please enter a valid option")
#         sleep(2)
#         system("cls")
#         mainMenu(connection, cur)
#
#
# def menuPassword(user_id, key, conn, cur):
#     system("cls")
#     afficherOptionsPassword()
#     choix = input()
#     if choix == "1":
#         system("cls")
#         site = input("For what site do you want to create a password: ")
#         site = site.lower().capitalize()
#         name = input("What is the username used for this website: ")
#
#         cur.execute('''SELECT EXISTS(SELECT * FROM endpass WHERE user_id == ? AND username == ? AND site ==?)''',
#                     (user_id, name, site))
#         exists = cur.fetchone()[0]
#         if exists == 1:
#             yesNo = input("A password exists already for this site and this username, "
#                           "do you want to change it?\nY/N >>")
#             while yesNo != "Y" or yesNo != "N":
#                 if yesNo == "Y":
#                     newPw = enterPw("Please enter your new password: ")
#                     newPw = PwEncryption.encrypt(key, newPw)
#                     cur.execute('''UPDATE endpass SET password == ? WHERE
#                     user_id == ? AND username == ? AND site ==?''', (newPw, user_id, name, site))
#                     conn.commit()
#                     print("Your password has been updated!")
#                     sleep(2)
#                     break
#                 elif yesNo == "N":
#                     break
#                 else:
#                     print("Please type Y or N to confirm your choice")
#         else:
#             pw = enterPw("Please enter a password for this website: ")
#             pw = PwEncryption.encrypt(key, pw)
#             cur.execute('''INSERT INTO endpass (user_id, site, username, password) VALUES(?,?,?,?)''',
#                         (user_id, site, name, pw))
#             conn.commit()
#             print("Your password has been saved!")
#             sleep(2)
#
#     elif choix == "2":
#         system("cls")
#         listUsers, site = getWebsites(cur, user_id, "What site do you want to get the password to?\n")
#         if listUsers is None:
#             print("There are no passwords yet")
#             sleep(2.5)
#             menuPassword(user_id, key, conn, cur)
#         print("Website: " + site)
#         print("Username: Password")
#         index = 1
#         nbUsers = len(listUsers)
#         for entry in range(len(listUsers)):
#             listUsers[entry] = list(listUsers[entry])
#             listUsers[entry][1] = PwEncryption.decrypt(key, listUsers[entry][1])
#             print(str(index) + ". " + listUsers[entry][0] + ": " + listUsers[entry][1])
#             index = index + 1
#         doCopy = input("If you want to copy a password to your clipboard enter the corresponding number, or press "
#                        "enter to continue\n")
#         try:
#             doCopy = int(doCopy)
#         except ValueError:
#             pass
#         else:
#             if 0 < doCopy <= nbUsers:
#                 ctrlc(str(listUsers[doCopy - 1][1]))
#                 print("The password has been copied to your clipboard!")
#                 sleep(2.5)
#             else:
#                 pass
#
#     elif choix == "3":
#         system("cls")
#         listUsers, site = getWebsites(cur, user_id, "From what website do you want to delete a password?\n")
#         if listUsers is None:
#             print("There are no passwords to delete")
#             sleep(2)
#             menuPassword(user_id, key, conn, cur)
#         nbUsers = len(listUsers)
#         print("Website: " + site)
#         index = 1
#         print("Users:")
#         for i in listUsers:
#             print(str(index) + ". " + i[0])
#             index = index + 1
#         doCopy = input("Select the user you want to delete, or press enter to continue\n")
#         try:
#             doCopy = int(doCopy)
#         except ValueError:
#             pass
#         else:
#             if 0 < doCopy <= nbUsers:
#                 confirm = input("Are you sure? Y/N\n")
#                 while True:
#                     if confirm == "Y":
#                         username = listUsers[doCopy - 1][0]
#                         cur.execute('''DELETE FROM endpass WHERE user_id == ? AND site == ? AND username == ?''',
#                                     (user_id, site, username))
#                         conn.commit()
#                         print("Your password has been successfully deleted!")
#                         sleep(2.5)
#                         break
#                     elif confirm == "N":
#                         break
#                     else:
#                         confirm = input("Please enter Y or N\n")
#     elif choix == "4":
#         system("cls")
#         mainMenu(conn, cur)
#     elif choix == "5":
#         sys.exit()
#     else:
#         print("Please enter a valid option")
#         sleep(2)
#     menuPassword(user_id, key, conn, cur)
#
#
# def getWebsites(cur, user_id, request):
#     cur.execute('''SELECT site FROM endpass WHERE user_id == ?''', (user_id,))
#     listSites = cur.fetchall()
#     nbSites = len(listSites)
#     if nbSites == 1:
#         site = listSites[0][0]
#     elif nbSites == 0:
#         return None, None
#     else:
#         sites = "Websites:\n"
#         index = 1
#         for i in range(len(listSites)):
#             sites += str(index) + ". " + listSites[i][0] + "\n"
#             index = index + 1
#         number = False
#         while not number:
#             print(sites)
#             site = input(request)
#             try:
#                 site = int(site)
#             except ValueError:
#                 print("Please enter a number between 1 and " + str(nbSites))
#                 sleep(2)
#             else:
#                 if 0 < site <= nbSites:
#                     site = listSites[site - 1][0]
#                     number = True
#                 else:
#                     print("Please enter a number between 1 and " + str(nbSites))
#                     sleep(2)
#     cur.execute("SELECT username, password FROM endpass WHERE site == ? AND user_id == ?", (site, user_id))
#     return cur.fetchall(), site
#
#
# def enterPw(prompt):
#     pw = ""
#     pwconfirm = "0"
#     while pw != pwconfirm:
#         pw = maskpass.askpass(prompt=prompt, mask="*")
#         pwconfirm = maskpass.askpass(prompt="Please confirm your password: ", mask="*")
#         if pw != pwconfirm:
#             print("Your passwords do not match, please try again")
#             sleep(1.5)
#     return pw
