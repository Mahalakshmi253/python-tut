from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import re
import mysql.connector as sql
import random,sys,os
from tkinter.ttk import Separator,Progressbar
from tkinter.messagebox import showinfo
#creating main page and frame
def login():
    root1.destroy()
    global root7
    root7=Tk()
    root7.title("Login System")
    root7.geometry('1350x700')
    bg_img=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\pic.jpg")
    user_img7=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\user.jpg")
    usericon_img7=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\user.png")
    passicon_img7=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\password.png")
    login_img7=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\login.png")
    register_img7=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\register.jpg")
    bglbl=Label(root7,image=bg_img).pack()
    #variables
    uname=StringVar()
    pname=StringVar()
    #creating title
    titlelbl=Label(root7,text="Login Page",fg="black",bg="blue",font=("cooper",26,"bold"),bd=10,relief="groove")
    titlelbl.place(x=0,y=0,relwidth=1)
    #creating
    l_frame=Frame(root7,bg="navy blue")
    l_frame.place(x=550,y=150)
    l_label=Label(l_frame,image=user_img7).grid(row=0,column=1,pady=20)
    #creating username and password label and entry
    user_name=Label(l_frame,text="Username",image=usericon_img7,fg="white",compound=LEFT,font=("times new roman",20,"bold"),highlightbackground="black",highlightthickness=7,bg="navy blue").grid(row=1,column=0)
    u_entry=Entry(l_frame,textvariable=uname,bg="white",fg="black",font=("",20)).grid(row=1,column=1,padx=20,pady=10)
    pass_lbl=Label(l_frame,text="Password",image=passicon_img7,fg="white",compound=LEFT,font=("times new roman",20,"bold"),highlightbackground="black",highlightthickness=7,bg="navy blue").grid(row=2,column=0)
    p_entry=Entry(l_frame,textvariable=pname,bg="white",fg="black",font=("",20),show="$").grid(row=2,column=1,padx=20,pady=10)
    #checking login connection
    def logincheck1():
        con=sql.connect(host="localhost",user="root",db="maha",password='mahaksankar')
        cur=con.cursor()
        cur.execute("select username,Password from users")
        try:
            for (i,v) in cur:
                if i==uname.get() and v==pname.get():
                    login=True
                    break
                else:
                    login=False
            if login==True:
                messagebox.showinfo("Login Sucessful","Login Sucessfully")
                welcome()
            elif login==False:
                messagebox.showerror("Login Unsucessful","Login Failed")
            else:
                cur.close()
                sql.close()
        except Exception as es:
                messagebox.showerror("error","error in registering")
    #creating login button
    #creating connection to check    
    btn7=Button(l_frame,text="Login",image=login_img7,compound=LEFT,font=("",15),bg="light green",fg="black",command=logincheck1)
    btn7.grid(row=3,column=1,padx=10,pady=10)
    root7.mainloop()    

