import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password='1234')
'''if mydb.is_connected():
    print("Connected successfully!!")'''
cr = mydb.cursor()
q = "Create database restaurant_management"
cr.execute(q)
q = "use restaurant_management"
cr.execute(q)
q = '''Create table cust(
    CId varchar(5) primary key,
    C_Name varchar(30) not null,
    Date date not null,
    Bill integer not null ,
    Review varchar(50))'''
cr.execute(q)
mydb.commit()
print("Database Initialised")