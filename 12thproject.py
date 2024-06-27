
'''
import turtle
from tkinter import *
import mysql.connector as mys
from tkinter import ttk


colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(25):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)


turtle.color('white')
style = ('Courier', 30, 'italic')
turtle.write('Welcome to Flight Management System', font=style, align='center')
turtle.hideturtle()




def menu():
    global root
    root=Tk()
    root.title("")

    txt=Label(root, text="Entry")
    txt.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    loginbtn=Button(root, text="Login",padx=90, pady=10, height=3, command= login)
    signinbtn=Button(root, text="Create an Acoount", padx=60, pady=10, height=3, command= signin) 
    loginbtn.grid(row=2, column=0)
    signinbtn.grid(row=2, column=1)
    root['background'] = 'RosyBrown1'
    root.geometry("700x600")

    canvas=Canvas(root, width=700,height=470,bg='RosyBrown1',highlightthickness=0)
    canvas.grid(row=1,column=0,columnspan=2)
    photo = PhotoImage(file = "airlines1.gif")
    canvas.create_image(20,20,anchor=NW, image=photo)
    mainloop()



def login():
  global root
  root.destroy()
  root=Tk()
  root.title("Login Window")


  txt=Label(root, text="Login")
  txt.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

  txt=Label(root, text="Enter Username")
  txt1=Label(root, text="Enter Password")

  global usrn
  global passw

  usrn=Entry(root, width=32, borderwidth=5)
  passw=Entry(root, width=32, borderwidth=5, show="*")

  logbtn=Button(root, text="Login", padx=130, pady=10,height=3, command= logpress)


  txt.grid(row=1, column=0)
  txt1.grid(row=2, column=0)
  usrn.grid(row=1, column=1)
  passw.grid(row=2, column=1)
  logbtn.grid(row=3, column=1)
  root['background'] = 'RosyBrown1'


def logpress():

  global susrn
  global spassw  

  susrn=usrn.get()
  spassw=passw.get()

  global root
  root.destroy()

  global lst
  
  lst=usrn_pass[susrn]
  
  if susrn in usrn_pass.keys():
      
    root=Tk()
    root.title("")
    root['background'] = 'RosyBrown1'
   
    if spassw==lst[1]:
        
      succ=Label(root, text="Login succesfull")
      cont=Button(root, text="Continue", width=50,height=3, command= acctype)

      succ.pack()
      cont.pack()
      
    else:

        fail=Label(root, text="Password entered incorrectly")
        fail.grid(row=0,column=0, columnspan=2, padx=5, pady=5)

        back=Button(root, text="Try Again", width=45,height=3, command= login)
        change=Button(root, text="Change password", width=45,height=3, command= cpass)

        back.grid(row=1, column=0)
        change.grid(row=1, column=1)
  else:

    root=Tk()
    root.title("Login failed")
    root['background'] = 'RosyBrown1'

    failtxt=Label(root, text="Username not registered", width=100)
    failtxt.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    backbtn=Button(root, text="Try Again", width=45,height=3, command= login)
    registerbtn=Button(root, text="Register", width=45,height=3, command= signin)

    backbtn.grid(row=1,column=0)
    registerbtn.grid(row=1,column=1)

def cpass():

  global root
  root.destroy()

  root=Tk()
  root.title("Change Password")
  root['background'] = 'RosyBrown1'


  txt=Label(root, text="Change password")
  txt.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

  txt=Label(root, text="Enter Username", width=20)
  txt2=Label(root, text="Enter Email", width=20)
  txt1=Label(root, text="Enter new Password", width=20)


  global usrn
  global mail
  global passw

  usrn=Entry(root, width=32, borderwidth=5)
  mail=Entry(root, width=32, borderwidth=5)
  passw=Entry(root, width=32, borderwidth=5, show="*")

  cbtn=Button(root, text="Change password", padx=130, pady=10,height=3, command=cpasscon)

  txt.grid(row=1, column=0)
  txt1.grid(row=2, column=0)
  usrn.grid(row=1, column=1)
  passw.grid(row=2, column=1)
  txt2.grid(row=3, column=0)
  mail.grid(row=3, column=1)
  cbtn.grid(row=4, column=1)
  
  





def cpasscon():

  fmail=mail.get()
  fpassw=passw.get()

  global root
  root.destroy()
  
  global lst
  global susrn
  
  if fmail==lst[0]:
    try:
        myconn=mys.connect(host='localhost',user='root',\
                                 passwd='adis',database='12project')
        mycur=myconn.cursor()
        mycur.execute("update logintable set passwd='{}' where usrname='{}';".format(fpassw,susrn))
        myconn.commit()
        logindict()
    except Exception as e:
        print(e)
    
    root=Tk()
    root.title("Success")
    root['background'] = 'RosyBrown1'

    succ=Label(text="Password changed successfully")
    cont=Button(root, text="Continue", width=50,height=3, command= login)

    succ.grid(row=0, column=0)
    cont.grid(row=1, column =0)

  else:
    root=Tk()
    root['background'] = 'RosyBrown1'
    root.title("Failed")

    failtxt=Label(root, text="Email entered incorrectly")
    failtxt.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    backbtn=Button(root, text="Try Again", width=45,height=3, command= cpass)
    registerbtn=Button(root, text="Register", width=45,height=3, command= signin)

    backbtn.grid(row=1,column=0)
    registerbtn.grid(row=1,column=1)




def signin():
  global root
  root.destroy()

  root=Tk()
  root.title("Register")
  root['background'] = 'RosyBrown1'


  txt=Label(root, text="Create an account", width=90)
  txt.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

  txt=Label(root, text="Enter Username", width=10)
  txt2=Label(root, text="Enter Email", width=10)
  txt1=Label(root, text="Enter Password")
  txt3=Label(root, text="Confirm Email", width=10)
  txt4=Label(root, text="Comfirm Password")


  global usrn
  global mail
  global passw
  global mail1
  global passw1

  usrn=Entry(root, width=32, borderwidth=5)
  mail=Entry(root, width=32, borderwidth=5)
  passw=Entry(root, width=32, borderwidth=5, show="*")
  mail1=Entry(root, width=32, borderwidth=5)
  passw1=Entry(root, width=32, borderwidth=5, show="*")

  cbtn=Button(root, text="Create account", padx=130, pady=10,height=3, command=createpass)

  txt.grid(row=1, column=0)
  txt1.grid(row=2, column=0)
  txt3.grid(row=5, column=0)
  txt4.grid(row=3, column=0)
  usrn.grid(row=1, column=1)
  passw.grid(row=2, column=1)
  txt2.grid(row=4, column=0)
  mail.grid(row=4, column=1)
  mail1.grid(row=5, column=1)
  passw1.grid(row=3, column=1)
  cbtn.grid(row=6, column=1)
  


def createpass():
  

  global usrn
  global lst
  global mail
  global passw
  global mail1
  global passw1

  fmail=mail.get()
  smail=mail1.get()
  fpassw=passw.get()
  spassw=passw1.get()
  fusrn=usrn.get()


  global root
  root.destroy()


  if smail==fmail and spassw==fpassw and fusrn not in usrn_pass.keys():
    try:
        myconn=mys.connect(host='localhost',user='root',\
                                 passwd='adis',database='12project')
        mycur=myconn.cursor()
        mycur.execute("Insert into logintable values('{}','{}','{}',Null,Null)".format(fusrn,fmail,fpassw))
        myconn.commit()
        logindict()

    except Exception as e:
        print(e)

    root=Tk()
    root.title("successfull")
    root['background'] = 'RosyBrown1'

    succ=Label(text="Account created successfully")
    cont=Button(root, text="Continue", width=50,height=3, command= login)

    succ.pack()
    cont.pack()

  else:
    root=Tk()
    root.title("Failed")
    root['background'] = 'RosyBrown1'

    failtxt=Label(root, text="Either, Passwords do not match, Emails do not match, Username is taken")
    failtxt.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    backbtn=Button(root, text="Try Again", width=45,height=3, command= signin)
    registerbtn=Button(root, text="Login", width=45,height=3, command= login)

    backbtn.grid(row=1,column=0)
    registerbtn.grid(row=1,column=1)



def acctype():
    global susrn
    global spassw

    lst1=usrn_pass["admin"]

    if susrn=="admin" and spassw==lst1[1]:
        adminmain()
    else:
        main()

def adminmain():
    global root
    root.destroy()
    root=Tk()
    root['background'] = 'RosyBrown1'
    root.geometry("1400x1000")

    title=Label(root, text="... Airways")
    status=Button(root, text="Check flight Status", width=50,height=3, command= status1)
    available=Button(root, text="Check Available Flights", width=50,height=3, command= available1)
    edit=Button(root, text="Edit/Add flight details", width=50,height=3, command= edit1)
    book=Button(root, text="Book/Cancel/Manage Flight", width=50,height=3, command= bookmenu)
    searchpass=Button(root, text="Search Passengers", width=50,height=3, command= searchpassengers)

    title.grid(row=0,column=0,columnspan=3)
    status.grid(row=2,column=0)
    available.grid(row=2,column=1)
    edit.grid(row=2,column=2)
    book.grid(row=3,column=1)
    searchpass.grid(row=3,column=0)
    
    canvas=Canvas(root, width=1300,height=540,bg='RosyBrown1',highlightthickness=0)
    canvas.grid(row=1,column=0,columnspan=3)
    photo = PhotoImage(file = "airplane-fact.gif")
    canvas.create_image(20,20,anchor=NW, image=photo)
    mainloop()



def main():
  global root
  root.destroy()
  root=Tk()
  root.title("Flight management system")
  root['background'] = 'RosyBrown1'
  root.geometry("1400x1000")

  title=Label(root, text="... Airways")
  status=Button(root, text="Check flight Status", width=50,height=3, command= status1)
  available=Button(root, text="Check Available Flights", width=50,height=3, command= available1)
  book=Button(root, text="Book/Cancel/Manage Flight", width=50,height=3, command= bookmenu)

  title.grid(row=0,column=0,columnspan=3)
  status.grid(row=2,column=0)
  available.grid(row=2,column=1)
  book.grid(row=2,column=2)
  canvas=Canvas(root, width=1300,height=540,bg='RosyBrown1',highlightthickness=0)
  canvas.grid(row=1,column=0,columnspan=3)
  photo = PhotoImage(file = "airplane-fact.gif")
  canvas.create_image(20,20,anchor=NW, image=photo)
  mainloop()

def status1():
    
    def statuspass():
        number=fnoe.get()
        lst1=flights[number]

        if number in flights.keys():
            frome.delete(0, END)
            toe.delete(0, END)
            datee.delete(0, END)
            timee.delete(0, END)
            statuse.delete(0, END)

            frome.insert(0,lst1[0])
            toe.insert(0,lst1[1])
            datee.insert(0,lst1[2])
            timee.insert(0,lst1[3])
            statuse.insert(0,lst1[4])
        else:
            root=Tk()
            root['background'] = 'RosyBrown1'

            error=Label(root,text="Flight number not found")

            error.pack()
            
            
    root=Tk()
    root.title("Check Flight Status")
    root['background'] = 'RosyBrown1'

    title=Label(root, text="Check Flight Status")
    fnot=Label(root, text="Flight Number:")
    fromt=Label(root, text="From:")
    tot=Label(root, text="To:")
    datet=Label(root, text="Date of Departure:")
    timet=Label(root, text="Time of Departure:")
    statust=Label(root, text="Status:")
    fnoe=Entry(root,width=32, borderwidth=5)
    frome=Entry(root,width=32, borderwidth=5)
    toe=Entry(root,width=32, borderwidth=5)
    datee=Entry(root,width=32, borderwidth=5)
    timee=Entry(root,width=32, borderwidth=5)
    statuse=Entry(root,width=32, borderwidth=5)
    findbtn=Button(root,text="Check Status",width=50,height=3, command=statuspass)

    title.grid(row=0,column=0,columnspan=2)
    fnot.grid(row=1,column=0)
    fromt.grid(row=2,column=0)
    tot.grid(row=3,column=0)
    datet.grid(row=4,column=0)
    timet.grid(row=5,column=0)
    statust.grid(row=6,column=0)
    fnoe.grid(row=1,column=1)
    frome.grid(row=2,column=1)
    toe.grid(row=3,column=1)
    datee.grid(row=4,column=1)
    timee.grid(row=5,column=1)
    statuse.grid(row=6,column=1)
    findbtn.grid(row=7,column=0,columnspan=2)

    


def available1():
    
    def checkavailable():
                
        from_=frome.get()
        to_=toe.get()
        date_=datee.get()



        try:
          myconn = mys.connect(host='localhost', user="root",\
                         passwd="adis", database="12project")
          if myconn.is_connected():
            print("connection succssful")
            mycur = myconn.cursor()
            query = "select * from flightdetails where podeparture='{}' and poarrival='{}' and date='{}';"\
                               .format(from_,to_,date_)
            mycur.execute(query)
            rs = mycur.fetchall()
            root = Tk()
            root.geometry("900x800")
            root.title("Flights Available")
            root['background'] = 'RosyBrown1'
            
            Title=Label(root, text ="Available Flights")
            
            frame = Frame(root)
            tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7,8), height = 40, show = "headings")
            
            tree.heading(1, text = "Flight No.")
            tree.heading(2, text = "Departure")
            tree.heading(3, text = "Arrival")
            tree.heading(4, text = "Date")
            tree.heading(5, text = "Time")
            tree.heading(6, text = "Status")
            tree.heading(7, text = "Total Seats")
            tree.heading(8, text = "Available Seats")
            tree.column(1, width = 75)
            tree.column(2, width = 130)
            tree.column(3, width = 130)
            tree.column(4, width = 100)
            tree.column(5, width = 75)
            tree.column(6, width = 130)
            tree.column(7, width = 85)
            tree.column(8, width = 85)
            scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            
            Title.grid(row=0,column=0,columnspan=2)
            frame.grid(row=1,column=0,columnspan=2)
            tree.pack(side = 'right')
            scroll.pack(side = 'right', fill = 'y')

            
            for val in rs:
                tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6],val[7]))
        except Exception as e:
          print(e)


                
                
    root=Tk()
    root.title("Check Available Flights")
    root['background'] = 'RosyBrown1'

    title=Label(root,text="Available flights")
    frome=Entry(root,width=32, borderwidth=5)
    toe=Entry(root,width=32, borderwidth=5)
    datee=Entry(root,width=32, borderwidth=5)
    fromt=Label(root,text="From:")
    tot=Label(root,text="To:")
    datet=Label(root,text="Date(dd/mm/yyyy)")
    check=Button(root,text="Check available flights",width=50,height=3,command= checkavailable)


    title.grid(row=0,column=0,columnspan=2)
    frome.grid(row=1,column=1)
    toe.grid(row=2,column=1)
    datee.grid(row=3,column=1)
    fromt.grid(row=1,column=0)
    tot.grid(row=2,column=0)
    datet.grid(row=3,column=0)
    check.grid(row=4,column=0,columnspan=2)

    



def edit1():
    def add():
        try:
            myconn=mys.connect(host='localhost',user='root',\
                                 passwd='adis',database='12project')
            mycur=myconn.cursor()
            mycur.execute("Insert into flightdetails values('{}','{}','{}','{}','{}','{}',{},{});"\
                              .format(fnoe.get(),frome.get(),toe.get(),datee.get(),timee.get(),statuse.get(),int(noseatse.get()),int(availseatse.get())))
            myconn.commit()
            flightsdict()
        except Exception as e:
            print(e)

        root=Tk()
        root.title("Find Flight")
        root['background'] = 'RosyBrown1'

        text=Label(root,text="Flight Number added")
            
        text.pack()
    def editpass():
        root=Tk()
        root.title("Edit Flight Details")
        root['background'] = 'RosyBrown1'

        btn=Button(root,text="Click if you are sure",height=3,command= change)

        btn.grid(row=1,column=1)

    def change():

        if fnoe.get() in flights.keys():
            root=Tk()
            root.title("Edit Flight Details")
            root['background'] = 'RosyBrown1'
            
            fromnew=frome.get()
            tonew=toe.get()
            datenew=datee.get()
            timenew=timee.get()
            statusnew=statuse.get()
            noseatsnew=int(noseatse.get())
            availseatsnew=int(availseatse.get())
            
            try:
                myconn=mys.connect(host='localhost',user='root',\
                                 passwd='adis',database='12project')
                mycur=myconn.cursor()
                mycur.execute("update flightdetails set podeparture='{}',poarrival='{}',date='{}',time='{}',status='{}',noseats={},availseats={} where Fno='{}'"\
                              .format(fromnew,tonew,datenew,timenew,statusnew,noseatsnew,availseatsnew,fnoe.get()))
                myconn.commit()
                flightsdict()
            except Exception as e:
                print(e)


            done=Label(root,text="Details Changed Succesfully")
            btn=Button(root,text="Go to home page",height=3,command= acctype)
            
            done.grid(row=0,column=0)
            btn.grid(row=0,column=1)

        else:
            root=Tk()
            root.title("Not Found")
            root['background'] = 'RosyBrown1'

            error=Label(root,text="Flight number not found")
            addbtn=Button(root,text="Click if you want to add the flight",height=3,command= add)

            error.grid(row=0,column=0)
            addbtn.grid(row=1,column=0)

        

    def find():

        if fnoe.get() in flights.keys():
            lst1=flights[fnoe.get()]
            frome.delete(0, END)
            toe.delete(0, END)
            datee.delete(0, END)
            timee.delete(0, END)
            statuse.delete(0, END)
            noseatse.delete(0, END)
            availseatse.delete(0, END)

            frome.insert(0,lst1[0])
            toe.insert(0,lst1[1])
            datee.insert(0,lst1[2])
            timee.insert(0,lst1[3])
            statuse.insert(0,lst1[4])
            noseatse.insert(0,lst1[5])
            availseatse.insert(0,lst1[6])
        else:
            root=Tk()
            root.title("Not Found")
            root['background'] = 'RosyBrown1'

            error=Label(root,text="Flight number not found")

            error.grid(row=0,column=0)




    root=Tk()
    root['background'] = 'RosyBrown1'

    title=Label(root, text="Check Flight Status")
    fnot=Label(root, text="Flight Number:")
    fromt=Label(root, text="From:")
    tot=Label(root, text="To:")
    datet=Label(root, text="Date of Departure:")
    timet=Label(root, text="Time of Departure:")
    statust=Label(root, text="Status:")
    noseatst=Label(root, text="Total Seats:")
    availseatst=Label(root, text="Available Seats:")
    fnoe=Entry(root,width=32, borderwidth=5)
    frome=Entry(root,width=32, borderwidth=5)
    toe=Entry(root,width=32, borderwidth=5)
    datee=Entry(root,width=32, borderwidth=5)
    timee=Entry(root,width=32, borderwidth=5)
    statuse=Entry(root,width=32, borderwidth=5)
    noseatse=Entry(root,width=32, borderwidth=5)
    availseatse=Entry(root,width=32, borderwidth=5)
    findbtn=Button(root,text="Find Details",width=35,height=3, command= find)
    editbtn=Button(root,text="Edit Details",width=35,height=3, command= editpass)
    addbtn=Button(root,text="Add Details",width=35,height=3,command= add)

           
    title.grid(row=0,column=0,columnspan=3)
    fnot.grid(row=1,column=0,columnspan=2)
    fromt.grid(row=2,column=0,columnspan=2)
    tot.grid(row=3,column=0,columnspan=2)
    datet.grid(row=4,column=0,columnspan=2)
    timet.grid(row=5,column=0,columnspan=2)
    statust.grid(row=6,column=0,columnspan=2)
    fnoe.grid(row=1,column=2)
    frome.grid(row=2,column=2)
    toe.grid(row=3,column=2)
    datee.grid(row=4,column=2)
    timee.grid(row=5,column=2)
    statuse.grid(row=6,column=2)
    noseatst.grid(row=7,column=0,columnspan=2)
    availseatst.grid(row=8,column=0,columnspan=2)
    noseatse.grid(row=7,column=2)
    availseatse.grid(row=8,column=2)
    findbtn.grid(row=9,column=2)
    editbtn.grid(row=9,column=1)
    addbtn.grid(row=9,column=0)


def bookmenu():
 root=Tk()
 root.title("Book/cancel")
 root['background'] = 'RosyBrown1'
 title=Label(root, text="Book/Cancel Your Flight")
 book=Button(root, text="Book Flight", width=50,height=3, command= booksearch)
 cancelbutton=Button(root, text="Cancel Flight", width=50,height=3, command=cancel)
 
 title.grid(row=0,column=0,columnspan=2)
 book.grid(row=2,column=0)
 cancelbutton.grid(row=2,column=1)


def booksearch():
    global fromentry
    global toentry
    global dateentry
    
    
    root=Tk()
    root.title("Book flight")
    root['background'] = 'RosyBrown1'
    title=Label(root,text="Available flights")
    fromentry=Entry(root,width=32, borderwidth=5)
    toentry=Entry(root,width=32, borderwidth=5)
    dateentry=Entry(root,width=32, borderwidth=5)
    fromt=Label(root,text="From:")
    tot=Label(root,text="To:")
    datet=Label(root,text="Date(dd/mm/yyyy)")
    check=Button(root,text="Check available flights",width=50,height=3,command= book)


    title.grid(row=0,column=0,columnspan=2)
    fromentry.grid(row=1,column=1)
    toentry.grid(row=2,column=1)
    dateentry.grid(row=3,column=1)
    fromt.grid(row=1,column=0)
    tot.grid(row=2,column=0)
    datet.grid(row=3,column=0)
    check.grid(row=4,column=0,columnspan=2)



def book():


    global fromentry
    global toentry
    global dateentry
    fromee=fromentry.get()
    toee=toentry.get()
    dateee=dateentry.get()


    try:
        myconn = mys.connect(host='localhost', user="root",\
                         passwd="adis", database="12project")
        if myconn.is_connected():
            print("connection succssful")
            mycur = myconn.cursor()
            query = "select * from flightdetails where podeparture='{}' and poarrival='{}' and date='{}';"\
                               .format(fromee,toee,dateee)
            mycur.execute(query)
            rs = mycur.fetchall()
            root = Tk()
            root.geometry("900x800")
            root.title("Flights Available")
            root['background'] = 'RosyBrown1'
            
            Title=Label(root, text ="Available Flights")
            
            frame = Frame(root)
            tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7,8), height = 15, show = "headings")
            
            tree.heading(1, text = "Flight No.")
            tree.heading(2, text = "Departure")
            tree.heading(3, text = "Arrival")
            tree.heading(4, text = "Date")
            tree.heading(5, text = "Time")
            tree.heading(6, text = "Status")
            tree.heading(7, text = "Total Seats")
            tree.heading(8, text = "Available Seats")
            tree.column(1, width = 75)
            tree.column(2, width = 130)
            tree.column(3, width = 130)
            tree.column(4, width = 100)
            tree.column(5, width = 75)
            tree.column(6, width = 130)
            tree.column(7, width = 85)
            tree.column(8, width = 85)
            scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)


            global fnobook
            global noseats

            fnotext=Label(root, text="Enter the flight number u would like to book")
            fnobook=Entry(root,width=32, borderwidth=5)
            noseatstext=Label(root, text="Enter the number of Seats u would like to book")
            noseats=Entry(root,width=32, borderwidth=5)
            bookbutton=Button(root,text="Book",width=50,height=3, command= bookpass)
            
            
            Title.grid(row=0,column=0,columnspan=2)
            frame.grid(row=1,column=0,columnspan=2)
            tree.pack(side = 'right')
            scroll.pack(side = 'right', fill = 'y')
            fnotext.grid(row=3,column=0)
            fnobook.grid(row=3,column=1)
            noseats.grid(row=4,column=1)
            noseatstext.grid(row=4,column=0)
            bookbutton.grid(row=5,column=1,columnspan=2)
            
            for val in rs:
                tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6],val[7]))
    except Exception as e:
        print(e)


def bookpass():
  root=Tk()
  root['background'] = 'RosyBrown1'
  btn=Button(root,text="Are you sure?",width=50,height=3, command= bookcont)
  btn.pack()



def bookcont():
  global fnobook
  global noseats
  global susrn

  fno=fnobook.get()
  seats=int(noseats.get())

  if fno in flights.keys():
    try:
      myconn=mys.connect(host='localhost',user='root',\
                          passwd='adis',database='12project')
      mycur=myconn.cursor()
      query1="update flightdetails set availseats=availseats-{} where fno='{}';".format(seats,fno)
                       
      mycur.execute(query1)
      myconn.commit()
      
      myconnn=mys.connect(host='localhost',user='root',\
                          passwd='adis',database='12project')
      mycurr=myconnn.cursor()
      
      query2="update logintable set flightbook='{}',noseats={} where usrname='{}';".format(fno,seats,susrn)
      mycurr.execute(query2)
      myconnn.commit()
      

      root=Tk()
      root['background'] = 'RosyBrown1'
      succ=Label(root, text="booked successfully")
      succ.pack()
    except Exception as e:
      print(e)


  else:
    root=Tk()
    root['background'] = 'RosyBrown1'
    fail=Label(root, text="Flight number not found")

    fail.pack()

  logindict()
  flightsdict()


def cancel():
  global susrn
  flight=usrn_pass[susrn][2]
  booked=usrn_pass[susrn][3]

  try:
    myconn = mys.connect(host='localhost', user="root",\
                         passwd="adis", database="12project")
    if myconn.is_connected():
      print("connection succssful")
      mycur = myconn.cursor()
      query = "select * from flightdetails where fno='{}';"\
                               .format(flight)
      mycur.execute(query)
      rs = mycur.fetchall()
      root = Tk()
      root.geometry("1000x800")
      root.title("Flights Available")
      root['background'] = 'RosyBrown1'
            
      Title=Label(root, text ="Cancel Ticket")
            
      frame = Frame(root)
      tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7,8,9), height = 15, show = "headings")
            
      tree.heading(1, text = "Flight No.")
      tree.heading(2, text = "Departure")
      tree.heading(3, text = "Arrival")
      tree.heading(4, text = "Date")
      tree.heading(5, text = "Time")
      tree.heading(6, text = "Status")
      tree.heading(7, text = "Total Seats")
      tree.heading(8, text = "Available Seats")
      tree.heading(9, text = "Tickets Booked")
      tree.column(1, width = 75)
      tree.column(2, width = 130)
      tree.column(3, width = 130)
      tree.column(4, width = 100)
      tree.column(5, width = 75)
      tree.column(6, width = 130)
      tree.column(7, width = 85)
      tree.column(8, width = 85)
      tree.column(9, width = 85)
      scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)


      global cancelticket

      canceltext=Label(root, text="Number of tickets to cancel")
      cancelticket=Entry(root,width=32, borderwidth=5)
      cancelbutton=Button(root,text="Cancel",width=50,height=3, command= cancelpass)
            
            
      Title.grid(row=0,column=0,columnspan=2)
      frame.grid(row=1,column=0,columnspan=2)
      tree.pack(side = 'right')
      scroll.pack(side = 'right', fill = 'y')
      canceltext.grid(row=3,column=0)
      cancelticket.grid(row=3,column=1)
      cancelbutton.grid(row=5,column=1,columnspan=2)
            
      for val in rs:
        tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6],val[7],booked))
  except Exception as e:
    print(e)


def cancelpass():
  root=Tk()
  root['background'] = 'RosyBrown1'
  btn=Button(root,text="Are you sure?",width=50,height=3, command= cancelcont)
  btn.pack()

def cancelcont():
  global susrn
  global cancelticket

  nocancel=int(cancelticket.get())
  fno=usrn_pass[susrn][2]

  try:
    myconn=mys.connect(host='localhost',user='root',\
                          passwd='adis',database='12project')
    mycur=myconn.cursor()
    query1="update flightdetails set availseats=availseats+{} where fno='{}';".format(nocancel,fno)
                       
    mycur.execute(query1)
    myconn.commit()
      
    myconnn=mys.connect(host='localhost',user='root',\
                          passwd='adis',database='12project')
    mycurr=myconnn.cursor()

    if nocancel==usrn_pass[susrn][3]:
      query2="update logintable set flightbook=null,noseats=null where usrname='{}';".format(susrn)
      mycurr.execute(query2)
      myconnn.commit()
    else:
      query2="update logintable set noseats=noseats-{} where usrname='{}';".format(nocancel,susrn)
      mycurr.execute(query2)
      myconnn.commit()
      

    root=Tk()
    root['background'] = 'RosyBrown1'
    succ=Label(root, text="Cancelled successfully")
    succ.pack()
  except Exception as e:
    print(e)

  logindict()
  flightsdict()




def searchpassengers():
    global fnosearch
    
    root=Tk()
    root.title("Search Passengers")
    root['background'] = 'RosyBrown1'
    title=Label(root,text="Search Passengers")
    fnosearch=Entry(root,width=32, borderwidth=5)
    fnot=Label(root,text="Flight number:")
    srchbtn=Button(root,text="Search Passengers",width=50,height=3,command=searchpasscont)


    title.grid(row=0,column=0,columnspan=2)
    fnosearch.grid(row=1,column=1)
    fnot.grid(row=1,column=0)
    srchbtn.grid(row=2,column=0,columnspan=2)

def searchpasscont():
    global fnosearch
    fno=fnosearch.get()

    try:
        myconn = mys.connect(host='localhost', user="root",\
                         passwd="adis", database="12project")
        if myconn.is_connected():
            print("connection succssful")
        mycur = myconn.cursor()
        query = "select usrname,flightbook,noseats from logintable where flightbook='{}';"\
                               .format(fno)
        mycur.execute(query)
        rs = mycur.fetchall()
        root = Tk()
        root.geometry("625x800")
        root.title("Flights Available")
        root['background'] = 'RosyBrown1'
            
        Title=Label(root, text ="Passengers")
            
        frame = Frame(root)
    except Exception as e:
        print(e)



usrn_pass={}
flights = {}


logindict()
flightsdict()
menu()


'''
import turtle
from tkinter import *
import mysql.connector as mys
from tkinter import ttk


colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(25):
    my_pen.pencolor(colors[x % 6])
    my_pen.width(x/100 + 1)
    my_pen.forward(x) 
    my_pen.left(59)


turtle.color('white')
style = ('Courier', 30, 'italic')
turtle.write('Welcome to Flight Management System', font=style, align='center')
turtle.hideturtle()




def menu():
    global root
    root=Toplevel()
    root.title("")

    txt=Label(root, text="Entry")
    txt.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    loginbtn=Button(root, text="Login",padx=90, pady=10, height=3, command= login)
    signinbtn=Button(root, text="Create an Acoount", padx=60, pady=10,height=3,command= signin)
    loginbtn.grid(row=2, column=0)
    signinbtn.grid(row=2, column=1)
    root['background'] = 'RosyBrown1'
    root.geometry("700x600")

    canvas=Canvas(root, width=700,height=470,bg='RosyBrown1',highlightthickness=0)
    canvas.grid(row=1,column=0,columnspan=2)
    photo = PhotoImage(file = "airlines1.gif")
    canvas.create_image(20,20,anchor=NW, image=photo)
    mainloop()



def login():
    global root
    root.destroy()
    root=Tk()
    root.title("Login Window")


    txt=Label(root, text="Login")
    txt.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    txt=Label(root, text="Enter Username")
    txt1=Label(root, text="Enter Password")

    global usrn
    global passw

    usrn=Entry(root, width=32, borderwidth=5)
    passw=Entry(root, width=32, borderwidth=5, show="*")

    logbtn=Button(root, text="Login", padx=130, pady=10,height=3, command= logpress)


    txt.grid(row=1, column=0)
    txt1.grid(row=2, column=0)
    usrn.grid(row=1, column=1)
    passw.grid(row=2, column=1)
    logbtn.grid(row=3, column=1)
    root['background'] = 'RosyBrown1'


