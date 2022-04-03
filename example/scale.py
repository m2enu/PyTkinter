import tkinter as tk
import tkinter.ttk as ttk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("400x300")

    val1 = tk.DoubleVar(value=0.0)
    prog1 = tk.Scale(master=root, variable=val1, orient=tk.HORIZONTAL,
        length=300, from_=0, to_=255, command=lambda e: print(e, val1.get()))
    prog1.pack(pady=16)

    val2 = tk.DoubleVar(value=0.0)
    prog2 = ttk.Scale(master=root, variable=val2, orient=tk.HORIZONTAL,
        length=300, from_=0, to_=255, command=lambda e: print(e, val2.get()))
    prog2.pack(pady=16)

    root.mainloop()