def register():
    root.destroy()
    global root1
    root1=Tk()
    root1.title("registeration System")
    root1.geometry('1350x700+0+0')
    bg_img1=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\reg.jpg")
    bglbl1=Label(root1,image=bg_img1).pack()
    name1=StringVar()
    password1=StringVar()
    email1=StringVar()
    city=StringVar()
    age=StringVar()
    phoneno=StringVar()
    titlelbl1=Label(root1,text="Registeration Page",fg="black",bg="light blue",font=("cooper",26,"bold"),bd=10,relief="groove")
    titlelbl1.place(x=0,y=0,relwidth=1)
    l_frame1=Frame(root1,bg="navy blue")
    l_frame1.place(x=550,y=150)
    usericon_img1=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\user.png")
    passicon_img1=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\password.png")
    login_img1=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\login.png")
    email_img=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\email.png")
    city_img=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\city.png")
    register_img=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\register.jpg")
    age_img=ImageTk.PhotoImage(file='C:\\Users\\maha\\Downloads\\age.png')
    phone_img=ImageTk.PhotoImage(file='C:\\Users\\maha\\Downloads\\phone.png')
    user_name1=Label(l_frame1,text="Username",image=usericon_img1,compound=LEFT,font=("times new roman",20,"bold"),bg="navy blue",fg="white").grid(row=0,column=0)              
    username1=Entry(l_frame1,textvariable=name1,bg="white",fg='black',highlightbackground="black",highlightthickness=7,font=("",20)).grid(row=0,column=1,padx=20,pady=10)
    pass_name1=Label(l_frame1,text="Password",image=passicon_img1,compound=LEFT,font=("times new roman",20,"bold"),bg="navy blue",fg="white").grid(row=1,column=0)
    password2=Entry(l_frame1,textvariable=password1,bg="white",fg='black',highlightbackground="black",highlightthickness=7,font=("",20),show="$").grid(row=1,column=1,padx=20,pady=10)
    email_lbl=Label(l_frame1,text="Email Id",image=email_img,compound=LEFT,font=("times new roman",20,"bold"),bg="navy blue",fg="white").grid(row=2,column=0)
    email=Entry(l_frame1,textvariable=email1,bg="white",fg='black',highlightbackground="black",highlightthickness=7,font=("",20)).grid(row=2,column=1,padx=20,pady=10)
    city_name=Label(l_frame1,text="City Name",image=city_img,compound=LEFT,font=("times new roman",20,"bold"),bg="navy blue",fg="white").grid(row=3,column=0)              
    city1=Entry(l_frame1,textvariable=city,bg="white",fg='black',highlightbackground="black",highlightthickness=7,font=("",20)).grid(row=3,column=1,padx=20,pady=10)
    age_lbl=Label(l_frame1,text="User's Age",image=age_img,compound=LEFT,font=("times new roman",20,"bold"),bg="navy blue",fg="white").grid(row=4,column=0)              
    age1=Entry(l_frame1,textvariable=age,bg="white",fg='black',highlightbackground="black",highlightthickness=7,font=("",20)).grid(row=4,column=1,padx=20,pady=10)
    phone_lbl=Label(l_frame1,text="Phone No:",image=phone_img,compound=LEFT,font=("times new roman",20,"bold"),bg="navy blue",fg="white").grid(row=5,column=0)              
    phone1=Entry(l_frame1,textvariable=phoneno,bg="white",fg='black',highlightbackground="black",highlightthickness=7,font=("",20)).grid(row=5,column=1,padx=20,pady=10)        
    def registercheck():  
        u=name1.get()
        p=password1.get()
        e=email1.get()
        c=city.get()
        a=age.get()
        ph=phoneno.get()
        def isValidEmail(email):
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if(re.search(regex,email)):
                return True  
            else:  
                return False
        errorCount = 0
        if u=="" or p=="" or e=="" or c=="" or a=="" or ph=="":
            errorCount=errorCount+1
            messagebox.showerror("Fields Required","All Fields are required")
        if  a.isdigit()!=True or len(a)>=3 or a=='0' or a=='00':
            errorCount=errorCount+1
            messagebox.showerror("Fields Required","Enter valid Age")
        if   len(ph)!=10:
            errorCount=errorCount+1
            messagebox.showerror("Fields Required","Enter valid Phone Number")
        string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if(string_check.search(u) != None):
            errorCount=errorCount+1
            messagebox.showerror("Fields Required","Enter valid User Name")
        if(string_check.search(c) != None):
            errorCount=errorCount+1
            messagebox.showerror("Fields Required","Enter valid City")
        if  isValidEmail(e)!=True:
            errorCount=errorCount+1
            messagebox.showerror("Fields Required","Enter valid EmailId")            
        if errorCount==0:
            try:
                con=sql.connect(host="localhost",user="root",db="maha",password='mahaksankar')
                cur=con.cursor()
                query="INSERT INTO users (username,password,emailid,city,age,phoneno) VALUES (%s,%s,%s,%s,%s,%s)"
                val=(u,p,e,c,a,ph)
                cur.execute(query,val)
                con.commit()
                cur.close()
                con.close()
                messagebox.showinfo("Registeration Sucessfull","Your are registered sucessfully")
                login()            
            except Exception as ek:
                messagebox.showerror("error","error in registering")
                print(ek)
        else:
            messagebox.showerror("Fields Required","Please Re-Enter the Correct Inputs")
    btn3=Button(l_frame1,text="Login",image=login_img1,compound=LEFT,font=("",15),bg="light green",fg="black",command=login)
    btn3.grid(row=6,column=0,padx=10,pady=10)
    btn4=Button(l_frame1,text="Register",image=register_img,compound=LEFT,font=("",15),bg="light green",fg="black",command=registercheck)
    btn4.grid(row=6,column=1,padx=10,pady=10)
    root1.mainloop()
