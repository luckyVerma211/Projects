from prettytable import PrettyTable
import time as t
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='restaurant_management')

#starters menu
Starters={1:['Air Fryer Zucchini Chips','₹220',220],2:['Batata Vada','₹150',150],3:['Bang Bang Cauliflower','₹340',340],
4:['Pani Puri','₹230',230],5:['Panner Tikka','₹360',360],6:['Panner 65','₹280',280],7:['Veg Kabab','₹210',210],
8:['Panner Manchurian Dry','₹250',250],9:['Manchurian Dry','200',200],10:['Veg Momos','₹180',180],
11:['Kurkure Momos','₹230',230],12:['Spring Roll','₹260',260],13:['Veg Cutlet','₹160',160],
14:['Mushroom Manchurain(Dry)','₹240',240],15:['Gobi Manchurain(Dry)','₹180',180],16:['Baked Samosa','₹190',190],
17:['Papri Chaat','₹230',230],18:['Veg Manchow Soup','₹210',210],19:['Sweet Corn Soup','₹170',170],
19:['Mixed Vegetable Soup','₹190',190],20:['Dry Chilli Potato','₹250',250],21:['Crispy Baby Corn Chilli','₹270',270],
22:['Red Sauce Pasta','₹300',300],23:['White Sauce Pasta','₹320',320],24:['Pink Sauce Pasta','₹310',310],
25:['Soya Chilli(Dry)','₹290',290],26:['Panner Chilli','₹200',200]}

#non veg starters menu
Non_Veg_Starters={1:['Egg Manchurian','₹190',190],2:['Egg Spring Roll','₹240',240],3:['Chilly Chicken','₹350',350],
4:['Chicken 65','₹370',370],5:['Chicken Lollipop','₹380',380],
6:['Chicken Manchurain','₹340',340],7:['Lemon Chicken','₹300',300],8:['Apolo Fish','₹290',290],
9:['Ginger Fish','₹370',370],10:['Chicken Shanghai','₹330',330],11:['Prawns','₹400',400],
12:['Prawns Manchurian','₹430',430],13:['Ginger Prawns','₹450',450],14:['Chicken Wings','₹390',390],
15:['Soya Chicken','₹360',360]}

#veg main course menu
Veg_Main_Course={1:['Panner Butter Masala','₹350',350],2:['Shahi Panner','₹300',300],3:['Mattar Panner','₹280',280],
4:['Kadai Panner','₹340',340],5:['Palak Paneer','₹310',310],6:['Mix Veg','₹300',300],7:['Kaju Panner','₹450',450],
8:['Aloo Gobhi','₹270',270],9:['Dal Tadka','₹290',290],10:['Malai Kofta','₹320',320],11:['Veg Kofta','₹300',300],
12:['Panner Do Pyaza','₹340',340],13:['Aloo Mattar','₹250',250],14:['Panner Tikka Masala','₹370',370],
15:['Channa Masala','₹290',290],16:['Pav Bhaji','₹300',300],17:['Chola Bhatura','₹260',260],18:['Rajma','₹290',290],
19:['Dhokla','₹300',300],20:['Idli & Sambhar','₹320',320]}

#non veg main course
Non_Veg_Main_Course={1:['Chicken Butter Masala','₹450',450],2:['Chicken Handi','₹420',420],3:['Chicken Briyani','₹400',400],
4:['Tandoori Chicken','₹430',430],5:['Desi Chicken Curry','₹300',300],6:['Chicken masala','₹380',380],
7:['Chicken Shwarma','₹390',390],8:['Chicken Tikka Masala','₹450',450],9:['Chicken Do Pyaza','₹420',420],
10:['Kolaha Puri Chicken Curry','₹470',470],11:['Amritsari Chicken Masala','₹490',490],12:['Chicken Dum Briyani','₹410',410],
13:['Hyderbadi Chicken Briyani','₹380',380],14:['Desi Mutton Curry','₹500',500],15:['Rogan Josh Mutton','₹690',690],
16:['Awadhi Mutton Briyani','₹590',590],17:['Sindhi Mutton Fry','₹550',550],18:['Dhabe de Kimma','₹600',600],
19:['Badami Lamb Korma','₹670',670],20:['Desi Fish Curry','₹300',300],21:['Red Hot Chilli Fish Fry','₹360',360],
22:['Goan Fish Curry','₹370',370],23:['Raw Mango Fish Curry','₹450',450],24:['Bengali Doi Maach','₹310',310],
25:['Rohu Fish Curry','₹470',470]}

