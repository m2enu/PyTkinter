import tkinter as tk
import tkinter.ttk as ttk

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("PyTkinter")
    root.geometry("600x400")

    progbars = (
        ttk.Progressbar(master=root, length=240, mode='determinate'  , orient=tk.HORIZONTAL),
        ttk.Progressbar(master=root, length=240, mode='indeterminate', orient=tk.HORIZONTAL),
        ttk.Progressbar(master=root, length=120, mode='determinate'  , orient=tk.VERTICAL  ),
        ttk.Progressbar(master=root, length=120, mode='indeterminate', orient=tk.VERTICAL  ),
    )
    progbars[0].grid(row=0, column=0, columnspan=2, padx=8, pady=8)
    progbars[1].grid(row=1, column=0, columnspan=2, padx=8, pady=8)
    progbars[2].grid(row=0, column=2, rowspan=2   , padx=8, pady=8)
    progbars[3].grid(row=0, column=3, rowspan=2   , padx=8, pady=8)

    def start():
        for p in progbars: p.start()
    def stop():
        for p in progbars: p.stop()
    def step():
        for p in progbars: p.step(2)

    buttons = (
        ttk.Button(master=root, text="Start", command=start),
        ttk.Button(master=root, text="Stop" , command=stop ),
        ttk.Button(master=root, text="Step" , command=step ),
    )
    for i, btn in enumerate(buttons):
        btn.grid(row=2, column=i, padx=8, pady=8)

    root.mainloop()