def welcome():
    root7.destroy()
    global root9
    root9 = Tk()
    root9.geometry("1500x800+0+0")
    root9.title("WELCOME")
    bg_img9=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\p2.jpeg")
    bglbl9=Label(root9,image=bg_img9).pack()
   
    button=Button(root9,text='START',font=("",25),bg="light green",fg="black",highlightbackground="black",highlightthickness=4,command=menu1)
    button.place(x=600,y=400)
    root9.mainloop()
def menu1():
    root9.destroy()
    global menu
    menu = Tk()
    menu_canvas = Canvas(menu,width=1300,height=950,bg="midnightblue")
    menu_canvas.pack()
    menu_frame = Frame(menu_canvas,bg="white")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    wel = Label(menu_canvas,text='WELCOME TO PYTHON TUTORIAL',fg="white",bg="midnightblue")
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)    
    level = Label(menu_frame,text='CHOOSE ANY LEVEL',bg="white",font="calibri 25",fg="darkviolet")
    level.place(relx=0.25,rely=0.3)    
    var = IntVar()
    easyR = Radiobutton(menu_frame,text='Easy',bg="white",fg="chocolate",font="calibri 20",value=1,variable = var)
    easyR.place(relx=0.25,rely=0.4)    
    mediumR = Radiobutton(menu_frame,text='Medium',bg="white",fg="forestgreen",font="calibri 20",value=2,variable = var)
    mediumR.place(relx=0.25,rely=0.5)    
    hardR = Radiobutton(menu_frame,text='Hard',bg="white",fg="orangered",font="calibri 20",value=3,variable = var)
    hardR.place(relx=0.25,rely=0.6)    
    def navigate():
       
        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            easy()
        elif x == 2:
            menu.destroy()
            medium()
       
        elif x == 3:
            menu.destroy()
            hard()
        else:
            pass
    letsgo = Button(menu_frame,text="Let's Go",bg="white",fg="dodgerblue",font="calibri 20",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)
def easy():    
    global root10
    root10=Tk()
    root10.geometry("1500x800+0+0")
    root10.title("EASY")
    bg_img10=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\data2bg.jpg")
    bglbl10=Label(root10,image=bg_img10).pack()
    t=Label(root10,text="Python was developed by Guido Van Rossum and has become very popular programming language among beginners",fg="black",font=("cooper",16,"bold"))
    t1=Label(root10,text="Data Types",fg="black",font=("cooper",20,"bold"))
    t2=Label(root10,text="mutability means in the same memory address a new value can be stored",fg="black",font=("cooper",16,"bold"))
    t3=Label(root10,text="mutuable data type can change its value in place",fg="black",font=("cooper",16,"bold"))
    t4=Label(root10,text="immutuable data type can never change its value in place",fg="black",font=("cooper",16,"bold"))
    dataimg=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\classification.jpeg")
    opimg=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\operator.jpeg")
    op=Label(root10,image=opimg)
    opi2mg=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\op2.jpeg")
    op2=Label(root10,image=opi2mg)
    data=Label(root10,image=dataimg)
    daeximg=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\mutimutjpeg.jpeg")
    data1=Label(root10,image=daeximg)
    t.place(x=50,y=0)
    t1.place(x=50,y=40)
    t2.place(x=50,y=100)
    t3.place(x=50,y=130)
    t4.place(x=50,y=160)
    op.place(x=100,y=400)
    op2.place(x=500,y=450)
    data.place(x=100,y=200)
    data1.place(x=500,y=200)
    easybtn=Button(root10,text='NEXT',padx=5,pady=5,width=5,bg="deepskyblue",font="15",fg="white",highlightbackground="black",highlightthickness=9,command=easy2)
    easybtn.place(x=800,y=600)
    root10.mainloop()
