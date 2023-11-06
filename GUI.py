from tkinter import *
from DatabaseClean import *

launch()

# region --- CONSTANTS ---
bgColour = "#1c1b1c"
fgColour = "#97afe8"
red = "#d1192b"
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
)
titleLabel.pack(padx=10, pady=10)
# endregion

# region --- DEFINING EVENTS ---
def switchFrames(oldFrame, newFrame):
    newFrame.pack(fill="both", expand="1")
    oldFrame.forget()
def submitSignIn(currentFrame, username, password, confirmPW):
    # erreur aura une valeur si et seulement s'il y a une erreur
    erreur = createUser(username, password, confirmPW)

    if erreur is not None:
        errorMsg = Label(
            currentFrame,
            text=erreur,
            fg=red,
        )
        errorMsg.pack()
        if erreur == "The passwords do not match":
            masterPasswordEntrySignIn.delete(0, "end")
            masterPasswordEntrySignInConfirm.delete(0, "end")
            masterPasswordEntrySignIn.focus_force()

def submitLogIn(currentFrame, username, password):
    erreur = logIn(username, password)

    if erreur is not None:
        errorMsg = Label(
            currentFrame,
            text=erreur,
            fg=red,
        )
        errorMsg.pack()

# endregion

# region --- FRAME: SIGN IN---
frameSignIn = Frame(
    window,
    bg=bgColour
)

# - defining the widgets -
titleMasterUsernameSignIn = Label(
    frameSignIn,
    text="Master Username",
    font=("Arial", 10),
    fg=fgColour,
    bg=bgColour
)

masterUsernameEntrySignIn = Entry(
    frameSignIn,
    font=("Arial", 10),
)

titleMasterPasswordSignIn = Label(
    frameSignIn,
    text="Master Password",
    font=("Arial", 10),
    fg=fgColour,
    bg=bgColour
)

masterPasswordEntrySignIn = Entry(
    frameSignIn,
    font=("Arial", 10)
)
titleMasterPasswordConfirm = Label(
    frameSignIn,
    text="Confirm your password",
    font=("Arial", 10),
    fg=fgColour,
    bg=bgColour
)
masterPasswordEntrySignIn.config(show="*")
masterPasswordEntrySignInConfirm = Entry(
    frameSignIn,
    font=("Arial", 10)
)
masterPasswordEntrySignInConfirm.config(show="*")

spaceSignIn = Label(
    frameSignIn,
    bg=bgColour,
)

submitButtonSignIn = Button(
    frameSignIn,
    text="Submit",
    font=("Arial", 10),
    command=lambda: submitSignIn(frameSignIn, masterUsernameEntrySignIn.get(), masterPasswordEntrySignIn.get(),
                                 masterPasswordEntrySignInConfirm.get())
)

# - showing widgets -
titleMasterUsernameSignIn.pack(padx=5, pady=5)
masterUsernameEntrySignIn.pack(padx=5, pady=5)
titleMasterPasswordSignIn.pack(padx=5, pady=5)
masterPasswordEntrySignIn.pack(padx=5, pady=5)
submitButtonSignIn.pack(padx=5, pady=5)
# endregion

# region --- FRAME: LOG IN ---
frameLogIn = Frame(
    window,
    bg=bgColour
)

# - defining the widgets -
titleMasterUsernameLogIn = Label(
    frameLogIn,
    text="Master Username",
    font=("Arial", 10),
    fg=fgColour,
    bg=bgColour,
)

masterUsernameEntryLogIn = Entry(
    frameLogIn,
    font=("Arial", 10)
)

titleMasterPasswordLogIn = Label(
    frameLogIn,
    text="Master Password",
    font=("Arial", 10),
    fg=fgColour,
    bg=bgColour
)

masterPasswordEntryLogIn = Entry(
    frameLogIn,
    font=("Arial", 10)
)
masterPasswordEntryLogIn.config(show="*")

submitButtonLogIn = Button(
    frameLogIn,
    text="Submit",
    font=("Arial", 10),
    command=lambda: submitLogIn(frameLogIn, masterUsernameEntrySignIn.get(), masterPasswordEntrySignIn.get())
)

# - showing widgets -
titleMasterUsernameLogIn.pack(padx=5, pady=5)
masterUsernameEntryLogIn.pack(padx=5, pady=5)
titleMasterPasswordLogIn.pack(padx=5, pady=5)
masterPasswordEntryLogIn.pack(padx=5, pady=5)
titleMasterPasswordConfirm.pack(padx=5, pady=5)
masterPasswordEntrySignInConfirm.pack(padx=5, pady=5)
submitButtonLogIn.pack(padx=5, pady=5)
# endregion

# region --- FRAME: ACCUEIL ---
frameAccueil = Frame(
    window,
    bg=bgColour
)

# - defining the widgets -
signInButton = Button(
    frameAccueil,
    text="Sign In",
    font=("Arial", 10),
    command=lambda: switchFrames(frameAccueil, frameSignIn)
)

logInButton = Button(
    frameAccueil,
    text="Log In",
    font=("Arial", 10),
    command=lambda: switchFrames(frameAccueil, frameLogIn)
)

# - showing widgets -
signInButton.pack()
logInButton.pack()
# endregion

frameAccueil.pack(fill="both", expand="1")
window.mainloop()