def logpress():

    global susrn
    global spassw

    susrn=usrn.get()
    spassw=passw.get()

    global root
    root.destroy()

    global lst

    lst=usrn_pass[susrn]

    if susrn in usrn_pass.keys():

        root=Tk()
        root.title("")
        root['background'] = 'RosyBrown1'

        if spassw==lst[1]:

            succ=Label(root, text="Login succesfull")
            cont=Button(root, text="Continue", width=50,height=3, command= acctype)

            succ.pack()
            cont.pack()

        else:

            fail=Label(root, text="Password entered incorrectly")
            fail.grid(row=0,column=0, columnspan=2, padx=5, pady=5)

            back=Button(root, text="Try Again", width=45,height=3, command= login)
            change=Button(root, text="Change password", width=45,height=3, command= cpass)

            back.grid(row=1, column=0)
            change.grid(row=1, column=1)
    else:

        root=Tk()
        root.title("Login failed")
        root['background'] = 'RosyBrown1'

        failtxt=Label(root, text="Username not registered", width=100)
        failtxt.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        backbtn=Button(root, text="Try Again", width=45,height=3, command= login)
        registerbtn=Button(root, text="Register", width=45,height=3, command= signin)

        backbtn.grid(row=1,column=0)
        registerbtn.grid(row=1,column=1)