def easy2():
    root10.destroy()
    global root2
    root2=Tk()
    root2.geometry("1550x820+0+0")
    root2.title("EASY2")
    bg_img2=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\data2bg.jpg")
    bglbl2=Label(root2,image=bg_img2).pack()
    g1=Label(root2,text="SIMPLE INPUT AND OUTPUT",fg="black",font=("cooper",15,"bold"))
    g2=Label(root2,text="The input() function always returns a value",fg="black",font=("cooper",10,"bold"))
    g3=Label(root2,text="The print() function prints name or expression or value",fg="black",font=("cooper",10,"bold"))
    g4=Label(root2,text="CONDITIONAL STATEMENT",fg="black",font=("cooper",15,"bold"))
    g5=Label(root2,text="if-else STATEMENTS",fg="black",font=("cooper",10,"bold"))
    g6=Label(root2,text="'if' statement tests a particular condition and if the condition is true,it carries out statements indented below 'if'",fg="black",font=("cooper",10,"bold"))
    g7=Label(root2,text="and in case condition evaluates to false, it carries out statements indented below 'else'",fg="black",font=("cooper",10,"bold"))
    g8=Label(root2,text="NESTED IF STATEMENTS-A 'nested if'is an 'if' that has another 'if' in its 'if's body or in 'elif's body' or in its 'else's body'",fg="black",font=("cooper",10,"bold"))
    gimg=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\easy1.jpeg")
    gimg1=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\easy2.png")
    op=Label(root2,image=gimg)
    data=Label(root2,image=gimg1)
    g1.place(x=50,y=0)
    g2.place(x=50,y=35)
    g3.place(x=50,y=55)
    g4.place(x=50,y=400)
    g5.place(x=50,y=435)
    g6.place(x=50,y=455)
    g7.place(x=50,y=475)
    g8.place(x=50,y=495)
    op.place(x=50,y=90)
    data.place(x=570,y=90)
    easy2btn2=Button(root2,text='NEXT',bg="navy",fg="white",font="15",highlightbackground="black",highlightthickness=9,padx=5,pady=5,width=5,command=easy3)
    easy2btn2.place(x=200,y=550)
    root2.mainloop()
def easy3():
    root2.destroy()
    global root3
    root3=Tk()
    root3.geometry("1590x850+0+0")
    root3.title("EASY3")
    bg_img3=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\bgpy.jpg")
    bglbl3=Label(root3,image=bg_img3).pack()
    a1=Label(root3,text="TUPLE",fg="black",font=("cooper",10,"bold"))
    a3=Label(root3,text="",fg="black",font=("cooper",10,"bold"))
    a4=Label(root3,text="STRING METHODS",fg="black",font=("cooper",10,"bold"))
    a5=Label(root3,text="LIST-It contains values of mixed data types and is a mutable sequence of python",fg="black",font=("cooper",10,"bold"))
    aimg=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\string.png")
    aimg1=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\str.jpeg")
    aimg2=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\list.png")
    aimg3=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\lst1.jpeg")
    ai=Label(root3,image=aimg)
    ao=Label(root3,image=aimg1)
    ai1=Label(root3,image=aimg2)
    ai2=Label(root3,image=aimg3 )
    a1.place(x=50,y=0)
    a3.place(x=50,y=20)
    a4.place(x=50,y=40)
    a5.place(x=50,y=370)
    ao.place(x=50,y=90)
    ai.place(x=600,y=50)
    ai1.place(x=50,y=400)
    ai2.place(x=750,y=350)
    easy3btn3=Button(root3,text='BACK TO LEVEL',highlightbackground="black",font="15",highlightthickness=9,bg="darkturquoise",fg="black",padx=15,pady=15,width=10,command=menu2)
    easy3btn3.place(x=1100,y=550)
    root3.mainloop()    
def menu2():
    root3.destroy()
    global menus
    menus = Tk()
    menu_canvas1 = Canvas(menus,width=1300,height=950,bg="midnightblue")
    menu_canvas1.pack()
    menu_frame1 = Frame(menu_canvas1,bg="white")
    menu_frame1.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    wel1 = Label(menu_canvas1,text='WELCOME TO PYTHON TUTORIAL',fg="white",bg="midnightblue")
    wel1.config(font=('Broadway 22'))
    wel1.place(relx=0.1,rely=0.02)    
    level1 = Label(menu_frame1,text='CHOOSE ANY LEVEL',bg="white",font="calibri 25",fg="darkviolet")
    level1.place(relx=0.25,rely=0.3)    
    var1 = IntVar()
    easyR1 = Radiobutton(menu_frame1,text='Easy',bg="white",fg="chocolate",font="calibri 20",value=1,variable = var1)
    easyR1.place(relx=0.25,rely=0.4)    
    mediumR1 = Radiobutton(menu_frame1,text='Medium',bg="white",fg="forestgreen",font="calibri 20",value=2,variable = var1)
    mediumR1.place(relx=0.25,rely=0.5)    
    hardR1 = Radiobutton(menu_frame1,text='Hard',bg="white",fg="orangered",font="calibri 20",value=3,variable = var1)
    hardR1.place(relx=0.25,rely=0.6)    
    def navigate1():
        x = var1.get()
        print(x)
        if x == 1:
            menus.destroy()
            easy()
        elif x == 2:
            menus.destroy()
            medium()
        elif x == 3:
            menus.destroy()
            hard()
        else:
            pass
    letsgo1 = Button(menu_frame1,text="Let's Go",bg="white",fg="dodgerblue",font="calibri 20",command=navigate1)
    letsgo1.place(relx=0.25,rely=0.8)    
