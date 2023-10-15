import tkinter
from tkinter import *
class Vue(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        conteneur = tkinter.Frame(self)
        conteneur.pack(side="top", fill="both", expand=True) #sert à quoi?

        conteneur.grid_rowconfigure(0, weight = 1)
        conteneur.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for i in (Page1):
            frame = i(conteneur, self)

            self.frames[i] = frame

            frame.grid(row=0, column=0, sticky="nsew") #whatt
        self.show_frame(Page1)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class Page1(tkinter.Tk):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

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
                        bg="#9d9e9d",
                        activebackground="#9d9e9d",
                        command=send(user_entry, pw_entry))
        submit.pack()

        # -------------------------------------
        #window.bind("<Return>", send(user_entry, pw_entry))
        window.mainloop()


app = Vue()
app.mainloop()

