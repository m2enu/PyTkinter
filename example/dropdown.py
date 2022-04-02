import tkinter as tk
from tkinter import ttk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("400x300")

    items = ("Alice", "Bob", "Carol")

    # DropDownList
    val = tk.StringVar(value=items[1])
    opt = tk.OptionMenu(root, val, *items, command=lambda x:print(val.get(), x))
    opt.pack(pady=10)

    # Combobox
    cmb = ttk.Combobox(root, values=items, state="readonly")
    cmb.current(1)
    cmb.bind("<<ComboboxSelected>>", lambda x:print(cmb.get(), x))
    cmb.pack(pady=10)

    root.mainloop()