#deserts
Deserts={1:['Red valvet Pastry','₹150',150],2:['White valvet Pastry','₹150',150],3:['Choco Lava Cake','₹210',210],
4:['Fruit Custard','₹160',160],5:['Apple and Butterscotch Pie','₹250',250],6:['Molten Chocolate Pudding','₹200',200],
7:['Almond Banana','₹190',190],8:['Kesar Kulfi','₹150',150],9:['Butterscotch Icecream','₹160',160],10:['Chocolate Icecream','₹120',120],
11:['Strawberry Icecream','₹130',130],12:['Vanilla Icecream','₹100',100],13:['Chocolate Bullets','₹190',190],
14:['Apple Crumble Desert Cake','₹250',250],15:['Tarts','₹280',280],16:['Butter Cake','₹360',360],17:['Black Forest Cake','₹400',400],
18:['Pineapple Cake','₹390',390],19:['Coffee Cake','₹350',350],20:['Layer Cake','₹340',340]}

#beverage
Beverage={1:['Hot Coffee','₹100',100],2:['Hot Leci Tea','₹90',90],3:['Ice Cold Coffee','₹120',120],4:['Americano','₹200',200],
5:['Cappuccino','₹250',250],6:['Espresso','₹240',240],7:['Flat White','₹270',270]}

#fast food
fast_food={1:['Farmhouse Pizza',"₹300",300],2:['Indi Tandoori Paneer Pizza','₹350',350],3:['Peppy Paneer Pizza','₹280',280],
4:['Veg Extravaganza Pizza','₹320',320],5:['Veggie Paradise','₹290',290]}

#additional items
Additional_Items={1:['Butter Naan Basket','₹180',180],2:['Tandoori Roti Basket','₹130',130],3:['Butter Roti Basket','₹100',100],
4:['Plain Roti Basket','₹80',80],5:['Lachha Paratha Basket','₹150',150],6:['Plain Naan Basket','₹170',170],
7:['Plain Rice Bowl','₹90',90],8:['Jeera Rice Bowl','₹110',110],9:['Veg Fried Rice Bowl','₹140',140],10:['Mineral Water','₹80',80]}

order1=[]
order2=[]
order3=[]
order4=[]
order5=[]
order6=[]
order7=[]
order8=[]
Order=[]

