import os
from tkinter import *
from tkinter import ttk

def create_repo():
    os.system("mkdir Repo && cd Repo && git init")

if __name__ == "__main__":
    root = Tk()
    frame = ttk.Frame(root, padding = 1)
    frame.grid()
    ttk.Button(frame, text="Create Repo", command=create_repo).grid(column=1,row=0)
    ttk.Button(frame, text="Exit", command=root.destroy).grid(column=1, row=1)
    root.mainloop()
