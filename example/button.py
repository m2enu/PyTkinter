import tkinter as tk
import tkinter.ttk as ttk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("400x300")

    # Button via Tk
    btntk = tk.Button(master=root, text="tk", command=lambda:print("Clicked: tk"))
    btntk.pack(pady=8)

    # Button via Ttk
    btnttk = ttk.Button(master=root, text="ttk")
    btnttk.bind("<ButtonRelease>", lambda e:print("Clicked: ttk", e))
    btnttk.pack(pady=8)

    root.mainloop()