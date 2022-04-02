import tkinter as tk
import tkinter.ttk as ttk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("400x300")

    items = ("Alice", "Bob", "Carol")

    # OptionMenu
    val = tk.StringVar(value=items[1])
    opt = tk.OptionMenu(root, val, *items, command=lambda e:print(e, val.get()))
    opt.pack(pady=10)

    # Combobox
    cmb = ttk.Combobox(root, values=items, state="readonly")
    cmb.current(1)
    cmb.bind("<<ComboboxSelected>>", lambda e:print(e, cmb.get()))
    cmb.pack(pady=10)

    root.mainloop()