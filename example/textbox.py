import tkinter as tk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("400x600")

    # Single line
    tbsingle = tk.Entry(master=root)
    tbsingle.insert(0, "hello world !")
    tbsingle.pack(pady=10)

    # Multi lines
    tbmulti = tk.Text(master=root, height=10)
    tbmulti.pack(pady=10)

    root.mainloop()