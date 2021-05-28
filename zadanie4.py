#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *

root = Tk()

c = Canvas(root, width=1000, height=900, bg='#99ccff')
c.pack()

c.create_rectangle(350, 400, 650, 750, fill='#cc0066',
                   outline='#000000', width=3)

c.create_rectangle(450, 500, 550, 600, fill='#000000',
                   outline='#ffffff', width=3)

c.create_polygon((300, 400), (500, 200), (700, 400), fill='#660033', outline='#000000', width=3)

c.create_oval(700, 100, 850, 250, width=2, fill='yellow')

a = 0

while a < 2000:
    c.create_line(-300+a, 1000, -240+a, 725, fill='green', width=5)
    a += 25

root.mainloop()
