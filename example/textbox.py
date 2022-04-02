import tkinter as tk
import tkinter.ttk as ttk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("400x600")

    # Single line via tk
    tktxts = tk.Entry(master=root)
    tktxts.insert(0, "hello tk world !")
    tktxts.pack(pady=8)

    # Single line via ttk
    ttktxts = ttk.Entry(master=root)
    ttktxts.insert(0, "hello ttk world !")
    ttktxts.pack(pady=8)

    # Multi lines via tk
    tktxtm = tk.Text(master=root, height=8)
    tktxtm.pack(pady=8)

    root.mainloop()