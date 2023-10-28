import tkinter
from tkinter import *
from tkinter import ttk, font, messagebox
import pymysql as mysql
import tk as tk



#Admin Login Check
def adminLogin(id,pin,win):
    connection = mysql.connect(host="localhost",user="root",password="livewire",database="student")
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (id, pin))
    user = cursor.fetchone()
    connection.close()
    if user:
        admin1(win)
    else:
        messagebox.showerror( "Incorrect", "Invalid UserId and Password")

def customerLogin(id,pin,win):
    connection = mysql.connect(host="localhost",user="root",password="livewire",database="student")
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM stud1 WHERE email=%s AND telmobile=%s', (id, pin))
    user = cursor.fetchone()
    connection.close()
    if user:
        print(id)
        customerpage(id,win)
    else:
        messagebox.showerror( "Incorrect", "Invalid UserId and Password")


def insert(n1,n2,n3,n4,n5,n6,n7,n8,n9,n):
    import pymysql as mysql
    connection = mysql.connect(host="localhost",user="root",password="livewire",database="student")
    cursor=connection.cursor()
    s="insert into stud1(studentname,fathername,mothername,gender,dateofbirth,email,level1,department,telmobile,percentage) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    t=(n1,n2,n3,n4,n5,n6,n7,n8,n9,n)
    cursor.execute(s,t)
    s="insert into verify(email,verify) values(%s,%s)"
    t=(n6,n)
    cursor.execute(s,t)
    connection.commit()
    import sms
    sms.sms1(n1)
    messagebox.showinfo( "Success", "User Insert Successfully")


def balance(id):
    print(id)
    connection = mysql.connect(host="localhost",user="root",password="livewire",database="student")
    cursor=connection.cursor()
    cursor.execute('select verify from verify where email=%s', (id))
    u=cursor.fetchone()
    a=0
    for x in u:
        a=int(x)
    if(a>60):
        b=" You are selected \n your Marks is eligible to join our Academic,\ncome and join with us :( "
    else:
        b="You are not selected \n your Marks is not eligible to our Academic,\n don't worry BE HAPPY :)"
    import sms
    sms.sms2(id,b)
    return b







def customerpage(cid,win):
    win.destroy()
    win=Tk()
    win.geometry("1200x650")
    win.title("STUDENT REGISTRATION")
    frame=Frame(win,width=1500,height=50,bg="green")
    frame.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    x=Label(frame,text="STUDENT REGISTRATION",font=label_font)
    x.config(bg= "green", fg= "white")
    x.place(relx=0.35,rely=0.01)
    frame=Frame(win,width=500,height=300,bg="pink")
    frame.pack()
    frame.place(relx=0.3,rely=0.3)
    label_font=font.Font(weight="bold",family="Times New Roman",size=17)
    print(cid)
    x=Label(frame,text=balance(cid),font=label_font)
    x.place(relx=0.01,rely=0.1)
    x.config(bg= "pink")
    frame=Frame(win,width=1500,height=50,bg="green")
    frame.pack()
    frame.place(relx=0.0,rely=0.94)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text=" Copyright © 2023 SanriA ",font=label_font,bg="Red")
    x.config(bg= "blue", fg= "white")
    x.place(relx=0.35,rely=0.1)
    win.mainloop()





def customer(win):
    win.destroy()
    win=Tk()
    win.geometry("1200x650")
    win.title("STUDENT LOGIN")
    frame=Frame(win,width=1500,height=50,bg="green")
    frame.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    x=Label(frame,text="STUDENT REGISTRATION",font=label_font)
    x.config(bg= "green", fg= "white")
    x.place(relx=0.35,rely=0.01)
    frame=Frame(win,width=500,height=300,bg="pink")
    frame.pack()
    frame.place(relx=0.3,rely=0.3)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="STUDENT LOGIN",font=label_font)
    x.place(relx=0.35,rely=0.1)
    x.config(bg= "pink")
    label_font=font.Font(weight="bold",family="Times New Roman",size=17)
    a=Label(frame,text="Student Email :",font=label_font)
    a.place(relx=0.1,rely=0.4)
    a.config(bg= "pink")
    b=Label(frame,text="Mobile Number",font=label_font)
    b.place(relx=0.1,rely=0.55)
    b.config(bg= "pink")
    a1=Entry(frame)
    a1.place(relx=0.5,rely=0.42, width=200, height=25)
    b1=Entry(frame,show="*")
    b1.place(relx=0.5,rely=0.57, width=200, height=25)
    b5=Button(frame,text="Login",font=label_font,activebackground="indianred",command=lambda:customerLogin(a1.get(),b1.get(),win))
    b5.place(relx=0.3,rely=0.8)
    frame=Frame(win,width=1500,height=50,bg="green")
    frame.pack()
    frame.place(relx=0.0,rely=0.94)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text=" Copyright © 2023 SanriA ",font=label_font,bg="Red")
    x.config(bg= "blue", fg= "white")
    x.place(relx=0.35,rely=0.1)
    win.mainloop()
