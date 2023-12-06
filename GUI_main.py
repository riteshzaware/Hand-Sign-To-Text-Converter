import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="#FFD700")
root.geometry("300x200")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Intelligent Travelling Assistant Chatbot")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('s1.jpg')
image2 = image2.resize((900,600), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=350, y=0)  # , relwidth=1, relheight=1)


#
label_l2 = tk.Label(root, text="Sign Language Recognition System",font=("times", 30, 'bold','italic'),
                    background="#FFD700", fg="white", width=70, height=2)
label_l2.place(x=0, y=0)

#logo


    
def window():
  root.destroy()
  
  
def log():
    from subprocess import call
    call(["python","login.py"])
  
def register():
    from subprocess import call
    call(["python","register.py"])
    
    
    

    
button1 = tk.Button(root, text="LOGIN", command=log, width=12, height=3,font=('times 15 bold italic '),bd=6, bg="#8B6914", fg="white")
button1.place(x=530, y=650)

button2 = tk.Button(root, text="REGISTER",command=register,width=12, height=3,font=('times 15 bold italic'), bd=6,bg="#8B6914", fg="white")
button2.place(x=720, y=650)

button4 = tk.Button(root, text="EXIT", command=window, width=12, height=3,font=('times 15 bold italic'),bd=6,bg="red", fg="white")
button4.place(x=920, y=650)




label_l1 = tk.Label(root, text="** Intelligent Travelling Chatbot System @ 2023 by _____ **",font=("Times New Roman",10, 'bold'),
                    background="#EEC900", fg="white", width=250, height=2)
label_l1.place(x=0, y=798)



root.mainloop()