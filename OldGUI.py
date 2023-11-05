import tkinter
from tkinter import *

class GUI:
    def __init__(self, win):
        self.win = win
        self.win.geometry("400x400")
        self.win.title("Bloc Buddies Password Manager")

        self.frames = {}
        self.create_main_menu() #0
        self.create_account() #1
        self.create_sign_in() #2
        self.succes() #3

        #self.create

        self.frames[0].tkraise() #Show main menu on start


    def switch_frame(self, frame_actuel, prochain_frame):
        prochain_frame.tkraise()
        frame_actuel.pack_forget()

    def afficher_titre(self, frame):
        titre = Label(frame,
                  text="Bloc Buddies Password Manager",
                  font=12
                  )
        titre.pack()

    def create_master_account(self, user, pw):
        print("Account creation worked!", user, pw)
        createAccount(user, pw)

    def create_main_menu(self):
        frame = Frame(self.win)
        frame.grid(row=0, column=0, sticky="nsew")
        self.afficher_titre(frame)
        create_account_btn = Button(frame,
                                    text="Create account",
                                    command=lambda: self.switch_frame(frame, self.frames[1]))
        sign_in_btn = Button(frame,
                             text="Sign in",
                             command=lambda : self.switch_frame(frame, self.frames[2]))
        quit_btn = Button(frame, text="Quit")
        create_account_btn.pack()
        sign_in_btn.pack()
        quit_btn.pack()
        self.frames[0] = frame

    def create_account(self):
        frame = Frame(self.win)
        frame.grid(row=0, column=0, sticky="nsew")
        self.afficher_titre(frame)

        create_new_user_lbl = Label(frame, text="Create new username: ")
        create_new_user_entry = Entry(frame)
        create_new_user_lbl.pack()
        create_new_user_entry.pack()

        create_master_pass = Label(frame, text="Create your master password: ")
        create_master_pass.pack()
        create_master_pass_entry = Entry(frame, show="*")
        create_master_pass_entry.pack()

        create_account_button = Button(frame,
                                       text="Submit",
                                       command=lambda: (self.switch_frame(frame, self.frames[3]),
                                                        self.create_master_account(create_new_user_entry.get(),
                                                                                   create_master_pass_entry.get())))
        create_account_button.pack()

        quit_btn = Button(frame, text="Quit")
        quit_btn.pack()

        self.frames[1] = frame

    def create_sign_in(self):
        frame = Frame(self.win)
        frame.grid(row=0, column=0, sticky="nsew")
        self.afficher_titre(frame)

        quit_btn = Button(frame, text="Quit")
        quit_btn.pack()

        self.frames[2] = frame

    def succes(self):
        frame = Frame(self.win)
        frame.grid(row=0, column=0, sticky="nsew")
        self.afficher_titre(frame)
        succes = Label(frame, text="Nous avons réussi l'opération!")
        succes.pack()

        menu_btn = Button(frame, text="Revenir au menu")
        menu_btn.pack()

        quit_btn = Button(frame, text="Quit")
        quit_btn.pack()

        self.frames[3] = frame

    def run(self):
        self.win.mainloop()
    # # ----- CONFIRMATION -----
    # confirmation_titre = Label(confirmation,
    #           text="Bloc Buddies Password Manager",
    #           font=12
    #           )
    # confirmation_titre.pack()
    # confirmation_compte_label = Label(confirmation, text="Opération est un succès!")
    # confirmation_compte_bouton = Button(confirmation, text="Revenir au menu principal",
    #                                         command=lambda: revenir_menu(confirmation))
    # confirmation_compte_label.pack()
    # confirmation_compte_bouton.pack()
    #
    # # ----- SIGN IN -----
    # sign_in_titre = Label(sign_in,
    #           text="Bloc Buddies Password Manager",
    #           font=12
    #           )
    # sign_in_titre.pack()
    #
    # sign_in_user_lbl = Label(sign_in, text="Username: ")
    # sign_in_user_lbl.pack()
    # sign_in_user_entry = Entry(sign_in)
    # sign_in_user_entry.pack()
    #
    # sign_in_master_pass = Label(sign_in, text="Create your master password: ")
    # sign_in_master_pass.pack()
    # sign_in_master_pass_entry = Entry(sign_in, show="*")
    # sign_in_master_pass_entry.pack()
    #
    # sign_in_button = Button(sign_in, text="Submit", command=lambda: aller_options(sign_in))
    # sign_in_button.pack()
    #
    #
    # # ----- OPTIONS -----
    # opts_titre = Label(options,
    #           text="Bloc Buddies Password Manager",
    #           font=12
    #           )
    # opts_titre.pack()
    #
    # opts_addNewPass = Button(options, text="Add a new password", command=lambda: aller_create_account(options))
    # opts_getExistingPass = Button(options, text="Get an existing password", command=lambda : aller_sign_in(main_menu))
    # opts_seeWebsites = Button(options, text="See what websites are associated with password")
    # opts_quit = Button(options, text="Quit")
    # opts_addNewPass.pack()
    # opts_getExistingPass.pack()
    # opts_seeWebsites.pack()
    # opts_quit.pack()

win = tkinter.Tk()
app = GUI(win)
app.run()