def cpass():

    global root
    root.destroy()

    root=Tk()
    root.title("Change Password")
    root['background'] = 'RosyBrown1'


    txt=Label(root, text="Change password")
    txt.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    txt=Label(root, text="Enter Username", width=20)
    txt2=Label(root, text="Enter Email", width=20)
    txt1=Label(root, text="Enter new Password", width=20)


    global usrn
    global mail
    global passw

    usrn=Entry(root, width=32, borderwidth=5)
    mail=Entry(root, width=32, borderwidth=5)
    passw=Entry(root, width=32, borderwidth=5, show="*")

    cbtn=Button(root, text="Change password", padx=130, pady=10,height=3, command=cpasscon)

    txt.grid(row=1, column=0)
    txt1.grid(row=2, column=0)
    usrn.grid(row=1, column=1)
    passw.grid(row=2, column=1)
    txt2.grid(row=3, column=0)
    mail.grid(row=3, column=1)
    cbtn.grid(row=4, column=1)







def cpasscon():

    fmail=mail.get()
    fpassw=passw.get()

    global root
    root.destroy()

    global lst
    global susrn

    if fmail==lst[0]:
        try:
            myconn=mys.connect(host='localhost',user='root', \
                               passwd='adis',database='12project')
            mycur=myconn.cursor()
            mycur.execute("update logintable set passwd='{}' where usrname='{}';".format(fpassw,susrn))
            myconn.commit()
            logindict()
        except Exception as e:
            print(e)

        root=Tk()
        root.title("Success")
        root['background'] = 'RosyBrown1'

        succ=Label(text="Password changed successfully")
        cont=Button(root, text="Continue", width=50,height=3, command= login)

        succ.pack()
        cont.pack()

    else:
        root=Tk()
        root['background'] = 'RosyBrown1'
        root.title("Failed")

        failtxt=Label(root, text="Email entered incorrectly")
        failtxt.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        backbtn=Button(root, text="Try Again", width=45,height=3, command= cpass)
        registerbtn=Button(root, text="Register", width=45,height=3, command= signin)

        backbtn.grid(row=1,column=0)
        registerbtn.grid(row=1,column=1)