def medium():
    global root4
    root4=Tk()
    root4.geometry("1590x850+0+0")
    root4.title("MEDIUM")
    bg_img4=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\data2bg.jpg")
    bglbl4=Label(root4,image=bg_img4).pack()
    h1=Label(root4,text="LOOPING STATEMENTS",fg="black",font=("cooper",14,"bold"))
    h2=Label(root4,text="ITERATION-it allows a set of instructions to be performed repeatedly until a certain condition is fulfilled",fg="black",font=("cooper",10,"bold"))
    h3=Label(root4,text="FOR LOOP-it repeats certain no: of times(counting loop) and ends when the loop is repeated for last value of sequence",fg="black",font=("cooper",10,"bold"))
    h4=Label(root4,text="WHILE LOOP-it is conditional loop and repeats as long as condition remains true",fg="black",font=("cooper",10,"bold"))
    h5=Label(root4,text="The range() function returns sequence of list type in 'for loop'",fg="black",font=("cooper",10,"bold"))
    h6=Label(root4,text="LOOP-ELSE STATEMENTS-it executes when the loop terminates normally for the last sequence in 'for' loop and condition becomes false in 'while' loop",fg="black",font=("cooper",10,"bold"))
    h7=Label(root4,text="NESTED LOOP-loop which has another loop in its body and 'break' statement terminates the inner loop before outer loop",fg="black",font=("cooper",10,"bold"))
    himg=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\for.jpeg")
    himg1=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\while.png")
    himg2=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\nested.png")
    l=Label(root4,image=himg)
    lo=Label(root4,image=himg1)
    l2=Label(root4,image=himg2)
    h1.place(x=50,y=0)
    h2.place(x=50,y=35)
    h3.place(x=50,y=55)
    h4.place(x=50,y=400)
    h5.place(x=50,y=435)
    h6.place(x=50,y=455)
    h7.place(x=50,y=475)
    l2.place(x=50,y=495)
    l.place(x=50,y=90)
    lo.place(x=570,y=90)
    med3btn3=Button(root4,text='NEXT',padx=10,pady=10,width=10,font="15",bg="gold",fg="black",command=medium1,highlightbackground="black")
    med3btn3.place(x=700,y=550)
    root4.mainloop()
def medium1():
    root4.destroy()
    global root5
    root5=Tk()
    root5.geometry("1590x850+0+0")
    root5.title("medium")
    bg_img5=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\bgpy.jpg")
    bglbl5=Label(root5,image=bg_img5).pack()
    m1=Label(root5,text="TUPLE-Tuples are sequences and is a collection of objects which are ordered and immutable",fg="black",font=("cooper",10,"bold"))
    m3=Label(root5,text="TUPLE METHODS",fg="black",font=("cooper",10,"bold"))
    m4=Label(root5,text="DICTIONARY-it is an unordered collection of elements in the form of key values pairs used to store data values",fg="black",font=("cooper",10,"bold"))
    m5=Label(root5,text="DICTIONARY METHODS",fg="black",font=("cooper",10,"bold"))
    mimg=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\tuple methods1.jpg")
    mimg3=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\dict_operations1.jpg")
    mimg1=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\tuple 1.png")
    mimg2=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\dict.png")
    mi=Label(root5,image=mimg)
    mo=Label(root5,image=mimg1)
    mi1=Label(root5,image=mimg2)
    mi2=Label(root5,image=mimg3)
    m1.place(x=50,y=0)
    m3.place(x=50,y=20)
    m4.place(x=50,y=420)
    m5.place(x=50,y=450)
    mo.place(x=50,y=90)
    mi.place(x=700,y=150)
    mi1.place(x=50,y=500)
    mi2.place(x=750,y=450)
    med4btn4=Button(root5,text='BACK TO LEVEL',bg="mediumaquamarine",fg="black",highlightbackground="black",font="15",highlightthickness=9,padx=15,pady=15,width=10,command=menu3)
    med4btn4.place(x=700,y=350)
    root5.mainloop()
