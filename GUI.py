import tkinter as tk
from tkinter import ttk
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


# ---------- Main Menu frame ----------
def load_main_menu_frame():
    # title
    title = ttk.Label(
        master=main_menu_frame,
        text="Bloc Buddys' Password Manager",
        font=("Calibri", 25))
    title.pack(pady=2.5)

    # Log in side
    left_side = ttk.Frame(master=main_menu_frame)
    left_side.pack(side='left')

    user_frame_ls = ttk.Frame(master=left_side)
    user_label_ls = ttk.Label(master=user_frame_ls,
                                text="Username: ")
    user_entry_ls = ttk.Entry(master=user_frame_ls,
                              width=30)
    user_frame_ls.pack()
    user_label_ls.pack(padx=5, pady=5, side='left')
    user_entry_ls.pack(padx=5, pady=5, side='right')

    pass_frame_ls = tk.Frame(master=left_side)
    pass_label_ls = ttk.Label(master=pass_frame_ls,
                                text="Password: ")
    pass_entry_ls = ttk.Entry(master=pass_frame_ls,
                              width=30)
    pass_frame_ls.pack()
    pass_label_ls.pack(padx=5, pady=5, side='left')
    pass_entry_ls.pack(padx=5, pady=5, side='right')

    log_in = ttk.Button(
        master=left_side,
        text="Log in")
    log_in.pack(pady=5)

    # Sign in side
    right_side = ttk.Frame(master=main_menu_frame)
    right_side.pack(padx=5, side='left')

    user_frame_rs = ttk.Frame(master=right_side)
    user_label_rs = ttk.Label(master=user_frame_rs,
                                text="Username: ")
    user_entry_rs = ttk.Entry(master=user_frame_rs,
                              width=30)
    user_frame_rs.pack()
    user_label_rs.pack(padx=5, pady=5, side='left')
    user_entry_rs.pack(padx=5, pady=5, side='left')

    pass_frame_rs = ttk.Frame(master=right_side)
    pass_label_rs = ttk.Label(master=pass_frame_rs,
                                text="Password: ")
    pass_entry_rs = ttk.Entry(master=pass_frame_rs,
                              width=30)
    pass_frame_rs.pack()
    pass_label_rs.pack(padx=5, pady=5, side='left')
    pass_entry_rs.pack(padx=5, pady=5, side='left')

    pass2_frame_rs = ttk.Frame(master=right_side)
    pass2_label_rs = ttk.Label(master=pass2_frame_rs,
                                 text="Confirm password: ")
    pass2_entry_rs = ttk.Entry(master=pass2_frame_rs,
                               width=30)
    pass2_frame_rs.pack()
    pass2_label_rs.pack(padx=5, pady=5, side='left')
    pass2_entry_rs.pack(padx=5, pady=5, side='left')

    sign_in = ttk.Button(
        master=right_side,
        text="Sign in")
    sign_in.pack(pady=2.5)

def load_password_list_frame():
    return password_list_frame



# ---------- Initialize application ----------
window = tk.Tk()
window.title("Bloc Buddy's Password Manager")
window.geometry("1000x300")

main_menu_frame = ttk.Frame(master=window)
password_list_frame = ttk.Frame(master=window)
frames_tuple = (main_menu_frame, password_list_frame)

for frame in frames_tuple:
    frame.grid(row=0, column=0, sticky='nsew')

load_main_menu_frame()

# ---------- Run ----------
window.mainloop()