#Admin Login
def admin(win):
    win.destroy()
    win=Tk()
    win.geometry("1200x650")
    win.title("STUDENT REGISTRATION")
    frame=Frame(win,width=1500,height=50,bg="green")
    frame.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    x=Label(frame,text="STUDENT REGISTRATION",font=label_font)
    x.config(bg= "green", fg= "white")
    x.place(relx=0.3,rely=0.01)
    frame=Frame(win,width=500,height=300,bg="pink")
    frame.pack()
    frame.place(relx=0.3,rely=0.3)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="ADMIN LOGIN",font=label_font)
    x.place(relx=0.35,rely=0.1)
    x.config(bg= "pink")
    label_font=font.Font(weight="bold",family="Times New Roman",size=17)
    a=Label(frame,text="Admin number:",font=label_font)
    a.place(relx=0.1,rely=0.4)
    a.config(bg= "pink")
    b=Label(frame,text="Password:",font=label_font)
    b.place(relx=0.1,rely=0.55)
    b.config(bg= "pink")
    a1=Entry(frame)
    a1.place(relx=0.5,rely=0.42, width=200, height=25)
    b1=Entry(frame,show="*")
    b1.place(relx=0.5,rely=0.57, width=200, height=25)
    b5=Button(frame,text="Login",font=label_font,activebackground="indianred",command=lambda:adminLogin(a1.get(),b1.get(),win))
    b5.place(relx=0.3,rely=0.8)
    frame=Frame(win,width=1500,height=50,bg="green")
    frame.pack()
    frame.place(relx=0.0,rely=0.94)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text=" Copyright © 2023 SanriA ",font=label_font,bg="Red")
    x.config(bg= "blue", fg= "white")
    x.place(relx=0.35,rely=0.1)
    win.mainloop()






def reg1(win):
    win.destroy()
    a=Tk()
    a.geometry("1200x650")
    frame = Frame(a, width=1500, height=50, bg="hot pink")

    frame.grid(row=0,column=1)
    label_font = font.Font(weight="bold", family="Times New Roman", size=30)
    x = Label(frame, text="STUDENT REGISTRATION", font=label_font, bg="Red")
    x.config(bg="hot pink", fg="white")
    x.grid(row=1,column=5)
    label_font1 = font.Font(weight="bold", family="Times New Roman", size=30)
    label_font= font.Font(weight="bold", family="Times New Roman", size=15)

    m2=Label(a,text="Student Name :",font=label_font)
    m2.grid(row=1 , column=1)
    m3=Label(a,text="Father's Name :",font=label_font)
    m3.grid(row=2 , column=1)
    m4=Label(a,text="Mother's Name :",font=label_font)
    m4.grid(row=3 , column=1)
    m5=Label(a,text="Gender :",font=label_font)
    m5.grid(row=4 , column=1)
    m6=Label(a,text="Date Of Birth :",font=label_font)
    m6.grid(row=5 , column=1)
    m7=Label(a,text="E-Mail :",font=label_font)
    m7.grid(row=6 , column=1)
    m8=Label(a,text="Level :",font=label_font)
    m8.grid(row=7 , column=1)
    m9=Label(a,text="Department :",font=label_font)
    m9.grid(row=8 , column=1)
    m10=Label(a,text="Tel/Mobile :",font=label_font)
    m10.grid(row=9 , column=1)
    m=Label(a,text="Percentage :",font=label_font)
    m.grid(row=10 , column=1)

    n1= Entry(a,font=label_font)
    n1.grid(row=1 , column=2)
    n2= Entry(a,font=label_font)
    n2.grid(row=2 , column=2)
    n3= Entry(a,font=label_font)
    n3.grid(row=3 , column=2)
    n42=Entry(a,font=label_font)
    n42.grid(row=4 , column=2)
    n5= Entry(a,font=label_font)
    n5.grid(row=5 , column=2)
    n6= Entry(a,font=label_font)
    n6.grid(row=6 , column=2)
    n7= ttk.Combobox(a,values=["high School","Under Graduate","Post Graduate"],font=label_font)
    n7.grid(row=7 , column=2)
    n8= ttk.Combobox(a,values=["Secondary School","Bachelor's of Engineering","Master's of Engineering"],font=label_font)
    n8.grid(row=8 , column=2)
    n9= Entry(a,font=label_font)
    n9.grid(row=9 , column=2)
    n= Entry(a,font=label_font)
    n.grid(row=10 , column=2)
    n10=Button(a,text="save",activebackground="indianred",command=lambda :insert(n1.get(),n2.get(),n3.get(),n42.get(),n5.get(),n6.get(),n7.get(),n8.get(),n9.get(),n.get()),font=label_font)
    n10.grid(row=11 , column=2)
    a.mainloop()



