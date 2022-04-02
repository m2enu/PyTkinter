import tkinter as tk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("400x300")

    val = tk.BooleanVar(value=True)
    checkbox = tk.Checkbutton(master=root, text="Enabled", variable=val, command=lambda:print(val.get()))
    checkbox.pack(expand=True)

    root.mainloop()