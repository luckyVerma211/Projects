print("!!!WELCOME TO THE WORLD OF GAME!!!")
print("!!!!!!!LETS's PLAY!!!!!!!")
print("!!!!STONE PAPER SCISSOR!!!!")
import random as r
p=["stone","scissor","paper"]
print("Enter 'st' for stone")
print("Enter 'pa' for paper")
print("Enter 'sc' for stone")
print("INVALID CHOICE WILL MAKE YOU LOSE")
m=input("Enter your name:")
ans='y'
com=0
pla=0
while ans=='y':
    n=r.randrange(0,3,1)
    c=p[n]
    a=input("Enter your Choice:")
    print("Computer choose:",c)
    if c=="stone" and a=="st":
        com+=1
        pla+=1
        print("!!SAME CHOICE!!")
    elif c=="paper" and a=="pa":
        com+=1
        pla+=1
        print("!!SAME CHOICE!!")
    elif c=="scissor" and a=="sc":
        com+=1
        pla+=1
        print("!!SAME CHOICE!!")
    elif c=="scissor" and a=="st":
        pla+=2
        print(m,"WON!!")
    elif c=="scissor" and a=="pa":
        com+=2
        print("!!Computer Won!!")
    elif c=="paper" and a=="sc":
        pla+=2
        print(m,"WON!!")
    elif c=="paper" and a=="st":
        com+=2
        print("!!Computer Won!!")
    elif c=="stone" and a=="pa":
        pla+=2
        print(m,"WON!!")
    elif c=="stone" and a=="sc":
        com+=2
        print("!!Computer Won!!")
    else:
        com+=2
        print("!!Computer Won!!")
    ans=input("Do You Want to play more?(Press 'y' to play more):")
print("The total points of computer is:",com)
print("The total points of player is:",pla)
if com>pla:
    print("!!!The winner is Computer!!!")
elif pla>com:
    print("!!!The Winner is",m,"!!!")
else:
    print("!!Both have equal points!!")

