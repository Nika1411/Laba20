#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *

box1 = ["apple", "bananas", "carrot", "bread", "butter", "meat",
        "potato", "tomato", "milk"]


def move_to_right(event):
    select = list(lbox1_listbox.curselection())
    select.reverse()
    for j in select:
        lbox2_listbox.insert(0, lbox1_listbox.get(j))
        lbox1_listbox.delete(j)


def move_to_left(event):
    select = list(lbox2_listbox.curselection())
    select.reverse()
    for j in select:
        lbox1_listbox.insert(0, lbox2_listbox.get(j))
        lbox2_listbox.delete(j)


root = Tk()

lbox1_listbox = Listbox(root, selectmode=EXTENDED)
lbox2_listbox = Listbox(root, selectmode=EXTENDED)
but1 = Button(root, bg='#7d00ff', width=3, text='>>>')
but2 = Button(root, bg='#7d00ff', width=3, text='<<<')

but1.bind('<Button>', move_to_right)
but2.bind('<Button>', move_to_left)


lbox1_listbox.pack(side=LEFT)
lbox2_listbox.pack(side=RIGHT)
but2.pack(side=BOTTOM, padx=1, pady=0)
but1.pack(side=BOTTOM, padx=1, pady=0)


for i in box1:
    lbox1_listbox.insert(0, i)

root.mainloop()
