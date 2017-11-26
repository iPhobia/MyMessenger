import socket
import tkinter as tk
from tkinter import *

def connect(event):
    with socket.socket() as conn:
        conn.connect(("localhost", 14900))
        conn.send(b"client1")
        rawdata = conn.recv(1024)
        data = rawdata.decode("utf-8")
        textbox.insert(1.0, data + '\n')

root = tk.Tk()
root.geometry('400x400')
root.title("Messenger")
panelFrame = Frame(root, height = 60, bg = 'gray')
textFrame = Frame(root, height = 50, width = 50)

panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')

sendBtn = Button(panelFrame, text = 'Send')
sendBtn.bind('<Button-1>', connect)
sendBtn.place(x = 10, y = 10, width = 40, height = 40)
root.mainloop()