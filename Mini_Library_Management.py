import time as t
def login():
    print("-"*30)
    print("\t LOGIN SCREEN ")
    print("-" * 30)
    username = input("Enter User Name : ")
    password = input("Enter Passwod   : ")

    if username == "lucky" and password == "python":
        return True
    else:
        return False

if login() == True:
    print("Please wait Loading........................")
    t.sleep(4)
    books = {}
    Lib=['Gulliver\'s Travels','The Wizard Of Oz','Harry Potter','Panchtantras','Mahabharta','Ramayana','Swami Vivekanada','2 States',
    'Girl in Room 105','Half Girlfriend','One Arranged Murder','400 Days','The 3 Mistakes of My Life','Gitanjali','The Blue Umbrella',
    'Wings Of Fire','Hamlet','Discovery of India','Fortynine Days','Godaan','Nirmala','Madhusala','White Tiger','The Inheritance of Loss',
    'Karna\'s Wife','Raavan','Devdas','Snow White','Cinderella','Alice in Wonderland','The jungle Book','Peter Pan','Sleeping Beauty',
    'Pinocchio','Susanna\'s seven Husbands','The Last Leaf','The midnight Library','Dream Town']
    while True:
        print("-" * 30)
        print("\nLibrary Management System")
        print("-" * 30)
        t.sleep(2)
        t.sleep(2)
        print("The BOOKS PRESENT IN LIBRARY:")
        t.sleep(1)
        print(Lib)
        print("-"*30)
        t.sleep(3)
        print("Press 1 - Issue a Book")
        print("Press 2 - Return a Book ")
        print("Press 3 - Display Issued Books")
        print("Press 4 - Exit ")
        print("-"*30)
        t.sleep(2)
        n = int(input("Enter your choice : "))
        print("Please wait Loading......................................")
        t.sleep(2)
        if n==1:
            print("!!!ATTENTIONS!!!")
            print("!!BE CAREFUL OF UPPER AND LOWER CASE!!")
            print('.'*50)
            t.sleep(5)
            title = input("Enter title of the book : ")
            member = input("Enter name of the borrower : ")
            doi = input("Enter issue date : ")
            if title in Lib:
                books[title] = [member,doi]
                Lib.remove(title)
                print("!!Book Issued Successfully!!")
            else:
                print("!!Sorry",title,"is not available in Library!!")
        elif n==3:
            print(books)
        elif n==2:
            print("!!!ATTENTIONS!!!")
            print("!!BE CAREFUL OF UPPER AND LOWER CASE!!")
            print('.'*50)
            t.sleep(5)
            v=input("Enter title of the book:")
            if v in books.keys():
                Lib.append(v)
                books.pop(v)
                print("!!Book Return Successful!!")
            else:
                print(v,"is not issued from the library!!")
        else:
            print("!!Thank You!!")
            print("!!Visit Again!!")
            break
        t.sleep(3)
else:
    print("-" * 30)
    print("\tInvalid username or password")
    print("-" * 30)
    