def signin():
    global root
    root.destroy()

    root=Tk()
    root.title("Register")
    root['background'] = 'RosyBrown1'


    txt=Label(root, text="Create an account", width=90)
    txt.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    txt=Label(root, text="Enter Username", width=10)
    txt2=Label(root, text="Enter Email", width=10)
    txt1=Label(root, text="Enter Password")
    txt3=Label(root, text="Confirm Email", width=10)
    txt4=Label(root, text="Comfirm Password")


    global usrn
    global mail
    global passw
    global mail1
    global passw1

    usrn=Entry(root, width=32, borderwidth=5)
    mail=Entry(root, width=32, borderwidth=5)
    passw=Entry(root, width=32, borderwidth=5, show="*")
    mail1=Entry(root, width=32, borderwidth=5)
    passw1=Entry(root, width=32, borderwidth=5, show="*")

    cbtn=Button(root, text="Create account", padx=130, pady=10,height=3, command=createpass)

    txt.grid(row=1, column=0)
    txt1.grid(row=2, column=0)
    txt3.grid(row=5, column=0)
    txt4.grid(row=3, column=0)
    usrn.grid(row=1, column=1)
    passw.grid(row=2, column=1)
    txt2.grid(row=4, column=0)
    mail.grid(row=4, column=1)
    mail1.grid(row=5, column=1)
    passw1.grid(row=3, column=1)
    cbtn.grid(row=6, column=1)



def createpass():


    global usrn
    global lst
    global mail
    global passw
    global mail1
    global passw1

    fmail=mail.get()
    smail=mail1.get()
    fpassw=passw.get()
    spassw=passw1.get()
    fusrn=usrn.get()


    global root
    root.destroy()


    if smail==fmail and spassw==fpassw and fusrn not in usrn_pass.keys():
        try:
            myconn=mys.connect(host='localhost',user='root', \
                               passwd='adis',database='12project')
            mycur=myconn.cursor()
            mycur.execute("Insert into logintable values('{}','{}','{}',Null,Null)".format(fusrn,fmail,fpassw))
            myconn.commit()
            logindict()

        except Exception as e:
            print(e)

        root=Tk()
        root.title("successfull")
        root['background'] = 'RosyBrown1'

        succ=Label(text="Account created successfully")
        cont=Button(root, text="Continue", width=50,height=3, command= login)

        succ.pack()
        cont.pack()

    else:
        root=Tk()
        root.title("Failed")
        root['background'] = 'RosyBrown1'

        failtxt=Label(root, text="Either, Passwords do not match, Emails do not match, Username is taken")
        failtxt.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        backbtn=Button(root, text="Try Again", width=45,height=3, command= signin)
        registerbtn=Button(root, text="Login", width=45,height=3, command= login)

        backbtn.grid(row=1,column=0)
        registerbtn.grid(row=1,column=1)



def acctype():
    global susrn
    global spassw

    lst1=usrn_pass["admin"]

    if susrn=="admin" and spassw==lst1[1]:
        adminmain()
    else:
        main()

