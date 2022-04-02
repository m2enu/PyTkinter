import tkinter as tk
import tkinter.ttk as ttk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("400x300")

    lbltk = tk.Label(master=root, text="hello tk world !")
    lbltk.pack(pady=8)

    lblttk = ttk.Label(master=root, text="hello ttk world !")
    lblttk.pack(pady=8)

    root.mainloop()