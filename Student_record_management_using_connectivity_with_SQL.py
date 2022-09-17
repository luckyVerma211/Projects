import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='Student_management')

def addstudent():
    sid=int(input("Enter the Student ID:"))
    s_name=input("Enter the Student Name:")
    cl=int(input("Enter the Class of Student:"))
    sec=input("Enter the Section of the Student:")
    while True:
        phone_no=input("Enter the Student's Phone no:")
        if len(phone_no)!=10:
            print("INVALID PHONE NUMBER!!")
        else:
            break
    Total_fee=int(input("Enter the Total fees of Student:"))
    Paid_fee=int(input("Enter the Paid fees of Student:"))
    Rem_fee=Total_fee-Paid_fee
    q="insert into Fee values(%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(sid,s_name,cl,sec,phone_no,Total_fee,Paid_fee,Rem_fee)
    cr=mydb.cursor()
    cr.execute(q,val)
    print("STUDENT DETAILS ADDED SUCCESSFULLY!!!")
    mydb.commit()

def updatestudent():
    ch=int(input("Enter the Student ID:"))
    print("Press 1 - To update Student's Name")
    print("Press 2 - To update Student's Class")
    print("Press 3 - To update Student's Section")
    print("Press 4 - To update Student's Phone no")
    up=int(input("Enter the which details to be updated:"))
    if up==1:
        a=input("Enter the new name of the student:")
        q='update Fee set s_name=%s where sid=%s'
        val=(a,ch)
        cr=mydb.cursor()
        cr.execute(q,val)
        print("STUDENT DETAILS UPDATED SUCCESSFULLY!!!")
        mydb.commit()
    elif up==2:
        a=input("Enter the new class of the student:")
        q='update Fee set class=%s where sid=%s'
        val=(a,ch)
        cr=mydb.cursor()
        cr.execute(q,val)
        print("STUDENT DETAILS UPDATED SUCCESSFULLY!!!")
        mydb.commit()
    elif up==3:
        a=input("Enter the new section of the student:")
        q='update Fee set Section=%s where sid=%s'
        val=(a,ch)
        cr=mydb.cursor()
        cr.execute(q,val)
        print("STUDENT DETAILS UPDATED SUCCESSFULLY!!!")
        mydb.commit()
    elif up==4:
        a=input("Enter the new phone no of the student:")
        q='update Fee set Phone_no=%s where sid=%s'
        val=(a,ch)
        cr=mydb.cursor()
        cr.execute(q,val)
        print("STUDENT DETAILS UPDATED SUCCESSFULLY!!!")
        mydb.commit()
    else:
        print("INVALID CHOICE!!")
    
def updatefees():
    ch=int(input("Enter the Student ID:"))
    print("Press 1 - To update the Paid Fees")
    print("Press 2 - To update the Total Fees")
    up=int(input("Enter the choice:"))
    if up==1:
        a=int(input("Enter the Paid fee of the student:"))
        q='update Fee set Paid_fee=%s where sid=%s'
        val=(a,ch)
        cr=mydb.cursor()
        cr.execute(q,val)
        mydb.commit()
    if up==2:
        a=input("Enter the Total fee of the student:")
        q='update Fee set Total_fee=%s where sid=%s'
        val=(a,ch)
        cr=mydb.cursor()
        cr.execute(q,val)
        mydb.commit()
    if up==1 or up==2:
        q='update fee set Remaining_fee=Total_fee-Paid_fee where sid=%s'
        val=(ch,)
        cr=mydb.cursor()
        cr.execute(q,val)
        print("STUDENT FEES DETAILS UPDATED SUCCESSFULLY!!!")
        mydb.commit()
    else:
        print("INVALID CHOICE!!")

def showstudent():
    print("Press 1 - To see record of a Student")
    print("Press 2 - To see record of Student of a class")
    print("Press 3 - To see record of all Student")
    ch=int(input("Enter the choice:"))
    if ch==1:
        up=int(input("Enter the Student ID:"))
        q='select * from fee where sid=%s'
        val=(up,)
        cr=mydb.cursor()
        cr.execute(q,val)
        res=cr.fetchall()
        for i in res:
            print("SID\tSTUDENT NAME\t\tCLASS\tSECTION\tPHONE NO\tTOTAL FEES\tPAID FEES\tREMAINING")
            print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],'\t',i[4],'\t',i[5],"\t\t",i[6],"\t\t",i[7])
        mydb.commit()
    elif ch==2:
        up=int(input("Enter the Class:"))
        q="select * from fee where class="+str(up)
        cr=mydb.cursor()
        cr.execute(q)
        res=cr.fetchall()
        print("SID\tSTUDENT NAME\t\tCLASS\tSECTION\tPHONE NO\tTOTAL FEES\tPAID FEES\tREMAINING")
        for i in res:
            print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],'\t',i[4],'\t',i[5],"\t\t",i[6],"\t\t",i[7])
        mydb.commit()
    elif ch==3:
        q="select * from fee"
        cr=mydb.cursor()
        cr.execute(q)
        res=cr.fetchall()
        print("SID\tSTUDENT NAME\t\tCLASS\tSECTION\tPHONE NO\tTOTAL FEES\tPAID FEES\tREMAINING")
        for i in res:
            print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],'\t',i[4],'\t',i[5],"\t\t",i[6],"\t\t",i[7])
        mydb.commit()
    
    else:
        print("INVALID CHOICE!!")

def login():
    print("-"*30)
    print("\t LOGIN SCREEN ")
    print("-" * 30)
    user=input("Enter the USER NAME:")
    passw=input("Enter the Password:")
    if user=='ALCODERS' and passw=='@AL123':
        return True
    else:
        print("Invalid username or password!!")

if login()==True:
    print("LOGIN SUCCESSFULLY!!")
    while True:
        print("-" * 30)
        print("\nSCHOOL MANAGEMENT SYSTEM")
        print("-" * 30)
        print("Press 1 - To Add A Student")
        print("Press 2 - To Modify A Student's Details")
        print("Press 3 - To Update Fee Structure A Student")
        print("Press 4 - To Display The Record of Student")
        print("Press 5 - To Exist")
        choice=int(input("Enter your choice:"))
        if choice==1:
            addstudent()
        elif choice==2:
            updatestudent()
        elif choice==3:
            updatefees()
        elif choice==4:
            showstudent()
        else:
            print("Visit Again!!")
            break