def order():
    while True:
        print("What would you like to have",name," Sir/Maam!!")
        print("Press 1 - For Veg Starter")
        print("Press 2 - For Non-Veg Starter")
        print("Press 3 - For Veg Main Course")
        print("Press 4 - For Non Veg Main Course")
        print("Press 5 - For Deserts")
        print("Press 6 - For Beverage")
        print("Press 7 - For Fast Food")
        print("Press 8 - For Additional Items")
        print("Press 9 - Exit")
        ch=int(input("Enter Your Choice Sir/Maam:"))
        if ch==1:
            print("🥰"*40)
            for i in Starters:
                print(i,"::",Starters[i][0],Starters[i][1])
            print("🥰"*40)
            a=input("Do you want to order(yes/no):")
            while a.lower()=='yes':
                n=int(input("Enter the choice:"))
                if n in Starters.keys():
                    order1.append(n)
                else:
                    print("Invalid Choice")
                a=input("Do you want to order more(yes/no):")
        if ch==2:
            print("🥰"*40)
            for i in Non_Veg_Starters:
                print(i,"::",Non_Veg_Starters[i][0],Non_Veg_Starters[i][1])
            print("🥰"*40)
            a=input("Do you want to order(yes/no):")
            while a.lower()=='yes':
                n=int(input("Enter the choice:"))
                if n in Non_Veg_Starters.keys():
                    order2.append(n)
                else:
                    print("Invalid Choice")
                a=input("Do you want to order more(yes/no):")
        
        if ch==3:
            print("🥰"*40)
            for i in Veg_Main_Course:
                print(i,"::",Veg_Main_Course[i][0],Veg_Main_Course[i][1])
            print("🥰"*40)
            a=input("Do you want to order(yes/no):")
            while a.lower()=='yes':
                n=int(input("Enter the choice:"))
                if n in Veg_Main_Course.keys():
                    order3.append(n)
                else:
                    print("Invalid Choice")
                a=input("Do you want to order(yes/no):")

        if ch==4:
            print("🥰"*40)
            for i in Non_Veg_Main_Course:
                print(i,"::",Non_Veg_Main_Course[i][0],Non_Veg_Main_Course[i][1])
            print("🥰"*40)
            a=input("Do you want to order(yes/no):")
            while a.lower()=='yes':
                n=int(input("Enter the choice:"))
                if n in Non_Veg_Main_Course.keys():
                    order4.append(n)
                else:
                    print("Invalid Choice")
                a=input("Do you want to order(yes/no):")
    
    
        if ch==5:
            print("🥰"*40)
            for i in Deserts:
                print(i,"::",Deserts[i][0],Deserts[i][1])
            print("🥰"*40)
            a=input("Do you want to order(yes/no):")
            while a.lower()=='yes':
                n=int(input("Enter the choice:"))
                if n in Deserts.keys():
                    order5.append(n)
                else:
                    print("Invalid Choice")
                a=input("Do you want to order(yes/no):")
        
        if ch==6:
            print("🥰"*40)
            for i in Beverage:
                print(i,"::",Beverage[i][0],Beverage[i][1])
            print("🥰"*40)
            a=input("Do you want to order(yes/no):")
            while a.lower()=='yes':
                n=int(input("Enter the choice:"))
                if n in Beverage.keys():
                    order6.append(n)
                else:
                    print("Invalid Choice")
                a=input("Do you want to order(yes/no):")
        
        if ch==7:
            print("🥰"*40)
            for i in fast_food:
                print(i,"::",fast_food[i][0],fast_food[i][1])
            print("🥰"*40)
            a=input("Do you want to order(yes/no):")
            while a.lower()=='yes':
                n=int(input("Enter the choice:"))
                if n in fast_food.keys():
                    order7.append(n)
                else:
                    print("Invalid Choice")
                a=input("Do you want to order(yes/no):")
        
        if ch==8:
            print("🥰"*40)
            for i in Additional_Items:
                print(i,"::",Additional_Items[i][0],Additional_Items[i][1])
            print("🥰"*40)
            a=input("Do you want to order(yes/no):")
            while a.lower()=='yes':
                n=int(input("Enter the choice:"))
                if n in Additional_Items.keys():
                    order8.append(n)
                else:
                    print("Invalid Choice")
                a=input("Do you want to order(yes/no):")
        else:
            break

