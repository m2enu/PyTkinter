import tkinter as tk
from tkinter import messagebox

def OnButtonClicked():
    messagebox.showinfo(title=None, message="hello world !")

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("400x300")

    button = tk.Button(master=root, text="click", command=OnButtonClicked)
    button.pack(expand=True)

    root.mainloop()