import tkinter as tk
import tkinter.ttk as ttk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("600x400")

    tab = ttk.Notebook(master=root)
    tab.pack(expand=True)

    pages = (tk.Frame(master=tab, width=500, height=300) for i in range(3))
    for i, page in enumerate(pages):
        tab.add(page, text="Page{0}".format(i + 1))

    root.mainloop()