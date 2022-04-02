import tkinter as tk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("300x400")

    val = tk.IntVar(value=1)
    radioboxes = (tk.Radiobutton(
        master=root, text="Item"+chr(0x31+i), value=i, variable=val, command=lambda:print(val.get()))
        for i in range(4))
    for radio in radioboxes:
        radio.pack(expand=True)

    root.mainloop()