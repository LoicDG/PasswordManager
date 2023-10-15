from tkinter import *

win = Tk()

win.geometry("400x400")
win.title("Bloc Buddies Password Manager")

p2 = Frame(win)
p1 = Frame(win)


p1.grid(row=0, column=0, sticky="nsew")
p2.grid(row=0, column=0, sticky="nsew")

def aller_p2():
    p2.tkraise()
    p1.pack_forget()


# ---- FRAME P1 ----
p1_titre = Label(p1,
              text="Bloc Buddies Password Manager",
              font=12
              )
p1_titre.pack()

p1_user_label = Label(p1, text="Utilisateur: ")
p1_user_label.pack()
p1_user_entry = Entry(p1)
p1_user_entry.pack()

p1_master_pw_label = Label(p1,
                 text="Password: ")
p1_master_pw_label.pack()
p1_master_pw_entry = Entry(p1,
                 show="*")
p1_master_pw_entry.pack()

p1_submit = Button(p1,
                text="Submit",
                bg = "#9d9e9d",
                activebackground="#9d9e9d",
                command=lambda: aller_p2())
p1_submit.pack()


# ----- FRAME P2 -----
p2_titre = Label(p2,
              text="Bloc Buddies Password Manager",
              font=12
              )
p2_titre.pack()

p2_website_label = Label(p2, text="Site: ")
p2_website_label.pack()
p2_website_entry = Entry(p2)
p2_website_entry.pack()

p2_user_label = Label(p2, text="Utilisateur: ")
p2_user_label.pack()
p2_user_entry = Entry(p2)
p2_user_entry.pack()

p2_pw_label = Label(p2,
                 text="Password: ")
p2_pw_label.pack()
p2_pw_entry = Entry(p2,
                 show="*")
p2_pw_entry.pack()

# p2_submit = Button(p2,
#                 text="Submit",
#                 bg = "#9d9e9d",
#                 activebackground="#9d9e9d",
#                 command=send)
#p2_submit.pack()

win.mainloop()