def cancel_order():
    ans=input("Do you want to cancel the order(yes/no):")
    if ans.lower()=='yes':
        while True:
            print("🥰"*40)
            print("Press 1 - To Cancel Veg Starter")
            print("Press 2 - To Cancel Non-Veg Starter")
            print("Press 3 - To Cancel Veg Main Course")
            print("Press 4 - To Cancel Non Veg Main Course")
            print("Press 5 - To Cancel Deserts")
            print("Press 6 - To Cancel Beverage")
            print("Press 7 - To Cancel Fast Food")
            print("Press 8 - To Cancel Additional Items")
            print("Press 9 - Exit")
            print("🥰"*40)
            ch=int(input("Enter the choice:"))
            if ch==1:
                if order1==[]:
                    print("No Items has been ordered from this section!!!")
                else:
                    for k in order1:
                        print(k,"    ",Starters[k][0])
                    h=int(input("Enter the serial no of item to be cancelled:"))
                    if h in order1:
                        order1.remove(h)
                        print("Item Cancelled Succesfully!!")
                    else:
                        print("Sorry!! Invalid Choice no such Item has been ordered.......")
            if ch==2:
                if order2==[]:
                    print("No Items has been ordered from this section!!!")
                else:
                    for k in order2:
                        print(k,"    ",Non_Veg_Starters[k][0])
                    h=int(input("Enter the serial no of item to be cancelled:"))
                    if h in order2:
                        order2.remove(h)
                        print("Item Cancelled Succesfully!!")
                    else:
                        print("Sorry!! Invalid Choice no such Item has been ordered.......")
            if ch==3:
                if order3==[]:
                    print("No Items has been ordered from this section!!!")
                else:
                    for k in order3:
                        print(k,"    ",Veg_Main_Course[k][0])
                    h=int(input("Enter the serial no of item to be cancelled:"))
                    if h in order3:
                        order3.remove(h)
                        print("Item Cancelled Succesfully!!")
                    else:
                        print("Sorry!! Invalid Choice no such Item has been ordered.......")
            if ch==4:
                if order4==[]:
                    print("No Items has been ordered from this section!!!")
                else:
                    for k in order4:
                        print(k,"    ",Non_Veg_Main_Course[k][0])
                    h=int(input("Enter the serial no of item to be cancelled:"))
                    if h in order4:
                        order4.remove(h)
                        print("Item Cancelled Succesfully!!")
                    else:
                        print("Sorry!! Invalid Choice no such Item has been ordered.......")
            if ch==5:
                if order5==[]:
                    print("No Items has been ordered from this section!!!")
                else:
                    for k in order5:
                        print(k,"    ",Deserts[k][0])
                    h=int(input("Enter the serial no of item to be cancelled:"))
                    if h in order5:
                        order5.remove(h)
                        print("Item Cancelled Succesfully!!")
                    else:
                        print("Sorry!! Invalid Choice no such Item has been ordered.......")
            if ch==6:
                if order6==[]:
                    print("No Items has been ordered from this section!!!")
                else:
                    for k in order6:
                        print(k,"    ",Beverage[k][0])
                    h=int(input("Enter the serial no of item to be cancelled:"))
                    if h in order6:
                        order6.remove(h)
                        print("Item Cancelled Succesfully!!")
                    else:
                        print("Sorry!! Invalid Choice no such Item has been ordered.......") 
            if ch==7:
                if order7==[]:
                    print("No Items has been ordered from this section!!!")
                else:
                    for k in order7:
                        print(k,"    ",fast_food[k][0])
                    h=int(input("Enter the serial no of item to be cancelled:"))
                    if h in order7:
                        order7.remove(h)
                        print("Item Cancelled Succesfully!!")
                    else:
                        print("Sorry!! Invalid Choice no such Item has been ordered.......")
            if ch==8:
                if order8==[]:
                    print("No Items has been ordered from this section!!!")
                else:
                    for k in order8:
                        print(k,"    ",Additional_Items[k][0])
                    h=int(input("Enter the serial no of item to be cancelled:"))
                    if h in order8:
                        order8.remove(h)
                        print("Item Cancelled Succesfully!!")
                    else:
                        print("Sorry!! Invalid Choice no such Item has been ordered.......")
            else:
                break