def menu3():
    root5.destroy()
    global menus1
    menus1 = Tk()
    menu_canvas2 = Canvas(menus1,width=1300,height=950,bg="midnightblue")
    menu_canvas2.pack()
    menu_frame2 = Frame(menu_canvas2,bg="white")
    menu_frame2.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    wel1 = Label(menu_canvas2,text='WELCOME TO PYTHON TUTORIAL',fg="white",bg="midnightblue")
    wel1.config(font=('Broadway 22'))
    wel1.place(relx=0.1,rely=0.02)    
    level1 = Label(menu_frame2,text='CHOOSE ANY LEVEL',bg="white",fg="darkviolet",font="calibri 25")
    level1.place(relx=0.25,rely=0.3)  
    var2= IntVar()
    easyR2 = Radiobutton(menu_frame2,text='Easy',bg="white",fg="chocolate",font="calibri 20",value=1,variable = var2)
    easyR2.place(relx=0.25,rely=0.4)    
    mediumR2 = Radiobutton(menu_frame2,text='Medium',bg="white",fg="forestgreen",font="calibri 20",value=2,variable = var2)
    mediumR2.place(relx=0.25,rely=0.5)    
    hardR2 = Radiobutton(menu_frame2,text='Hard',bg="white",fg="orangered",font="calibri 20",value=3,variable = var2)
    hardR2.place(relx=0.25,rely=0.6)    
    def navigate2():        
        x = var2.get()
        print(x)
        if x == 1:
            menus1.destroy()
            easy()
        elif x == 2:
            menus1.destroy()
            medium()        
        elif x == 3:
            menus1.destroy()
            hard()
        else:
            pass
    letsgo1 = Button(menu_frame2,text="Let's Go",bg="white",fg="dodgerblue",font="calibri 20",command=navigate2)
    letsgo1.place(relx=0.25,rely=0.8)
def hard():
    global root6
    root6=Tk()
    root6.geometry("1590x850+0+0")
    root6.title("HARD")
    bg_img6=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\bgpy.jpg")
    bglbl6=Label(root6,image=bg_img6).pack()
    m1=Label(root6,text="FUNCTIONS-function is a subprogram that acts on data and often returns a value",fg="black",font=("cooper",10,"bold"))
    m3=Label(root6,text="FUNCTION TYPES-1.bultin function 2.function defined in modules 3.user defined functions",fg="black",font=("cooper",10,"bold"))
    m4=Label(root6,text="PALINDROME-a word or sequence that reads the same backwards as forwards,e.g.madam",fg="black",font=("cooper",10,"bold"))
    mimg=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\func.jpg")
    mimg3=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\dctnary.png")
    mimg1=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\palindrome 1.png")
    mimg2=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\listjoin.png")
    mo=Label(root6,image=mimg)
    mi=Label(root6,image=mimg1)
    mi1=Label(root6,image=mimg2)
    mi2=Label(root6,image=mimg3)
    m1.place(x=50,y=0)
    m3.place(x=50,y=20)
    m4.place(x=50,y=400)
    mo.place(x=50,y=90)
    mi.place(x=700,y=90)
    mi1.place(x=50,y=435)
    mi2.place(x=750,y=450)
    
    root6.mainloop()    

def start():
    global root
    root = Tk()
    root.title("Python Tutorial")
    root.geometry('1350x700')
    bg_img6=ImageTk.PhotoImage(file="C:\\Users\\maha\\Downloads\\python tutorial.jpeg")
    bglbl6=Label(root,image=bg_img6).pack()
    btn6=Button(root,text="Start",font=("",15),bg="light green",fg="black",highlightbackground="black",highlightthickness=9,command=register)
    btn6.place(x=700,y=400)
    root.mainloop()
if __name__=="__main__":    
    start()    
