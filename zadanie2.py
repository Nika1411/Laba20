#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


def add_item(event):
    lbox_listbox.insert(END, entry.get())
    entry.delete(0, END)


def bb(event):
    select = list(lbox_listbox.curselection())
    select.reverse()
    for j in select:
        entry.insert(0, lbox_listbox.get(j))
        lbox_listbox.delete(j)


root = Tk()

lbox_listbox = Listbox(root, bg='#99ccff', width=50, selectmode=EXTENDED)
entry = Entry(root, width=50)


entry.pack()
lbox_listbox.pack()

entry.bind('<Return>', add_item)
lbox_listbox.bind('<Double-Button-1>', bb)

root.mainloop()
