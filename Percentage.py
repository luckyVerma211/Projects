from tkinter import *
def add():
    n1=eval(t1.get())
    n2=eval(t2.get())
    n3=eval(t3.get())
    n4=eval(t4.get())
    n5=eval(t5.get())
    n6=eval(t6.get())
    res=n1+n2+n3+n4+n5+n6
    l4.configure(text="Sum of marks is:"+str(res))
def per():
    n1=eval(t1.get())
    n2=eval(t2.get())
    n3=eval(t3.get())
    n4=eval(t4.get())
    n5=eval(t5.get())
    n6=eval(t6.get())
    res=n1+n2+n3+n4+n5+n6
    tot=(res/600)*100
    l4.configure(text="Percentage is:"+str(tot))
def result():
    m=nam.get()
    n1=eval(t1.get())
    n2=eval(t2.get())
    n3=eval(t3.get())
    n4=eval(t4.get())
    n5=eval(t5.get())
    n6=eval(t6.get())
    res=n1+n2+n3+n4+n5+n6
    n=(res/600)*100
    if n>95:
        l4.configure(text=m+"got Grade A+ !!")
    elif n>90:
        l4.configure(text=m+"got Grade A !!")
    elif n>85:
        l4.configure(text=m+"got Grade B+ !!")
    elif n>80:
        l4.configure(text=m+"got Grade B !!")
    elif n>70:
        l4.configure(text=m+"got Grade C !!")
    elif n>60:
        l4.configure(text=m+"got Grade D+ !!")
    elif n>50:
        l4.configure(text=m+"got Grade D !!")
    elif n>40:
        l4.configure(text=m+"got Grade E+ !!")
    elif n>35:
        l4.configure(text=m+"got Grade E !!")
    else:
        l4.configure(text=m+"got Grade F !!")
cal=Tk()
cal.title("MARKS CALCULATOR")
l1=Label(cal,text="!!!!WELCOME TO THE RESULT CALCULATOR!!!!",foreground="Green", background="yellow", font=("Monotype Corsiva",18))
h=Label(cal,text="Enter your name:")
l2=Label(cal,text="Enter marks of Mathematics:")
l3=Label(cal,text="Enter marks of Physics:")
l4=Label(cal,text="Enter marks of Chemistry:")
l5=Label(cal,text="Enter marks of English Core:")
l6=Label(cal,text="Enter marks of Fifth Subject(CS/IP/PE):")
l7=Label(cal,text="Enter marks of Sixth subject(Yoga/Vocal/Fine Arts):")
l1.place(x=110, y=50)
h.place(x=100, y=90)
l2.place(x=100, y=120)
l3.place(x=100, y=150)
l4.place(x=100, y=180)
l5.place(x=100, y=210)
l6.place(x=100, y=240)
l7.place(x=100, y=270)
nam=Entry(cal, width=10)
t1=Entry(cal, width=10)
t2=Entry(cal, width=10)
t3=Entry(cal, width=10)
t4=Entry(cal, width=10)
t5=Entry(cal, width=10)
t6=Entry(cal, width=10)
nam.place(x=300, y=90)
t1.place(x=300, y=120)
t2.place(x=300, y=150)
t3.place(x=300, y=180)
t4.place(x=300, y=210)
t5.place(x=375, y=240)
t6.place(x=375, y=270)
b1=Button(cal,text="TOTAL MARKS",command=add,font=("Arial",15))
b2=Button(cal,text="PERCENTAGE",command=per,font=("Arial",15))
b3=Button(cal,text="GRADE", command=result,font=("Arial",15))
b1.place(x=150, y=290)
b2.place(x=350, y=290)
b3.place(x=550,y=290)
l4=Label(cal,text="Result",font=("forte",15),foreground="#7F00FF")
l4.place(x=330, y=350)
cal.mainloop()