def Show_Orders(bill=0):
    print('❣️'*50)
    if order1!=[]:
        for a in order1:
            print(Starters[a][0],"    ",Starters[a][1])
            bill+=Starters[a][2]
    if order2!=[]:
        for b in order2:
            print(Non_Veg_Starters[b][0],"    ",Non_Veg_Starters[b][1])
            bill+=Non_Veg_Starters[b][2]
    if order3!=[]:
        for c in order3:
            print(Veg_Main_Course[c][0],"    ",Veg_Main_Course[c][1])
            bill+=Veg_Main_Course[c][2]
    if order4!=[]:
        for d in order4:
            print(Non_Veg_Main_Course[d][0],"    ",Non_Veg_Main_Course[d][1])
            bill+=Non_Veg_Main_Course[d][2]
    if order5!=[]:
        for e in order5:
            print(Deserts[e][0],"    ",Deserts[e][1])
            bill+=Deserts[e][2]
    if order6!=[]:
        for f in order6:
            print(Beverage[f][0],"    ",Beverage[f][1])
            bill+=Beverage[f][2]
    if order7!=[]:
        for g in order7:
            print(fast_food[g][0],"    ",fast_food[g][1])
            bill+=fast_food[g][2]
    if order8!=[]:
        for h in order8:
            print(Additional_Items[h][0],"    ",Additional_Items[h][1])
            bill+=Additional_Items[h][2]
    print('❣️'*50)
    t.sleep(2)
    print("Total amount:          ","₹",bill)
    print('❣️'*50)

def total_bill():
    bill=0
    if order1!=[]:
        for a in order1:
            bill+=Starters[a][2]
    if order2!=[]:
        for b in order2:
            bill+=Non_Veg_Starters[b][2]
    if order3!=[]:
        for c in order3:
            bill+=Veg_Main_Course[c][2]
    if order4!=[]:
        for d in order4:
            bill+=Non_Veg_Main_Course[d][2]
    if order5!=[]:
        for e in order5:
            bill+=Deserts[e][2]
    if order6!=[]:
        for f in order6:
            bill+=Beverage[f][2]
    if order7!=[]:
        for g in order7:
            bill+=fast_food[g][2]
    if order8!=[]:
        for h in order8:
            bill+=Additional_Items[h][2]
    return bill

def cid_generator():
    q='select max(CID) from cust'
    cr=mydb.cursor()
    cr.execute(q)
    res=cr.fetchone()
    if res==(None,):
        cid='E0001'
    else:
        for k in res:
            c=k
        num=str(int(c[1:5])+1)
        if len(num)==1:
            cid='E000'+str(num)
        if len(num)==2:
            cid='E00'+str(num)
        if len(num)==3:
            cid='E0'+str(num)
        if len(num)==4:
            cid='E'+str(num)
    mydb.commit()
    return cid

def Bill_printer():
    print("*"*20,end='')
    print("Bill",end='')
    print("*"*20)
    n=1
    print("🎆"*40)
    print("ITEMS"+"  "+"AMOUNT")
    if order1!=[]:
        for a in order1:
            print(Starters[a][0],"    ",Starters[a][1])
    if order2!=[]:
        for b in order2:
            print(Non_Veg_Starters[b][0],"    ",Non_Veg_Starters[b][1])
    if order3!=[]:
        for c in order3:
            print(Veg_Main_Course[c][0],"    ",Veg_Main_Course[c][1])
    if order4!=[]:
        for d in order4:
            print(Non_Veg_Main_Course[d][0],"    ",Non_Veg_Main_Course[d][1])
    if order5!=[]:
        for e in order5:
            print(Deserts[e][0],"    ",Deserts[e][1])
    if order6!=[]:
        for f in order6:
            print(Beverage[f][0],"    ",Beverage[f][1])
    if order7!=[]:
        for g in order7:
            print(fast_food[g][0],"    ",fast_food[g][1])
    if order8!=[]:
        for h in order8:
            print(Additional_Items[h][0],"    ",Additional_Items[h][1])
    print("🎆"*40)
    print("*"*50)
    print("Net amount:","     ",total_bill())
    print("*"*50)
    


def login_manager():
    uname=input("Enter the username:")
    password=input("Enter the password:")
    if uname=='ALmanager07' and password=='ALCODERS':
        return True
    else:
        return False

