#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
def register():
    SpecialChar = ['$','@','#','%']
    db = open('database.txt','r')
    Username = input("Create username: ")
    Password = input("Create password: ")
    Password1 = input("Confirm password: ")
    d = []
    f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    #print(data)
    
    if not re.search("@gmail.com$", Username):
        print("Invalid,restart")
        register()
    else:
        if Password != Password1:
            print("Password don't match,restart")
            register()
        elif (len(Password)<5 or len(Password)>16):
            print("length of Password should be greater than 5 and should be smaller than 16,restart")
            register()
        elif not any (char.isdigit() for char in Password):
            print("Password should have at least one digit,restart")
            register()
        elif not any(char.isupper() for char in Password):
            print("Password should have at least one uppercase letter,restart")
            register()
        elif not any(char.islower() for char in Password):
            print("Password should have at least one lowercase letter,restart")
            register()
        elif not any(char in SpecialChar for char in Password):
            print("Password should have at least one of the symbol $@#")
            register()
        #else:
            #print("Password seems fine")
        
        elif Username in d:
            print("username exists")
            register()
        else:
            db = open('database.txt','a')
            db.write(Username+", "+Password+"\n")
            print("Success!")

def access():
    db = open('database.txt','r')
    Username = input("Enter the username: ")
    Password = input("Enter the password: ")
    
    if not len(Username or Password)<1:
        d = []
        f = []
        for i in db:
            a,b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        
        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        print("Login Success")
                        print("Hi,", Username)
                    else:
                        print("Password or Username is incorrect")
                except:
                    print("Incorrect Password or Username")
            else:
                print("Username or Password dosen't Exist")
        except:
            print("Username or Password dosen't exist")
    else:
        print("Please Enter a value")

def ForgotPassword():
    Username = input("Enter the Username:")
    file1 = open('database.txt','r')
    flag = 0
    index = 0
    for line in file1:
        if Username in line:
            flag = 1
            break
    if flag == 0:
        print("Username doesn't Exist")
    else:
        print(line)
        
def home(option=None):
    option = input("Login | Signup | ForgotPassword:")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    elif option == "ForgotPassword":
        ForgotPassword()
    else:
        print("Please enter an option")
    
home()


# In[ ]:




