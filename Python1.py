from tkinter import *

root=Tk()
root.title("Python1")
root.geometry("500x300")

Mylabel=Label(root,text="Write your name",borderwidth=3, bg="blue", fg="white") #widget
Mylabel.pack()

input=Entry(root,fg="blue",width=56) #input
input.pack()


def onclick(): #function
    label1=Label(root,text="Yes,"+input.get()+" is a human")
    label1.pack()


btn=Button(root,text="Are you a human?",borderwidth=5,command=onclick) #button
btn.pack()


root.mainloop()  
