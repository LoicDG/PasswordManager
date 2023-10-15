from tkinter import *
import time

win = Tk()

win.geometry("400x400")
win.title("Bloc Buddies Password Manager")

options = Frame(win)
sign_in = Frame(win)
create_account = Frame(win)
confirmation = Frame(win)
main_menu = Frame(win)

options.grid(row=0, column=0, sticky="nsew")
sign_in.grid(row=0, column=0, sticky="nsew")
main_menu.grid(row=0, column=0, sticky="nsew")
create_account.grid(row=0, column=0, sticky="nsew")
confirmation.grid(row=0, column=0, sticky="nsew")


def revenir_menu(frame_actuel):
    main_menu.tkraise()
    frame_actuel.pack_forget()

def aller_create_account(frame_actuel):
    create_account.tkraise()
    frame_actuel.pack_forget()

def aller_sign_in(frame_actuel):
    sign_in.tkraise()
    frame_actuel.pack_forget()

def aller_confirmation(frame_actuel):
    confirmation.tkraise()
    frame_actuel.pack_forget()

def aller_options(frame_actuel):
    options.tkraise()
    frame_actuel.pack_forget()

# ---- MAIN MENU ----
main_menu_titre = Label(main_menu,
              text="Bloc Buddies Password Manager",
              font=12
              )
main_menu_titre.pack()

main_menu_create_account_button = Button(main_menu, text="Create account", command=lambda: aller_create_account(main_menu))
main_menu_sign_in_button = Button(main_menu, text="Sign in", command=lambda : aller_sign_in(main_menu))
main_menu_quit_button = Button(main_menu, text="Quit")
main_menu_create_account_button.pack()
main_menu_sign_in_button.pack()
main_menu_quit_button.pack()

# ----- CREATE ACCOUNT -----
create_account_titre = Label(create_account,
              text="Bloc Buddies Password Manager",
              font=12
              )
create_account_titre.pack()

create_account_create_new_user = Label(create_account, text="Create new username: ")
create_account_create_new_user.pack()
create_account_new_user_entry = Entry(create_account)
create_account_new_user_entry.pack()

create_account_create_master_pass = Label(create_account, text="Create your master password: ")
create_account_create_master_pass.pack()
create_account_master_pass_entry = Entry(create_account, show="*")
create_account_master_pass_entry.pack()

create_account_button = Button(create_account, text="Submit", command=lambda: aller_confirmation(create_account))
create_account_button.pack()

# ----- CONFIRMATION -----
confirmation_titre = Label(confirmation,
              text="Bloc Buddies Password Manager",
              font=12
              )
confirmation_titre.pack()
confirmation_compte_label = Label(confirmation, text="Opération est un succès!")
confirmation_compte_bouton = Button(confirmation, text="Revenir au menu principal",
                                            command=lambda: revenir_menu(confirmation))
confirmation_compte_label.pack()
confirmation_compte_bouton.pack()

# ----- SIGN IN -----
sign_in_titre = Label(sign_in,
              text="Bloc Buddies Password Manager",
              font=12
              )
sign_in_titre.pack()

sign_in_user_lbl = Label(sign_in, text="Username: ")
sign_in_user_lbl.pack()
sign_in_user_entry = Entry(sign_in)
sign_in_user_entry.pack()

sign_in_master_pass = Label(sign_in, text="Create your master password: ")
sign_in_master_pass.pack()
sign_in_master_pass_entry = Entry(sign_in, show="*")
sign_in_master_pass_entry.pack()

sign_in_button = Button(sign_in, text="Submit", command=lambda: aller_options(sign_in))
sign_in_button.pack()


# ----- OPTIONS -----
opts_titre = Label(options,
              text="Bloc Buddies Password Manager",
              font=12
              )
opts_titre.pack()

opts_addNewPass = Button(options, text="Add a new password", command=lambda: aller_create_account(options))
opts_getExistingPass = Button(options, text="Get an existing password", command=lambda : aller_sign_in(main_menu))
opts_seeWebsites = Button(options, text="See what websites are associated with password")
opts_quit = Button(options, text="Quit")
opts_addNewPass.pack()
opts_getExistingPass.pack()
opts_seeWebsites.pack()
opts_quit.pack()

win.mainloop()
