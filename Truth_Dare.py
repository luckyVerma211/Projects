import random
dare=['Show the most embarrassing photo on your phone','Show the last five people you texted and what the messages said',
'Let the rest of the group DM someone from your Instagram account','Keep three ice cubes in your mouth until they melt','Say something dirty to the person on your left',
'Give a foot massage to the person on your right','Put 10 different available liquids into a cup and drink it',
'Remove four items of clothing','Seductively eat a banana','Empty out your wallet/purse and show everyone what is inside',
'Pretend to be the person to your right for 1 minutes',
'Eat a snack without using your hands','Say two honest things about everyone else in the group','Tell everyone an embarrassing story about yourself',
'Post the oldest selfie on your phone on Instagram Stories','Let someone else tickle you and try not to laugh','Put as many snacks into your mouth at once as you can',]
truth=['When was the last time you cried?','What is your biggest fear?','Whats i the worst thing you have ever done?','Have you ever cheated on someone?',
'Who was your first celebrity crush?','What is the most embarrassing thing you have ever done?','What is your biggest insecurity?',
'What is the biggest mistake you have ever made?','What is the most disgusting thing you have ever done?','Who would you like to kiss in this room?',
'What is the worst thing anyone has ever done to you?','What is the worst thing you have ever said to anyone?','Have you ever peed in the shower?',
'Where is the weirdest place you have had sex?',' What is the youngest age partner you had date?','Who in this room would you list as your emergency contact?',
'Who was your first love?','Have you ever farted in an elevator?','Have you ever had a one-night stand?','Who was the last person you said, “I love you” to?',
'What is the most bogus rumor you have ever heard about yourself?']
print("!!!!!!!!!!!!!!!!!!!!! !WELCOME! !!!!!!!!!!!!!!!!!!!!!!!!!")
print("!!!!!!!!!!!!!!!!!!Ready to play TRUTH $ DARE!!!!!!!!!!!!!!!!!!!!!!!")
l=eval(input("Enter the list of players:"))

ans='yes'
tn=len(truth)
dn=len(dare)
while ans=='yes':
    n=len(l)
    if n==1:
        print("THE WINNER IS:",l[0])
        print("!!!!CONGRATULATION!!!!")
        break
    else:
        a=random.randint(0,n-1)
        print("The player selected is:",l[a])
        print("Press t for truth!!")
        print('Press d for dare!!')
        wish=input("You want truth or dare:")
        if wish=='t':
            b=random.randint(0,tn-1)
            print("Your tell us that:",truth[b])
        elif wish=='d':
            c=random.randint(0,dn-1)
            print("Your dare is:",dare[c])
        else:
            print("Your are idiot!!!")
        l.remove(l[a])
        ans=input("Do you want to play more:")
print("Thanks for playing!!!")
print("***********SEE YOU SOON************")

