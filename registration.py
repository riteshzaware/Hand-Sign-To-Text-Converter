import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os
import cv2


window = tk.Tk()
w,h = window.winfo_screenwidth(),window.winfo_screenheight()
window.geometry("%dx%d+0+0"%(w,h))
window.title("REGISTRATION FORM")
window.configure(background="black")

Fullname = tk.StringVar()
#address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
#Phoneno = tk.IntVar()
#var = tk.IntVar()
#age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()

value = random.randint(1, 1000)
print(value)

# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
               "(Fullname TEXT, username TEXT, Email TEXT, password TEXT)")
db.commit()



def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fullname.get()
    #addr = address.get()
    un = username.get()
    email = Email.get()
   # mobile = Phoneno.get()
    #gender = var.get()
    #time = age.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM registration WHERE username = ?')
    c.execute(find_user, [(username.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    # elif (addr == ""):
    #     ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    # elif((len(str(mobile)))<10 or len(str((mobile)))>10):
    #     ms.showinfo("Message", "Please Enter 10 digit mobile number")
    # elif ((time > 100) or (time == 0)):
    #     ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
    # elif (var == False):
        # ms.showinfo("Message", "Please Enter gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO registration(Fullname, username, Email,  password) VALUES(?,?,?,?)',
                (fname,  un, email,  pwd))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            
            # window.destroy()
            window.destroy()
            
            from subprocess import call
            call(["python", "login.py"])
#####################################################################################################################################################




# assign and define variable
# def login():

# #####For background Image
image2 =Image.open('s3.jpg')
image2 =image2.resize((w,800), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)





frame = tk.LabelFrame(window, text="", width=370, height=579, bd=4, font=('times', 14, ' bold '),bg="white")
frame.grid(row=0, column=0, sticky='nw')
frame.place(x=80, y=88)



lbl = tk.Label(window, text="Register Your Account", font=('times', 20,' bold '), height=1, width=18,bg="skyblue",fg="black")
lbl.place(x=120, y=35)



#l1 = tk.Label(window, text="Registration Form", font=("Times new roman", 30, "bold"), bg="blue4", fg="red")
#l1.place(x=490, y=40)

# that is for label1 registration

l2 = tk.Label(frame, text="Name", width=4, font=("Times new roman", 15, "bold"), bg="white",bd=5, fg="black")
l2.place(x=25, y=5)
t1 = tk.Entry(frame, textvar=Fullname, width=26, font=('', 15),bd=4, bg="white")
t1.place(x=26, y=35)
# that is for label 2 (full name)


l4 = tk.Label(frame, text="Username", width=7, font=("Times new roman", 15, "bold"), bg="white")
l4.place(x=25, y=95)
t3 = tk.Entry(frame, textvar=username, width=26, font=('', 15),bd=4,  bg="white")
t3.place(x=26, y=125)



l5 = tk.Label(frame, text="E-mail", width=5, font=("Times new roman", 15, "bold"), bg="white")
l5.place(x=23, y=185)
t4 = tk.Entry(frame, textvar=Email, width=26, font=('', 15),bd=4, bg="white")
t4.place(x=26, y=215)


l9 = tk.Label(frame, text="Password", width=7, font=("Times new roman", 15, "bold"), bg="white")
l9.place(x=24, y=275)
t9 = tk.Entry(frame, textvar=password, width=26, font=('', 15), show="*",bd=4,  bg="white")
t9.place(x=26, y=305)


l10 = tk.Label(frame, text="Confirm Password", width=13, font=("Times new roman", 15, "bold"), bg="white")
l10.place(x=26, y=365)
t10 = tk.Entry(frame, textvar=password1, width=26, font=('', 15), show="*",bd=4,  bg="white")
t10.place(x=26, y=395)
# l3 = tk.Label(frame, text="Address :", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2",bd=5)
# l3.place(x=30, y=80)
# t2 = tk.Entry(frame, textvar=address, width=20, font=('', 15),bd=5)
# t2.place(x=230, y=80)
# that is for label 3(address)


# that is for label 4(blood group)


# that is for email address

# l6 = tk.Label(frame, text="Phone number :", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2")
# l6.place(x=30, y=180)
# t5 = tk.Entry(frame, textvar=Phoneno, width=20, font=('', 15),bd=5)
# t5.place(x=230, y=180)
# phone number
# l7 = tk.Label(frame, text="Gender :", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2")
# l7.place(x=30, y=230)
# # gender
# tk.Radiobutton(frame, text="Male", padx=5, width=5, bg="antiquewhite2", font=("bold", 15), variable=var, value=1).place(x=230,
#                                                                                                                 y=230)
# tk.Radiobutton(frame, text="Female", padx=20, width=4, bg="antiquewhite2", font=("bold", 15), variable=var, value=2).place(
#     x=340, y=230)

# l8 = tk.Label(frame, text="Age :", width=12, font=("Times new roman", 15, "bold"), bg="antiquewhite2")
# l8.place(x=30, y=280)
# t6 = tk.Entry(frame, textvar=age, width=20, font=('', 15),bd=5)
# t6.place(x=230, y=280)


def log():
    from subprocess import call
    call(["python","login.py"])
    window.destroy()


btn = tk.Button(frame, text="Sign up", bg="green",font=("times",17),fg="white", width=22,bd=3,  command=insert)
btn.place(x=25, y=455)



l10 = tk.Label(frame, text="Already have an account?", width=20, font=("Times new roman", 13), bg="white")
l10.place(x=35, y=525)


btn = tk.Button(frame, text="Sign in.", bg="white",font=('times 15 bold underline'),fg="blue", bd=0, command=log)
btn.place(x=218, y=518)

# btn = tk.Button(frame, text="Sign in", bg="white",font=("",17),fg="blue", width=22,bd=3,  command=insert)
# btn.place(x=150, y=525)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)

window.mainloop()