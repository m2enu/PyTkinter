import tkinter as tk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("400x300")

    # Integer
    spinint = tk.Spinbox(master=root, state="readonly", from_=0, to_=10, increment=1)
    spinint.pack(expand=True)

    # Float
    spinflt = tk.Spinbox(master=root, state="readonly", from_=0, to_=1, increment=0.1, format="%3.1f")
    spinflt.pack(expand=True)

    # with StringVar
    val = tk.StringVar()
    val.set("Bob")
    members = ("Alice", "Bob", "Carol")
    spinstr = tk.Spinbox(master=root, state="readonly", textvariable=val, values=members)
    spinstr.pack(expand=True)

    root.mainloop()