def adminmain():
    global root
    root.destroy()
    root=Toplevel()
    root['background'] = 'RosyBrown1'
    root.geometry("1400x1000")

    title=Label(root, text="... Airways")
    status=Button(root, text="Check flight Status", width=50,height=3, command= status1)
    available=Button(root, text="Check Available Flights", width=50,height=3, command= available1)
    edit=Button(root, text="Edit/Add flight details", width=50,height=3, command= edit1)
    book=Button(root, text="Book/Cancel/Manage Flight", width=50,height=3, command= bookmenu)
    searchpass=Button(root, text="Search Passengers", width=50,height=3, command= searchpassengers)

    title.grid(row=0,column=0,columnspan=3)
    status.grid(row=2,column=0)
    available.grid(row=2,column=1)
    edit.grid(row=2,column=2)
    book.grid(row=3,column=1)
    searchpass.grid(row=3,column=0)

    canvas=Canvas(root, width=1300,height=540,bg='RosyBrown1',highlightthickness=0)
    canvas.grid(row=1,column=0,columnspan=3)
    photo = PhotoImage(file = "airplane-fact.gif")
    canvas.create_image(20,20,anchor=NW, image=photo)
    mainloop()



def main():
    global root
    root.destroy()
    root=Toplevel()
    root.title("Flight management system")
    root['background'] = 'RosyBrown1'
    root.geometry("1400x1000")

    title=Label(root, text="... Airways")
    status=Button(root, text="Check flight Status", width=50,height=3, command= status1)
    available=Button(root, text="Check Available Flights", width=50,height=3, command= available1)
    book=Button(root, text="Book/Cancel/Manage Flight", width=50,height=3, command= bookmenu)

    title.grid(row=0,column=0,columnspan=3)
    status.grid(row=2,column=0)
    available.grid(row=2,column=1)
    book.grid(row=2,column=2)
    
    canvas=Canvas(root, width=1300,height=540,bg='RosyBrown1',highlightthickness=0)
    canvas.grid(row=1,column=0,columnspan=3)
    photo = PhotoImage(file = "airplane-fact.gif")
    canvas.create_image(20,20,anchor=NW, image=photo)
    mainloop()

def status1():

    def statuspass():
        number=fnoe.get()
        lst1=flights[number]

        if number in flights.keys():
            frome.delete(0, END)
            toe.delete(0, END)
            datee.delete(0, END)
            timee.delete(0, END)
            statuse.delete(0, END)

            frome.insert(0,lst1[0])
            toe.insert(0,lst1[1])
            datee.insert(0,lst1[2])
            timee.insert(0,lst1[3])
            statuse.insert(0,lst1[4])
        else:
            root=Tk()
            root['background'] = 'RosyBrown1'

            error=Label(root,text="Flight number not found")

            error.pack()


    root=Tk()
    root.title("Check Flight Status")
    root['background'] = 'RosyBrown1'

    title=Label(root, text="Check Flight Status")
    fnot=Label(root, text="Flight Number:")
    fromt=Label(root, text="From:")
    tot=Label(root, text="To:")
    datet=Label(root, text="Date of Departure:")
    timet=Label(root, text="Time of Departure:")
    statust=Label(root, text="Status:")
    fnoe=Entry(root,width=32, borderwidth=5)
    frome=Entry(root,width=32, borderwidth=5)
    toe=Entry(root,width=32, borderwidth=5)
    datee=Entry(root,width=32, borderwidth=5)
    timee=Entry(root,width=32, borderwidth=5)
    statuse=Entry(root,width=32, borderwidth=5)
    findbtn=Button(root,text="Check Status",width=50,height=3, command=statuspass)

    title.grid(row=0,column=0,columnspan=2)
    fnot.grid(row=1,column=0)
    fromt.grid(row=2,column=0)
    tot.grid(row=3,column=0)
    datet.grid(row=4,column=0)
    timet.grid(row=5,column=0)
    statust.grid(row=6,column=0)
    fnoe.grid(row=1,column=1)
    frome.grid(row=2,column=1)
    toe.grid(row=3,column=1)
    datee.grid(row=4,column=1)
    timee.grid(row=5,column=1)
    statuse.grid(row=6,column=1)
    findbtn.grid(row=7,column=0,columnspan=2)




def available1():

    def checkavailable():

        from_=frome.get()
        to_=toe.get()
        date_=datee.get()



        try:
            myconn = mys.connect(host='localhost', user="root", \
                                 passwd="adis", database="12project")
            if myconn.is_connected():
                print("connection succssful")
                mycur = myconn.cursor()
                query = "select * from flightdetails where podeparture='{}' and poarrival='{}' and date='{}';" \
                    .format(from_,to_,date_)
                mycur.execute(query)
                rs = mycur.fetchall()
                root = Tk()
                root.geometry("900x800")
                root.title("Flights Available")
                root['background'] = 'RosyBrown1'

                Title=Label(root, text ="Available Flights")

                frame = Frame(root)
                tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7,8), height = 40, show = "headings")

                tree.heading(1, text = "Flight No.")
                tree.heading(2, text = "Departure")
                tree.heading(3, text = "Arrival")
                tree.heading(4, text = "Date")
                tree.heading(5, text = "Time")
                tree.heading(6, text = "Status")
                tree.heading(7, text = "Total Seats")
                tree.heading(8, text = "Available Seats")
                tree.column(1, width = 75)
                tree.column(2, width = 130)
                tree.column(3, width = 130)
                tree.column(4, width = 100)
                tree.column(5, width = 75)
                tree.column(6, width = 130)
                tree.column(7, width = 85)
                tree.column(8, width = 85)
                scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)

                Title.grid(row=0,column=0,columnspan=2)
                frame.grid(row=1,column=0,columnspan=2)
                tree.pack(side = 'right')
                scroll.pack(side = 'right', fill = 'y')


                for val in rs:
                    tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6],val[7]))
        except Exception as e:
            print(e)




    root=Tk()
    root.title("Check Available Flights")
    root['background'] = 'RosyBrown1'

    title=Label(root,text="Available flights")
    frome=Entry(root,width=32, borderwidth=5)
    toe=Entry(root,width=32, borderwidth=5)
    datee=Entry(root,width=32, borderwidth=5)
    fromt=Label(root,text="From:")
    tot=Label(root,text="To:")
    datet=Label(root,text="Date(dd/mm/yyyy)")
    check=Button(root,text="Check available flights",width=50,height=3,command= checkavailable)


    title.grid(row=0,column=0,columnspan=2)
    frome.grid(row=1,column=1)
    toe.grid(row=2,column=1)
    datee.grid(row=3,column=1)
    fromt.grid(row=1,column=0)
    tot.grid(row=2,column=0)
    datet.grid(row=3,column=0)
    check.grid(row=4,column=0,columnspan=2)





