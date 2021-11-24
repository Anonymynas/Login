from tkinter import *
from tkinter import messagebox
import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB 

#Import dataset
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/SMS-Spam-Detection/master/spam.csv", encoding= 'latin-1')
data.head()
data = data[['class','message']]
#train dataset
x = np.array(data["message"])
y = np.array(data["class"])
cv = CountVectorizer()
X = cv.fit_transform(x) 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
clf = MultinomialNB()
clf.fit(X_train,y_train)

#display
#sample = input('Enter a message:')
#data = cv.transform([sample]).toarray()
#print(clf.predict(data))

######################################################################################################################################
#login GUI
def main_menu():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x500")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Admin", height="3", width="50", command = sadmin).pack()
    Label(text="").pack()
    Button(text="User", height="3", width="50", command=suser).pack()
 
    main_screen.mainloop()
 
#admin login screen
def sadmin():
    global admin_login_screen
    admin_login_screen = Toplevel(main_screen)
    admin_login_screen.title("Login")
    admin_login_screen.geometry("300x250")
    Label(admin_login_screen, text="Please enter details below to login").pack()
    Label(admin_login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(admin_login_screen, text="Username * ").pack()
    username_login_entry = Entry(admin_login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(admin_login_screen, text="").pack()
    Label(admin_login_screen, text="Password * ").pack()
    password_login_entry = Entry(admin_login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(admin_login_screen, text="").pack()
    Button(admin_login_screen, text="Login", width=10, height=1, command=admin_login_verify).pack()

#user login screen
def suser():
    global user_login_screen
    user_login_screen = Toplevel(main_screen)
    user_login_screen.title("Login")
    user_login_screen.geometry("300x250")
    Label(user_login_screen, text="Please enter details below to login").pack()
    Label(user_login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(user_login_screen, text="Username * ").pack()
    username_login_entry = Entry(user_login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(user_login_screen, text="").pack()
    Label(user_login_screen, text="Password * ").pack()
    password_login_entry = Entry(user_login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(user_login_screen, text="").pack()
    Button(user_login_screen, text="Login", width=10, height=1, command=user_login_verify).pack()

#verify admin password
def admin_login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    if(username1 == 'Admin' and password1 == '1234'):
        messagebox.showinfo("", "Login To Admin")
    else:
        messagebox.showinfo("", "Incorrect Username / Password ")
        
#verify user password
def user_login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    if(username1 == 'user' and password1 == '1234'):
        user_page()
    else:
        messagebox.showinfo("", "Incorrect Username / Password ")

#user page
def user_page():
    global user_page
    user_page = Toplevel(main_screen)
    user_page.title("SPAM DETECTION SYSTEM")
    user_page.geometry("700x700")
    Label(user_page, text="WELCOME TO", font="20",fg="black").pack()
    Label(user_page, text="SPAM DETECTION SYSTEM", font="20",fg="black").pack()
    

main_menu()
 