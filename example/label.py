import tkinter as tk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("400x300")

    label = tk.Label(master=root, text="hello world !")
    label.pack()

    root.mainloop()