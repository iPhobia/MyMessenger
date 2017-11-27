from tkinter import *
import socket



def sendMessage(event):
    conn.send("'".encode() + entryValue.get().encode() + "': ".encode() + text.get().encode())
    text.set('')


# chat window
root = Tk()
root.title("Messenger")

    # establishing connection
conn = socket.socket()
conn.connect(("localhost", 14900))


text = StringVar()
entryValue = StringVar()

userLabel = Label(root)
msgLabel = Label(root, text = "Message:")
textbox = Text(root, width = 50, height = 15, font='Arial 10', wrap='word')
entry1 = Entry(root, textvariable = text, state = DISABLED)
enterUserNameLabel = Label(root, text="Enter username")
entry2 = Entry(root, textvariable = entryValue)

textbox.grid(row = 1)
entry1.grid(row = 3, sticky=NE + SW)
userLabel.grid(row=0)
msgLabel.grid(row=2,  sticky=W)
enterUserNameLabel.grid(row=4, sticky=W)
entry2.grid(row=5, sticky=NE + SW)

entry1.bind('<Return>',sendMessage)
def updateLable(event):
    userLabel["text"] = "User: " + entryValue.get()
    textbox.insert(1.0, "Hello " + entryValue.get() + '\n...................\nNow you can chat!\n...................\n')
    entry1.config(state = NORMAL)
entry2.bind('<Return>',updateLable)

def loopproc():
    textbox.see(END)
    conn.setblocking(False)
    try:
        message = conn.recv(128).decode()
        textbox.insert(END, message + '\n')
    except:
        root.after(1, loopproc)
        return
    root.after(1, loopproc)
    return

root.after(1, loopproc)
root.mainloop()


