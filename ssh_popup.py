from Tkinter import *
import sys

class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="username")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.l=Label(top,text="password")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.m = Message(self.master,text = "if you don't connect to a server your orders will cancel when you close this program.")
        self.m.pack()
        self.b=Button(master,text="SSH to server?",command=self.popup)
        self.b.pack()
        self.b2=Button(master,text="continue without connection.", command = exit)
        self.b2.pack()

    def popup(self):
        self.w=popupWindow(self.master)
        self.master.wait_window(self.w.top)

    def exit(self):
        self.master.destroy()

if __name__ == "__main__":
    root=Tk()
    m=mainWindow(root)
    root.mainloop()
