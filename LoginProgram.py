#   Author : Jamal Hamid
#   DOB    : 24/10/2005
#   Purpose of this program is a simple login/Resigtering program
#   Programing language:	Python

#Librarys
from ast import Try, While
from ntpath import join
from posixpath import split
import string
import random
from this import d
import os
from time import sleep

#   Dashboard to allow you to select the Login or Registering function
def dashboard():
	print("Welcome to your dashboard")

#   password_generator_options fuction
def password_generator_options(Username):
    while True:
    #   Picking password character options
        print("Your options are :")
        print("Letters | Numbers | Symbols")
        print("Example format needed to process is")
        print("Letters Numbers Symbols")
        option = input("Select your options : ")
        if option == ("Letters Numbers Symbols" or "Numbers Symbols Letters" or "Numbers Letters Symbols" or "Numbers Letters Symbols" or "Letters Numbers Symbols" or "Letters Symbols Numbers" or "Symbols Letters Numbers" or "Letters  Symbols Numbers" or "Letters Numbers Symbols"):
            characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        elif option == ("Letters Numbers" or "Numbers Letters"):
            characters = list(string.ascii_letters + string.digits)
        elif option == ("Letters"):
            characters = list(string.ascii_letters)
        elif option == ("Symbols"):
            characters = list("!@#$%^&*()")
        elif option == ("Numbers Symbols" or "Symbols Numbers"):
            characters = list(string.digits + "!@#$%^&*()")
        elif option == ("Numbers"):
            characters = list(string.digits)
        elif option == ("Letters Symbols" or "Symbols Letters"):
            characters = list(string.ascii_letters +"!@#$%^&*()")
        elif option == (""):
            print("You need to choose at least one option")
            sleep(2)
            password_generator_options(Username)
        else:
            print("Please enter a valid parameter, this is case-sensitive")
            sleep(2)
            password_generator_options(Username)
        
        print("Do you want to choose the password lenght : ")
        option = input("Yes | No : ")
        if option == "Yes":
    #   Checking that the password lenght value is >= 10 
            length = int(input("Enter password length : "))
            if length >= 10:
                generate_random_password(Username, characters, length)
                break
            else:
                print("Must be a number equal to or greater then 10")
        elif option == "No":
            length = 10
            generate_random_password(Username, characters, length)
            break
        else:
            print("Please enter a valid parameter, this is case-sensitive")
            sleep(2)
            password_generator_options(Username)

#   Password generating function
def generate_random_password(Username, characters, length):
    while True:
        random.shuffle(characters)     
    #   Picking random characters from the list
        Password = []
        for i in range(length):
            Password.append(random.choice(characters))
    #   Shuffling the resultant password
        random.shuffle(Password)
    #   Printing the list
        print("".join(Password))
    #   Converting the list to string
        Password = "".join(Password)
    #   Writing to file
        db_1 = open("accounts.txt", "a")
        db_1.write("\n"+Username+" "+Password)
        db_1.close 		                 
        print("Success!")
        break

def no_password_generator(Username):
    while True:
        try:
            Password = input("Create password : ")
            Password1 = input("Confirm password : ")    
            #   Verifying that the passwords matches
            if Password != Password1:
                print("Password dont match up, restert")
                no_password_generator(Username)
        #   Verifying that the password meets the minuim password lenght
            else:
                if len(Password) < 10:
                    print("Password is too short, restart")
                    no_password_generator(Username)
        #   Writing the login information to the database
                else:
                #   Writing to file
                    print(Username+" "+Password)                  
                    db_1 = open("accounts.txt", "a")
                    db_1.write("\n"+Username+" "+Password)
                    db_1.close
                    print("Success!")
                    break
        except: (ValueError)

#   Login function
def login():
#   Entering in the credential that you want verified
    Username = input("Enter your username : ")
    Password = input("Enter your Password : ")
    success = False
#   Slipting the txt file into usernames and passwords
    file = open("accounts.txt","r")
    for i in file:
        a,b = i.split(" ")
        a = a.strip()
        b = b.strip()
    if(a==Username and b==Password):
        #   Closing file
        file.close()
        success = True
    elif (Username=="Admin" and Password=="Admin"):
        print("Login Successful")
        admin()

#   Successful login
    if(success):
        print("Login Successful")
        print("You are not admin, so cannot view accounts")
    else:
        print("Details does not match")
        sleep(1.5)

#   Admin fuction
def admin():
    print("View accounts ")
    x= input("Yes | No : ")
#   Print database
    if x == "Yes":
        file = open("accounts.txt","r")
        for i in file:
            i.split(" ")
            print(i)
        sleep(30)
#   Redirect you to the home dashboard    
    elif x == "No":
        home()
    else:
        print("Please enter a valid parameter, this is case-sensitive")

#   Registion menu selection
def register():
    file = open("accounts.txt","r")
    d = []
    for i in file:
        a,b = i.split(" ")
        a = a.strip()
        b = b.strip()
        d.append(a)
    Username = input("Enter your username : ")
    if(Username == a):
        print("Username exists")
        sleep(2)
        register()
    else:
        print("Would you like to generator a password")
        print("Please select an option")
        option = input("Yes | No : ")
        if option == "Yes":
                password_generator_options(Username)
        elif option == "No":
                no_password_generator(Username)
        else:
                print("Please enter a valid parameter, this is case-sensitive")
                sleep(2)

# Home dashboard
def home():
    while True:
        sleep(2)
    #   Clearing the terminal
        os.system('clear')
    #   Selection menu
        dashboard()
        print("Please select an option")
        option = input("Login | Resigter | Exit : ")
        if option == "Login":
            login()
        elif option == "Resigter":
            register()
        elif option == "Exit":
            sleep(2)
            break
        else:
            print("Please enter a valid parameter, this is case-sensitive")

home()