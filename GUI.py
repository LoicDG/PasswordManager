from tkinter import *
from DatabaseClean import *

launch()

# region --- CONSTANTS ---
bgColour = "#1c1b1c"
fgColour = "#97afe8"
windowDimensions = "420x600"
# endregion

# region --- WINDOW SETUP ---
window = Tk()
window.geometry(windowDimensions)
window.title("Bloc Buddies Password Manager")
window.config(background=bgColour)

titleLabel = Label(
    window,
    text="Bloc Buddies' Password Manager",
    font=("Arial", 15, "bold"),
    fg=fgColour,
    bg=bgColour,
    padx=10,
    pady=10
)
titleLabel.pack()
# endregion


# region --- DEFINING EVENTS ---
def switchToAccueil(oldFrame):
    frameAccueil.pack(fill="both", expand=1)
    oldFrame.forget()
def switchTo2(oldFrame):
    frame2.pack(fill="both", expand=1)
    oldFrame.forget()

def submitMasters():
    username = masterUsernameEntry.get()
    print("Works", username)
    switchTo2(frame1)

# endregion

# region --- FRAME ACCUEIL ---
# - defining the frame -
frameAccueil = Frame(
    window,
    bg=bgColour
)

# - defining the widgets -
signInButton = Button(
    frame1,
    text="Submit",
    font=("Arial", 10),
    command=submitMasters
)

logInButton = Button(
    frame1,
    text="Submit",
    font=("Arial", 10),
    command=submitMasters
)

# - showing widgets -
frameAccueil.pack(fill="both", expand="1")
signInButton.pack()
logInButton.pack()
# endregion


# region --- FRAME#1: MASTER USER & PASS ---
# - defining the frame -
frame1 = Frame(
    window,
    bg=bgColour
)

# - defining the widgets -

titleMasterUsername = Label(
    frame1,
    text="Master Username",
    font=("Arial", 10),
    fg=fgColour,
    bg=bgColour,
    padx=10,
    pady=10
)

masterUsernameEntry = Entry(
    frame1,
    font=("Arial", 10),
)

titleMasterPassword = Label(
    frame1,
    text="Master Password",
    font=("Arial", 10),
    fg=fgColour,
    bg=bgColour,
    padx=10,
    pady=10
)

masterPasswordEntry = Entry(
    frame1,
    font=("Arial", 10)
)
masterPasswordEntry.config(show="*")

space1 = Label(
    frame1,
    bg=bgColour,
    padx=10,
    pady=5
)

submitButton = Button(
    frame1,
    text="Submit",
    font=("Arial", 10),
    command=submitMasters
)

# - showing widgets -
titleMasterUsername.pack()
masterUsernameEntry.pack()
titleMasterPassword.pack()
masterPasswordEntry.pack()
space1.pack()
submitButton.pack()
# endregion

# region --- FRAME#2:  ---
# - defining the frame -
frame2 = Frame(
    window,
    bg=bgColour
)

# - defining the widgets -

# - showing widgets -

# endregion


# region --- FRAME#3: ---

# endregion

window.mainloop()