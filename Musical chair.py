import pyttsx3
import random
import time as tm
k=pyttsx3.init()

print(".............................................WELCOME TO THE WORLD OF FUN...............................................")
k.say("WELCOME TO THE WORLD OF FUN")
k.runAndWait()
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!LET'S PLAY MUSICAL CHAIR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
k.say("LET'S PLAY MUSICAL CHAIR")
k.runAndWait()
k.say("Enter the names of Players as tuple of strings")
k.runAndWait()
t=eval(input("Enter the players:"))
names=list(t)


Once=0
while Once==0:
    k.say("Are you all Ready")
    k.say("We are going to Start with the game in Three second")
    tm.sleep(1)
    k.say("Three")
    k.say("Two")
    k.say("One")
    k.say("Go")
    k.runAndWait()
    Once=1

for i in range(len(names),0,-1):
    if len(names)==1:
        tm.sleep(5)
        print("\n","*"*30)
        k.say("Horray The Winner is")
        print("Winner is ", names[0])
        print("*"*30)
        k.say(names[0])
        k.runAndWait()
        
    else:
        tm.sleep(2)
        el = random.choice(names)
        print("-" * 30)
        k.say("The Player Eliminated is")
        print(el," is eliminated at postion",i)
        print("-" * 30)
        k.say(el)
        k.say('You are out of the game')
        k.runAndWait()
        names.remove(el)
