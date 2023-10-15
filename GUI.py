from tkinter import *
def send():
    user = user_entry.get()
    pw = pw_entry.get()
    print("This is the user: ", user)
    print("This is the pass: ", pw)

window = Tk()

window.geometry("500x500")
window.title("Bloc Buddies Password Manager")

# ----- TITRE -----
titre = Label(window,
              text="Bloc Buddies Password Manager",
              font=12
              )
titre.pack()

# ----- USER ENTRY -----
user_label = Label(window, text="Utilisateur: ")
user_label.pack()

user_entry = Entry(window)
user_entry.pack()

# ----- PASSWORD ENTRY -----
pw_label = Label(window,
                 text="Password: ")
pw_label.pack()

pw_entry = Entry(window,
                 show="*")
pw_entry.pack()

# ----- SUBMIT BUTTON -----
submit = Button(window,
                text="Submit",
                bg = "#9d9e9d",
                activebackground="#9d9e9d",
                command=send)
submit.pack()

# -------------------------------------
window.mainloop()