def edit1():
    def add():
        try:
            myconn=mys.connect(host='localhost',user='root', \
                               passwd='adis',database='12project')
            mycur=myconn.cursor()
            mycur.execute("Insert into flightdetails values('{}','{}','{}','{}','{}','{}',{},{});" \
                          .format(fnoe.get(),frome.get(),toe.get(),datee.get(),timee.get(),statuse.get(),int(noseatse.get()),int(availseatse.get())))
            myconn.commit()
            flightsdict()
        except Exception as e:
            print(e)

        root=Tk()
        root.title("Find Flight")
        root['background'] = 'RosyBrown1'

        text=Label(root,text="Flight Number added")

        text.pack()
    def editpass():
        root=Tk()
        root.title("Edit Flight Details")
        root['background'] = 'RosyBrown1'

        btn=Button(root,text="Click if you are sure",height=3,command= change)

        btn.grid(row=1,column=1)

    def change():

        if fnoe.get() in flights.keys():
            root=Tk()
            root.title("Edit Flight Details")
            root['background'] = 'RosyBrown1'

            fromnew=frome.get()
            tonew=toe.get()
            datenew=datee.get()
            timenew=timee.get()
            statusnew=statuse.get()
            noseatsnew=int(noseatse.get())
            availseatsnew=int(availseatse.get())

            try:
                myconn=mys.connect(host='localhost',user='root', \
                                   passwd='adis',database='12project')
                mycur=myconn.cursor()
                mycur.execute("update flightdetails set podeparture='{}',poarrival='{}',date='{}',time='{}',status='{}',noseats={},availseats={} where Fno='{}'" \
                              .format(fromnew,tonew,datenew,timenew,statusnew,noseatsnew,availseatsnew,fnoe.get()))
                myconn.commit()
                flightsdict()
            except Exception as e:
                print(e)


            done=Label(root,text="Details Changed Succesfully")
            btn=Button(root,text="Go to home page",height=3,command= acctype)

            done.grid(row=0,column=0)
            btn.grid(row=0,column=1)

        else:
            root=Tk()
            root.title("Not Found")
            root['background'] = 'RosyBrown1'

            error=Label(root,text="Flight number not found")
            addbtn=Button(root,text="Click if you want to add the flight",height=3,command= add)

            error.grid(row=0,column=0)
            addbtn.grid(row=1,column=0)



    def find():

        if fnoe.get() in flights.keys():
            lst1=flights[fnoe.get()]
            frome.delete(0, END)
            toe.delete(0, END)
            datee.delete(0, END)
            timee.delete(0, END)
            statuse.delete(0, END)
            noseatse.delete(0, END)
            availseatse.delete(0, END)

            frome.insert(0,lst1[0])
            toe.insert(0,lst1[1])
            datee.insert(0,lst1[2])
            timee.insert(0,lst1[3])
            statuse.insert(0,lst1[4])
            noseatse.insert(0,lst1[5])
            availseatse.insert(0,lst1[6])
        else:
            root=Tk()
            root.title("Not Found")
            root['background'] = 'RosyBrown1'

            error=Label(root,text="Flight number not found")

            error.grid(row=0,column=0)




    root=Tk()
    root['background'] = 'RosyBrown1'

    title=Label(root, text="Check Flight Status")
    fnot=Label(root, text="Flight Number:")
    fromt=Label(root, text="From:")
    tot=Label(root, text="To:")
    datet=Label(root, text="Date of Departure:")
    timet=Label(root, text="Time of Departure:")
    statust=Label(root, text="Status:")
    noseatst=Label(root, text="Total Seats:")
    availseatst=Label(root, text="Available Seats:")
    fnoe=Entry(root,width=32, borderwidth=5)
    frome=Entry(root,width=32, borderwidth=5)
    toe=Entry(root,width=32, borderwidth=5)
    datee=Entry(root,width=32, borderwidth=5)
    timee=Entry(root,width=32, borderwidth=5)
    statuse=Entry(root,width=32, borderwidth=5)
    noseatse=Entry(root,width=32, borderwidth=5)
    availseatse=Entry(root,width=32, borderwidth=5)
    findbtn=Button(root,text="Find Details",width=35,height=3, command= find)
    editbtn=Button(root,text="Edit Details",width=35,height=3, command= editpass)
    addbtn=Button(root,text="Add Details",width=35,height=3,command= add)


    title.grid(row=0,column=0,columnspan=3)
    fnot.grid(row=1,column=0,columnspan=2)
    fromt.grid(row=2,column=0,columnspan=2)
    tot.grid(row=3,column=0,columnspan=2)
    datet.grid(row=4,column=0,columnspan=2)
    timet.grid(row=5,column=0,columnspan=2)
    statust.grid(row=6,column=0,columnspan=2)
    fnoe.grid(row=1,column=2)
    frome.grid(row=2,column=2)
    toe.grid(row=3,column=2)
    datee.grid(row=4,column=2)
    timee.grid(row=5,column=2)
    statuse.grid(row=6,column=2)
    noseatst.grid(row=7,column=0,columnspan=2)
    availseatst.grid(row=8,column=0,columnspan=2)
    noseatse.grid(row=7,column=2)
    availseatse.grid(row=8,column=2)
    findbtn.grid(row=9,column=2)
    editbtn.grid(row=9,column=1)
    addbtn.grid(row=9,column=0)


def bookmenu():
    root=Tk()
    root.title("Book/cancel")
    root['background'] = 'RosyBrown1'
    title=Label(root, text="Book/Cancel Your Flight")
    book=Button(root, text="Book Flight", width=50,height=3, command= booksearch)
    cancelbutton=Button(root, text="Cancel Flight", width=50,height=3, command=cancel)

    title.grid(row=0,column=0,columnspan=2)
    book.grid(row=2,column=0)
    cancelbutton.grid(row=2,column=1)


def booksearch():
    global fromentry
    global toentry
    global dateentry


    root=Tk()
    root.title("Book flight")
    root['background'] = 'RosyBrown1'
    title=Label(root,text="Available flights")
    fromentry=Entry(root,width=32, borderwidth=5)
    toentry=Entry(root,width=32, borderwidth=5)
    dateentry=Entry(root,width=32, borderwidth=5)
    fromt=Label(root,text="From:")
    tot=Label(root,text="To:")
    datet=Label(root,text="Date(dd/mm/yyyy)")
    check=Button(root,text="Check available flights",width=50,height=3,command= book)


    title.grid(row=0,column=0,columnspan=2)
    fromentry.grid(row=1,column=1)
    toentry.grid(row=2,column=1)
    dateentry.grid(row=3,column=1)
    fromt.grid(row=1,column=0)
    tot.grid(row=2,column=0)
    datet.grid(row=3,column=0)
    check.grid(row=4,column=0,columnspan=2)



def book():


    global fromentry
    global toentry
    global dateentry
    fromee=fromentry.get()
    toee=toentry.get()
    dateee=dateentry.get()


    try:
        myconn = mys.connect(host='localhost', user="root", \
                             passwd="adis", database="12project")
        if myconn.is_connected():
            print("connection succssful")
            mycur = myconn.cursor()
            query = "select * from flightdetails where podeparture='{}' and poarrival='{}' and date='{}';" \
                .format(fromee,toee,dateee)
            mycur.execute(query)
            rs = mycur.fetchall()
            root = Tk()
            root.geometry("900x800")
            root.title("Flights Available")
            root['background'] = 'RosyBrown1'

            Title=Label(root, text ="Available Flights")

            frame = Frame(root)
            tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7,8), height = 15, show = "headings")

            tree.heading(1, text = "Flight No.")
            tree.heading(2, text = "Departure")
            tree.heading(3, text = "Arrival")
            tree.heading(4, text = "Date")
            tree.heading(5, text = "Time")
            tree.heading(6, text = "Status")
            tree.heading(7, text = "Total Seats")
            tree.heading(8, text = "Available Seats")
            tree.column(1, width = 75)
            tree.column(2, width = 130)
            tree.column(3, width = 130)
            tree.column(4, width = 100)
            tree.column(5, width = 75)
            tree.column(6, width = 130)
            tree.column(7, width = 85)
            tree.column(8, width = 85)
            scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)


            global fnobook
            global noseats

            fnotext=Label(root, text="Enter the flight number u would like to book")
            fnobook=Entry(root,width=32, borderwidth=5)
            noseatstext=Label(root, text="Enter the number of Seats u would like to book")
            noseats=Entry(root,width=32, borderwidth=5)
            bookbutton=Button(root,text="Book",width=50,height=3, command= bookpass)


            Title.grid(row=0,column=0,columnspan=2)
            frame.grid(row=1,column=0,columnspan=2)
            tree.pack(side = 'right')
            scroll.pack(side = 'right', fill = 'y')
            fnotext.grid(row=3,column=0)
            fnobook.grid(row=3,column=1)
            noseats.grid(row=4,column=1)
            noseatstext.grid(row=4,column=0)
            bookbutton.grid(row=5,column=1,columnspan=2)

            for val in rs:
                tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6],val[7]))
    except Exception as e:
        print(e)


