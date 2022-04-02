import tkinter as tk
import tkinter.ttk as ttk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("400x300")

    # Integer
    spinint = tk.Spinbox(master=root, state="readonly", from_=0, to_=10, increment=1)
    spinint.pack(pady=8)

    # Float
    spinflt = tk.Spinbox(master=root, state="readonly", from_=0, to_=1, increment=0.1, format="%3.1f")
    spinflt.pack(pady=8)

    # with StringVar
    val = tk.StringVar()
    val.set("Bob")
    members = ("Alice", "Bob", "Carol")
    spinstr = tk.Spinbox(master=root, state="readonly", textvariable=val, values=members)
    spinstr.pack(pady=8)

    # Integer via ttk
    ttkspinint = ttk.Spinbox(master=root, state="readonly", from_=0, to_=10, increment=1)
    ttkspinint.set(1)
    ttkspinint.pack(pady=8)

    root.mainloop()