def admin1(win):
    win.destroy()
    win = Tk()
    win.geometry("1200x650")
    win.title("STUDENT ADMISSION PORTAL")
    def show_data():
        import pymysql as mysql
        connection = mysql.connect(host="localhost", user="root", password="livewire", database="student")
        cursor = connection.cursor()
        cursor.execute('SELECT studentname,email,telmobile,percentage FROM stud1 WHERE  percentage>60')
        data = cursor.fetchall()
        connection.close()
        for item in tree.get_children():
                            tree.delete(item)
        for row in data:
            tree.insert("", "end", values=row)
    frame = Frame(win, width=1500, height=50, bg="blue")

    frame.pack()
    label_font = font.Font(weight="bold", family="Times New Roman", size=30)
    x = Label(frame, text="STUDENT ADMISSION PORTAL", font=label_font, bg="Red")
    x.config(bg="blue", fg="white")
    x.place(relx=0.35, rely=0.01)
    label_font = font.Font(weight="bold", family="Times New Roman", size=20)
    s = """An Application Letter for College Admission is a document that individuals 
    can use when they want to apply for a college program of their interest.."""
    l = Label(win, text=s, font=label_font)
    l.place(relx=0.2, rely=0.1)
    frame = Frame(win)
    frame.pack()
    frame.place(relx=0.2, rely=0.4)
    show = Button(frame, text="Show Data", command=show_data,activebackground="indianred")
    show.pack()
    tree = ttk.Treeview(frame, columns=("Name", "Mail-ID", "Phone Number", "Percentage"), show="headings")
    tree.heading("Name", text="Name")
    tree.heading("Mail-ID", text="Mail-ID")
    tree.heading("Phone Number", text="Phone Number")
    tree.heading("Percentage", text="Percentage")
    tree.pack()
    win.mainloop()






#HOME Page
"Home Page"
win=Tk()
win.geometry("1200x650")
win.title("Student Admission Portal")
frame=Frame(win,width=1500,height=50,bg="midnight blue")
frame.pack()
label_font=font.Font(weight="bold",family="Times New Roman",size=30)
x=Label(frame,text="STUDENT ADMISSION PORTAL",font=label_font,bg="Red")
x.config(bg= "navy blue", fg= "white")
x.place(relx=0.3,rely=0.01)
label_font=font.Font(weight="bold",family="Times New Roman",size=20)
s="""An admission letter, also known as an acceptance letter, 
is a formal document issued by an educationalinstitution, such as a college, university."""
l=Label(win,text=s,font=label_font)
l.place(relx=0.1,rely=0.1)
label_font=font.Font(weight="bold",family="Times New Roman",size=20)
b=Button(win,text="Admin Login",font=label_font,activebackground="indianred",command=lambda:admin(win))
b.place(relx=0.42,rely=0.3)
label_font=font.Font(weight="bold",family="Times New Roman",size=20)
q="""Do you have any queries about what you need to submit or the deadline? Contact the Admission 
Office at the College you applied to as soon as possible. Find College contact information.."""
l=Label(win,text=q,font=label_font)
l.place(relx=0.1,rely=0.4)
b=Button(win,text="Student Registration",font=label_font,activebackground="indianred",command=lambda:reg1(win))
b.place(relx=0.29,rely=0.6)
b=Button(win,text="Student Login",font=label_font,activebackground="indianred",command=lambda:customer(win))
b.place(relx=0.55,rely=0.6)


label_font=font.Font(weight="bold",family="Times New Roman",size=20)
q="""This is a required part of the application. Take your time writing your essay. 
Get feedback from your parents, a favorite teacher, or your school counselor.."""
l=Label(win,text=q,font=label_font)
l.place(relx=0.21,rely=0.7)
frame=Frame(win,width=1500,height=50,bg="midnight blue")
frame.pack()
frame.place(relx=0.0,rely=0.94)
label_font=font.Font(weight="bold",family="Times New Roman",size=20)
x=Label(frame,text="Copyright © 2023 SanriA ",font=label_font,bg="Red")
x.config(bg= "indigo", fg= "white")
x.place(relx=0.35,rely=0.1)
win.mainloop()





