import tkinter as tk
import tkinter.ttk as ttk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("300x500")

    tkval = tk.IntVar(value=1)
    tkradio = (tk.Radiobutton(
        master=root, text="Item"+chr(0x31+i), value=i, variable=tkval, command=lambda:print(tkval.get()))
        for i in range(4))
    for radio in tkradio:
        radio.pack(pady=4)

    ttkval = tk.IntVar(value=1)
    ttkradio = (ttk.Radiobutton(
        master=root, text="Item"+chr(0x41+i), value=i, variable=ttkval)
        for i in range(4))
    for radio in ttkradio:
        radio.bind("<ButtonRelease>", lambda e: print(e, ttkval.get()))
        radio.pack(pady=4)

    root.mainloop()