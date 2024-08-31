from tkinter import *
import win32com.client as w

root=Tk()
root.title(" Simple Calculator APP")




    # while True:
    #     x=input("ENter what you want to speak: ")
    #     if x=='q':
    #         speak.speak("say 'bye bye friend'")
    #         break
    #     command=f"{x}";
    #     speak.speak(command)

if __name__=='__main__':
    speak=w.Dispatch("SAPI.SpVoice")
    speak.speak("Welcome")
    
    e=Entry(root,fg="black",borderwidth=5,bg="grey",width=35)
    e.grid(row=0,column=0,columnspan=3)


    def Button_click(number):
        current_num=e.get()
        e.delete(0,END)
        e.insert(0,str(current_num)+str(number))

    def Button_add():
        first_number=e.get()
        global f_num
        f_num=int(first_number)
        global op
        op="addition"
        e.delete(0,END)

    def Button_subtract():
        first_number=e.get()
        global f_num
        f_num=int(first_number)
        global op
        op="subtraction"
        e.delete(0,END)
    

    def Button_multiply():
        first_number=e.get()
        global f_num
        f_num=int(first_number)
        global op
        op="multiply"
        e.delete(0,END)


    def Button_divide():
        first_number=e.get()
        global f_num
        f_num=int(first_number)
        global op
        op="divide"
        e.delete(0,END)


    def Button_equal():
        second_number=e.get()
        e.delete(0,END)
        global op,num
        if op=="addition":
            e.insert(0,f_num+int(second_number))
        elif op=="subtraction":
            e.insert(0,f_num-int(second_number))
        elif op=="multiply" :
            e.insert(0,f_num*int(second_number))
        elif op=="divide":
            if int(second_number) != 0:  # Check for division by zero
                e.insert(0, f_num / int(second_number))
            else:
                speak.speak("Invalid operation")
                e.insert(0, "Error: Division by zero")
        else:
            e.insert(0, "Error: Invalid operation")

        
    def Button_clear():
        e.delete(0,END)

    Button_1=Button(root,text="1",fg="black",bg="white",padx=30,pady=20,command=lambda:Button_click(1))
    Button_2=Button(root,text="2",fg="black",bg="white",padx=30,pady=20,command=lambda:Button_click(2))
    Button_3=Button(root,text="3",fg="black",bg="white",padx=30,pady=20,command=lambda:Button_click(3))
    Button_4=Button(root,text="4",fg="black",bg="white",padx=30,pady=20,command=lambda:Button_click(4))
    Button_5=Button(root,text="5",fg="black",bg="white",padx=30,pady=20,command=lambda:Button_click(5))
    Button_6=Button(root,text="6",fg="black",bg="white",padx=30,pady=20,command=lambda:Button_click(6))
    Button_7=Button(root,text="7",fg="black",bg="white",padx=30,pady=20,command=lambda:Button_click(7))
    Button_8=Button(root,text="8",fg="black",bg="white",padx=30,pady=20,command=lambda:Button_click(8))
    Button_9=Button(root,text="9",fg="black",bg="white",padx=30,pady=20,command=lambda:Button_click(9))
    Button_0=Button(root,text="0",fg="black",bg="white",padx=30,pady=20,command=lambda:Button_click(0))
    Button_add=Button(root,text="+",fg="black",bg="white",padx=30,pady=20,command=Button_add)
    Button_equal=Button(root,text="=",fg="black",bg="white",padx=70,pady=20,command=Button_equal)
    Button_clear=Button(root,text="clear",fg="black",bg="white",padx=60,pady=20,command=Button_clear)
    Button_subtract=Button(root,text="-",fg="black",bg="white",padx=30,pady=20,command=Button_subtract)
    Button_multiply=Button(root,text="*",fg="black",bg="white",padx=30,pady=20,command=Button_multiply)
    Button_divide=Button(root,text="/",fg="black",bg="white",padx=30,pady=20,command=Button_divide)



    Button_1.grid(row=3,column=0)
    Button_2.grid(row=3,column=1)
    Button_3.grid(row=3,column=2)

    Button_4.grid(row=2,column=2)
    Button_5.grid(row=2,column=1)
    Button_6.grid(row=2,column=0)

    Button_7.grid(row=1,column=0)
    Button_8.grid(row=1,column=1)
    Button_9.grid(row=1,column=2)

    Button_0.grid(row=4,column=0)
    Button_add.grid(row=5,column=0)
    Button_equal.grid(row=5,columnspan=2,column=1)
    Button_clear.grid(row=4,columnspan=2,column=1)
    Button_subtract.grid(row=6,column=0)
    Button_multiply.grid(row=6,column=2)
    Button_divide.grid(row=6,column=1)



    
    root.mainloop()
