import tkinter as tk
from tkinter import ttk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("600x600")

    # Table
    tree1 = ttk.Treeview(master=root, height=3, show="headings", columns=("id", "name"))
    tree1.column("id", anchor="center")
    tree1.column("name", anchor="w")
    tree1.heading("id", text="ID")
    tree1.heading("name", text="Name")
    for n, seq in enumerate( ((1234, "Alice"), (5678, "Bob")) ):
        tree1.insert(parent="", index=tk.END, iid=n, values=seq)
    tree1.pack(pady=10)

    # Tree
    tree2 = ttk.Treeview(master=root, height=5, show="tree")
    iid = tree2.insert(parent="" , index=tk.END, text="Item0", open=True )
    iid = tree2.insert(parent=iid, index=tk.END, text="Item1", open=True )
    iid = tree2.insert(parent=iid, index=tk.END, text="Item2", open=True )
    iid = tree2.insert(parent="" , index=tk.END, text="Item3", open=False)
    tree2.pack(pady=10)

    # Tree and Table
    tree3 = ttk.Treeview(master=root, height=10, columns=("data1", "data2"))
    tree3.heading("#0"   , text="Category")
    tree3.heading("data1", text="Data-1")
    tree3.heading("data2", text="Data-2")
    iid = tree3.insert("" , tk.END, open=True , text="Item0", values=("0-1", "0-2"))
    iid = tree3.insert(iid, tk.END, open=True , text="Item1", values=("1-1", "1-2"))
    iid = tree3.insert(iid, tk.END, open=True , text="Item2", values=("2-1", "2-2"))
    iid = tree3.insert("" , tk.END, open=True , text="Item3", values=("3-1", "3-2"))
    iid = tree3.insert(iid, tk.END, open=True , text="Item4", values=("4-1", "4-2"))
    iid = tree3.insert("" , tk.END, open=False, text="Item5", values=("5-1", "5-2"))
    tree3.pack(pady=10)

    root.mainloop()