print('😍'*50)
print(" "*30,end='')
print("WELCOME TO AL RESTAURANT")
print('🥳'*50)
t.sleep(2)
print("Hello, Welcome to AL Restaurant Sir!!")
t.sleep(0.5)
print("Have Your Seat Please!!")
t.sleep(1)
print("Follow the Instructions to proceed......................")
print("😀"*40)
print("Press A - To login as Manager")
print("Press B - To login as Customer")
print("😀"*40)
t.sleep(0.5)
log1=input("Enter your choice:")
print("Please wait Loading...........................")
t.sleep(1)
if log1.lower()=='a':
    if login_manager()==True:
        print("Login Successful!!")
        t.sleep(1)
        print("🤗"*40)
        while True:
            print("Press 1 - To See the Details of Customer of a day")
            print("Press 2 - To See the Details of Customer of a month")
            print("Press 3 - To See the Details of Customer of a year")
            print("Press 4 - To See the Total collection of a day")
            print("Press 5 - To See the Total collection of a month")
            print("Press 6 - To See the Total collection of a year")
            print("Press 7 - To See the Details of a Customer via Name")
            print("Press 8 - To Exit")
            ch=int(input("Enter the choice:"))
            print("🤗"*40)
            if ch==1:
                while True:
                    date=input("Enter the Date whose total collection to be searched(YYYY-MM-DD):")
                    if len(date)==10:
                        if date[4]=='-' and date[7]=='-':
                            if int(date[0]+date[1]+date[2]+date[3])>=2022 and int(date[0]+date[1]+date[2]+date[3])<2050:
                                if date[5]+date[6]=='01' or date[5]+date[6]=='03' or date[5]+date[6]=='05' or date[5]+date[6]=='07' or date[5]+date[6]=='08' or date[5]+date[6]=='10' or date[5]+date[6]=='12':
                                    if int(date[8]+date[9])<32 and int(date[8]+date[9])>0:
                                        break
                                elif date[5]+date[6]=='04' or date[5]+date[6]=='06' or date[5]+date[6]=='09' or date[5]+date[6]=='11':
                                    if int(date[8]+date[9])<31 and int(date[8]+date[9])>0:
                                        break
                                elif date[5]+date[6]=='02':
                                    if int(date[5]+date[6])>0 or int(date[5]+date[6])<29:
                                        break
                    else:
                        print("Invalid date number or date format!!")
                val=(date,)
                q="select * from cust where date=%s"
                cr=mydb.cursor()
                cr.execute(q,val)
                res=cr.fetchall()
                myTable = PrettyTable(["Customer ID","Customer Name","Date ", "Bill","Review"])
                for sh in res:
                    myTable.add_row(sh)
                print("🤩"*40)
                print(myTable)
                print("🤩"*40)
                mydb.commit()
            elif ch==2:
                while True:
                    s_dt=input("Enter the Month to be searched(MM):")
                    if int(s_dt)>0 and int(s_dt)<13:
                        break
                    else:
                        print("Invalid Month!!")
                        print("Try Again")
                while True:
                    l_dt=input("Enter the Year to be searched(YYYY):")
                    if int(l_dt)>2021 and int(l_dt)<2050:
                        break
                    else:
                        print("Invalid Month!!")
                        print("Try Again")
                q="select * from cust where date>=%s and date<=%s"
                m=l_dt+"-"+s_dt+"-01"
                if s_dt=='01' or s_dt=='03' or s_dt=='05' or s_dt=='07' or s_dt=='08' or s_dt=='10' or s_dt=='12':
                    f=l_dt+"-"+s_dt+"-31"
                elif s_dt=='04' or s_dt=='06' or s_dt=='09' or s_dt=='11':
                    f=l_dt+"-"+s_dt+"-30"
                else:
                    if l_dt%100==0:
                        if l_dt%400==0:
                            f=l_dt+"-"+s_dt+"-29"
                        else:
                            f=l_dt+"-"+s_dt+"-28"
                    else:
                        if l_dt%4==0:
                            f=l_dt+"-"+s_dt+"-29"
                        else:
                            f=l_dt+"-"+s_dt+"-28"
                val=(m,f)
                cr=mydb.cursor()
                cr.execute(q,val)
                res=cr.fetchall()
                myTable = PrettyTable(["Customer ID","Customer Name","Date ", "Bill","Review"])
                for sh in res:
                    myTable.add_row(sh)
                print("🤩"*40)
                print(myTable)
                print("🤩"*40)
                mydb.commit()
            elif ch==3:
                while True:
                    y=input("Enter the year to be searched(YYYY):")
                    if int(y)>2021 and int(y)<2050:
                        break
                    else:
                        print("Invalid Month!!")
                        print("Try Again")
                q="select * from cust where date>=%s and date<=%s"
                m=y+"-01-01"
                f=y+"-12-31"
                val=(m,f)
                cr=mydb.cursor()
                cr.execute(q,val)
                res=cr.fetchall()
                myTable = PrettyTable(["Customer ID","Customer Name","Date ", "Bill","Review"])
                for sh in res:
                    myTable.add_row(sh)
                print("🤩"*40)
                print(myTable)
                print("🤩"*40)
                mydb.commit()
            elif ch==4:
                while True:
                    date=input("Enter the Date whose total collection to be searched(YYYY-MM-DD):")
                    if len(date)==10:
                        if date[4]=='-' and date[7]=='-':
                            if int(date[0]+date[1]+date[2]+date[3])>=2022 and int(date[0]+date[1]+date[2]+date[3])<2050:
                                if date[5]+date[6]=='01' or date[5]+date[6]=='03' or date[5]+date[6]=='05' or date[5]+date[6]=='07' or date[5]+date[6]=='08' or date[5]+date[6]=='10' or date[5]+date[6]=='12':
                                    if int(date[8]+date[9])<32 and int(date[8]+date[9])>0:
                                        break
                                elif date[5]+date[6]=='04' or date[5]+date[6]=='06' or date[5]+date[6]=='09' or date[5]+date[6]=='11':
                                    if int(date[8]+date[9])<31 and int(date[8]+date[9])>0:
                                        break
                                elif date[5]+date[6]=='02':
                                    if int(date[5]+date[6])>0 or int(date[5]+date[6])<29:
                                        break
                    else:
                        print("Invalid date number or date format!!")
                val=(date,)
                q="select sum(bill) from cust where date=%s"
                cr=mydb.cursor()
                cr.execute(q,val)
                res=cr.fetchone()
                print("🤗"*40)
                print("The total collection of ",date," is:")
                for sh in res:
                    print(sh)
                print("🤗"*40)
                mydb.commit()
            elif ch==5:
                while True:
                    s_dt=input("Enter the Month to be searched(MM):")
                    if int(s_dt)>0 and int(s_dt)<13:
                        break
                    else:
                        print("Invalid Month!!")
                        print("Try Again")
                while True:
                    l_dt=input("Enter the Year to be searched(YYYY):")
                    if int(l_dt)>2021 and int(l_dt)<2050:
                        break
                    else:
                        print("Invalid Month!!")
                        print("Try Again")
                q="select sum(bill) from cust where date>=%s and date<=%s"
                m=l_dt+"-"+s_dt+"-01"
                if s_dt=='01' or s_dt=='03' or s_dt=='05' or s_dt=='07' or s_dt=='08' or s_dt=='10' or s_dt=='12':
                    f=l_dt+"-"+s_dt+"-31"
                elif s_dt=='04' or s_dt=='06' or s_dt=='09' or s_dt=='11':
                    f=l_dt+"-"+s_dt+"-30"
                else:
                    if l_dt%100==0:
                        if l_dt%400==0:
                            f=l_dt+"-"+s_dt+"-29"
                        else:
                            f=l_dt+"-"+s_dt+"-28"
                    else:
                        if l_dt%4==0:
                            f=l_dt+"-"+s_dt+"-29"
                        else:
                            f=l_dt+"-"+s_dt+"-28"
                val=(m,f)
                cr=mydb.cursor()
                cr.execute(q,val)
                res=cr.fetchone()
                print("🤗"*40)
                print("The total collection of ",s_dt,"month",l_dt,"year is:")
                for sh in res:
                    print(sh)
                mydb.commit()
                print("🤗"*40)
            elif ch==6:
                while True:
                    y=input("Enter the year to be searched(YYYY):")
                    if int(y)>2021 and int(y)<2050:
                        break
                    else:
                        print("Invalid Month!!")
                        print("Try Again")
                q="select sum(bill) from cust where date>=%s and date<=%s"
                m=y+"-01-01"
                f=y+"-12-31"
                val=(m,f)
                cr=mydb.cursor()
                cr.execute(q,val)
                res=cr.fetchone()
                print("🤗"*40)
                print("The total collection of ",y,"year is:")
                for sh in res:
                    print(sh)
                mydb.commit()
                print("🤗"*40)
            elif ch==7:
                n=input("Enter the name of the Customer:")
                a='select * from cust where C_Name=%s'
                val=(n,)
                cr=mydb.cursor()
                cr.execute(a,val)
                res=cr.fetchall()
                myTable = PrettyTable(["Customer ID","Customer Name","Date ", "Bill","Review"])
                for sh in res:
                    myTable.add_row(sh)
                print("🤩"*40)
                print(myTable)
                print("🤩"*40)
                mydb.commit()

            else:
                break
            
    else:
        print("Invalid Username or password!!")

