import tkinter as tk
import tkinter.ttk as ttk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("400x300")

    tkval = tk.BooleanVar(value=True)
    tkchk = tk.Checkbutton(master=root, text="tk", variable=tkval, command=lambda:print(tkval.get()))
    tkchk.pack(pady=8)

    ttkval = tk.BooleanVar(value=True)
    ttkchk = ttk.Checkbutton(master=root, text="ttk", variable=ttkval)
    ttkchk.bind("<ButtonRelease>", lambda e: print(e, ttkval.get()))
    ttkchk.pack(pady=8)

    root.mainloop()