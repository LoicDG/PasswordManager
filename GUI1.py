from tkinter import *
def send():
    user = user_entry.get()
    master_pw = master_pw_entry.get()
    print("This is the user: ", user)
    print("This is the pass: ", master_pw)

window = Tk()

window.geometry("500x500")
window.title("Bloc Buddies Password Manager")

# ----- TITRE -----
titre1 = Label(window,
              text="Bloc Buddies Password Manager",
              font=12
              )
titre1.pack()

# ----- USER ENTRY -----
user_label = Label(window, text="Utilisateur: ")
user_label.pack()

user_entry = Entry(window)
user_entry.pack()

# ----- PASSWORD ENTRY -----
master_pw_label = Label(window,
                 text="Password: ")
master_pw_label.pack()

master_pw_entry = Entry(window,
                 show="*")
master_pw_entry.pack()

# ----- SUBMIT BUTTON -----
submit = Button(window,
                text="Submit",
                bg = "#9d9e9d",
                activebackground="#9d9e9d",
                command=send)
submit.pack()

# -------------------------------------
window.mainloop()