if log1.lower()=='b':
    name=input("Please tell you Good Name Sir/Maam:")
    print("Hello ",name,"!!")
    while True:
        print("Please enter today's date in given format only!!")
        date=input("Enter Today's date(YYYY-MM-DD):")
        if len(date)==10:
            if date[4]=='-' and date[7]=='-':
                if int(date[0]+date[1]+date[2]+date[3])>=2022 and int(date[0]+date[1]+date[2]+date[3])<2050:
                    if date[5]+date[6]=='01' or date[5]+date[6]=='03' or date[5]+date[6]=='05' or date[5]+date[6]=='07' or date[5]+date[6]=='08' or date[5]+date[6]=='10' or date[5]+date[6]=='12':
                        if int(date[8]+date[9])<32 and int(date[8]+date[9])>0:
                            break
                    elif date[5]+date[6]=='04' or date[5]+date[6]=='06' or date[5]+date[6]=='09' or date[5]+date[6]=='11':
                        if int(date[8]+date[9])<31 and int(date[8]+date[9])>0:
                            break
                    elif date[5]+date[6]=='02':
                        if int(date[5]+date[6])>0 or int(date[5]+date[6])<29:
                            break 
        else:
            print("Please Write Date in given format only!!")
    t.sleep(1)
    while True:
        print("✨"*40)
        print("Press 1 - To Order")
        print("Press 2 - To See Orders")
        print("Press 3 - To Cancel Order")
        print("Press 4 - To Exit")
        print("✨"*40)
        t.sleep(2)
        ch=int(input("Enter the choice to proceed:"))
        t.sleep(1)
        if ch==1:
            order()
        elif ch==3:
            cancel_order()
        elif ch==2:
            Show_Orders()
        elif ch==4:
            Bill_printer()
            while True:
                review=input("Please give Feedback Sir/Maam(Not more than 50 words):")
                if len(review)<=50:
                    break
                else:
                    print("Sir/Maam... Please give review in not more than 50 Words!!")
            cid=cid_generator()
            tot=total_bill()
            val=(cid,name,date,tot,review)
            q="insert into cust values(%s,%s,%s,%s,%s)"
            cr=mydb.cursor()
            cr.execute(q,val)
            mydb.commit()
            t.sleep(0.5)
            print("Thank You!!")
            print("Hope you enjoyed the meal!!")
            print("Visit Again!!")
            print("✨"*40)
            break 
        else:
            True
else:
    print("Invalid Choice!!")
