#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


def big(event):
    text['width'] = entry1.get()
    text['height'] = entry2.get()


def in_focus(event):
    text['bg'] = 'lightgrey'
    root['bg'] = 'lightgrey'
    but['bg'] = 'lightgrey'


def out_focus(event):
    text['bg'] = 'white'
    root['bg'] = 'white'
    but['bg'] = 'white'


root = Tk()

entry1 = Entry(root, width=5)
entry2 = Entry(root, width=5)
but = Button(root, width=15, text="Изменить")
text = Text(root, width=30)

entry1.grid(row=0, column=0, sticky=E, padx=5)
entry2.grid(row=1, column=0, sticky=E, padx=5)
but.grid(row=0, rowspan=2, column=1, sticky=W)
text.grid(row=3, column=0, columnspan=2, pady=5)

but.bind('<Button>', big)
text.bind('<FocusIn>', in_focus)
text.bind('<FocusOut>', out_focus)
root.mainloop()