def bookpass():
    root=Tk()
    root['background'] = 'RosyBrown1'
    btn=Button(root,text="Are you sure?",width=50,height=3, command= bookcont)
    btn.pack()



def bookcont():
    global fnobook
    global noseats
    global susrn

    fno=fnobook.get()
    seats=int(noseats.get())

    if fno in flights.keys():
        try:
            myconn=mys.connect(host='localhost',user='root', \
                               passwd='adis',database='12project')
            mycur=myconn.cursor()
            query1="update flightdetails set availseats=availseats-{} where fno='{}';".format(seats,fno)

            mycur.execute(query1)
            myconn.commit()

            myconnn=mys.connect(host='localhost',user='root', \
                                passwd='adis',database='12project')
            mycurr=myconnn.cursor()

            query2="update logintable set flightbook='{}',noseats={} where usrname='{}';".format(fno,seats,susrn)
            mycurr.execute(query2)
            myconnn.commit()


            root=Tk()
            root['background'] = 'RosyBrown1'
            succ=Label(root, text="booked successfully")
            succ.pack()
        except Exception as e:
            print(e)


    else:
        root=Tk()
        root['background'] = 'RosyBrown1'
        fail=Label(root, text="Flight number not found")

        fail.pack()

    logindict()
    flightsdict()


def cancel():
    global susrn
    flight=usrn_pass[susrn][2]
    booked=usrn_pass[susrn][3]

    try:
        myconn = mys.connect(host='localhost', user="root", \
                             passwd="adis", database="12project")
        if myconn.is_connected():
            print("connection succssful")
            mycur = myconn.cursor()
            query = "select * from flightdetails where fno='{}';" \
                .format(flight)
            mycur.execute(query)
            rs = mycur.fetchall()
            root = Tk()
            root.geometry("1000x800")
            root.title("Flights Available")
            root['background'] = 'RosyBrown1'

            Title=Label(root, text ="Cancel Ticket")

            frame = Frame(root)
            tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7,8,9), height = 15, show = "headings")

            tree.heading(1, text = "Flight No.")
            tree.heading(2, text = "Departure")
            tree.heading(3, text = "Arrival")
            tree.heading(4, text = "Date")
            tree.heading(5, text = "Time")
            tree.heading(6, text = "Status")
            tree.heading(7, text = "Total Seats")
            tree.heading(8, text = "Available Seats")
            tree.heading(9, text = "Tickets Booked")
            tree.column(1, width = 75)
            tree.column(2, width = 130)
            tree.column(3, width = 130)
            tree.column(4, width = 100)
            tree.column(5, width = 75)
            tree.column(6, width = 130)
            tree.column(7, width = 85)
            tree.column(8, width = 85)
            tree.column(9, width = 85)
            scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)


            global cancelticket

            canceltext=Label(root, text="Number of tickets to cancel")
            cancelticket=Entry(root,width=32, borderwidth=5)
            cancelbutton=Button(root,text="Cancel",width=50,height=3, command= cancelpass)


            Title.grid(row=0,column=0,columnspan=2)
            frame.grid(row=1,column=0,columnspan=2)
            tree.pack(side = 'right')
            scroll.pack(side = 'right', fill = 'y')
            canceltext.grid(row=3,column=0)
            cancelticket.grid(row=3,column=1)
            cancelbutton.grid(row=5,column=1,columnspan=2)

            for val in rs:
                tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6],val[7],booked))
    except Exception as e:
        print(e)


def cancelpass():
    root=Tk()
    root['background'] = 'RosyBrown1'
    btn=Button(root,text="Are you sure?",width=50,height=3, command= cancelcont)
    btn.pack()

def cancelcont():
    global susrn
    global cancelticket

    nocancel=int(cancelticket.get())
    fno=usrn_pass[susrn][2]

    try:
        myconn=mys.connect(host='localhost',user='root', \
                           passwd='adis',database='12project')
        mycur=myconn.cursor()
        query1="update flightdetails set availseats=availseats+{} where fno='{}';".format(nocancel,fno)

        mycur.execute(query1)
        myconn.commit()

        myconnn=mys.connect(host='localhost',user='root', \
                            passwd='adis',database='12project')
        mycurr=myconnn.cursor()

        if nocancel==usrn_pass[susrn][3]:
            query2="update logintable set flightbook=null,noseats=null where usrname='{}';".format(susrn)
            mycurr.execute(query2)
            myconnn.commit()
        else:
            query2="update logintable set noseats=noseats-{} where usrname='{}';".format(nocancel,susrn)
            mycurr.execute(query2)
            myconnn.commit()


        root=Tk()
        root['background'] = 'RosyBrown1'
        succ=Label(root, text="Cancelled successfully")
        succ.pack()
    except Exception as e:
        print(e)

    logindict()
    flightsdict()




def searchpassengers():
    global fnosearch

    root=Tk()
    root.title("Search Passengers")
    root['background'] = 'RosyBrown1'
    title=Label(root,text="Search Passengers")
    fnosearch=Entry(root,width=32, borderwidth=5)
    fnot=Label(root,text="Flight number:")
    srchbtn=Button(root,text="Search Passengers",width=50,height=3,command=searchpasscont)


    title.grid(row=0,column=0,columnspan=2)
    fnosearch.grid(row=1,column=1)
    fnot.grid(row=1,column=0)
    srchbtn.grid(row=2,column=0,columnspan=2)

def searchpasscont():
    global fnosearch
    fno=fnosearch.get()

    try:
        myconn = mys.connect(host='localhost', user="root", \
                             passwd="adis", database="12project")
        if myconn.is_connected():
            print("connection succssful")
        mycur = myconn.cursor()
        query = "select usrname,flightbook,noseats from logintable where flightbook='{}';" \
            .format(fno)
        mycur.execute(query)
        rs = mycur.fetchall()
        root = Tk()
        root.geometry("625x800")
        root.title("Flights Available")
        root['background'] = 'RosyBrown1'

        Title=Label(root, text ="Passengers")

        frame = Frame(root)
        tree = ttk.Treeview(frame, columns = (1,2,3), height = 30, show = "headings")

        tree.heading(1, text = "Username")
        tree.heading(2, text = "Flight Number")
        tree.heading(3, text = "Number of Seats")

        tree.column(1, width = 200)
        tree.column(2, width = 200)
        tree.column(3, width = 200)

        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)


        Title.grid(row=0,column=0,columnspan=2)
        frame.grid(row=1,column=0,columnspan=2)
        tree.pack(side = 'right')
        scroll.pack(side = 'right', fill = 'y')


        for val in rs:
            tree.insert('', 'end', values = (val[0], val[1], val[2]))
    except Exception as e:
        print(e)







def logindict():
    try:
        myconn=mys.connect(host='localhost',user='root', \
                           passwd='adis',database='12project')

        mycur=myconn.cursor()
        query='select * from logintable;'
        mycur.execute(query)
        rs=mycur.fetchall()    #Record Set
        count=mycur.rowcount
        for row in rs:
            usrn_pass[row[0]]=[row[1],row[2],row[3],row[4]]
    except Exception as e:
        print(e)

def flightsdict():
    try:
        myconn=mys.connect(host='localhost',user='root', \
                           passwd='adis',database='12project')

        mycur=myconn.cursor()
        query='select * from flightdetails;'
        mycur.execute(query)
        rs=mycur.fetchall()    #Record Set
        count=mycur.rowcount
        for row in rs:
            flights[row[0]]=[row[1],row[2],row[3],row[4],row[5],row[6],row[7]]
    except Exception as e:
        print(e)





usrn_pass={}
flights={}


logindict()
flightsdict()
menu()
