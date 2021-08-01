from tkinter import *
from tkinter import ttk

class Student():
    def __init__(self,root):
        self.root=root
        self.root.title("Studenti Management System")
        self.root.geometry("1378x700+0+0")

        title = Label(self.root, text="Manager Studenti", bd=9, relief=GROOVE, font=(" times new roman", 50,"bold"), bg="yellow", fg="red")
        title.pack(side=TOP,fill=X)


class Student():
    pass
    root = Tk()
    obj = Student(root)
    root.mainloop()

