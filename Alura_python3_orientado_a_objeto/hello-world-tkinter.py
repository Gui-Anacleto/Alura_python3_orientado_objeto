from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="{}".format()).grid(column=0, row=0)
ttk.Button(frm, text="1", ).grid(column=1, row=1)
ttk.Button(frm, text="2",).grid(column=2, row=1)
ttk.Button(frm, text="3",).grid(column=3, row=1)
ttk.Button(frm, text="4",).grid(column=1, row=2)
ttk.Button(frm, text="5",).grid(column=2, row=2)
ttk.Button(frm, text="6",).grid(column=3, row=2)
ttk.Button(frm, text="7",).grid(column=1, row=3)
ttk.Button(frm, text="8",).grid(column=2, row=3)
ttk.Button(frm, text="9",).grid(column=3, row=3)
ttk.Button(frm, text="0",).grid(column=2, row=4)

ttk.Button(frm, text="Exit", command=root.destroy).grid(column=2, row=5)

root.mainloop()