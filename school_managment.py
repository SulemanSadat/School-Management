from tkinter import *
import datetime


# ==================================Start=======================================
system = Tk()
system.geometry('1280x720')
system.resizable(0, 0)

system.title("School Management System")
system.config(bg='white')


def navigator():  # Navigation bar
    header = Frame(width=1280, height=40, bg='#00AAFF').place(x=0, y=0)
    name = Label(header, text='Home', font='bold 15', bg="#00AAFF", foreground='white').place(x=20, y=5)
    nav = Frame(width=300, height=680, background='#222').place(x=0, y=40)
    MyName = Label(nav, text="Suleman Sadat Admin", font='bold 14', bg='#222', foreground="white").place(x=100,y=85)  # admin name

    first = PhotoImage(file="./images/user.png")
    photo1 = Label(nav,image=first , background='#333').place(x=15, y=60)

    dush = Button(nav, text="Dashboard", background='#000', foreground="white", font='bold 15',command=dush1)  # Button 1
    dush.config(width=27, height=2)
    dush.place(x=-7, y=180)

    menu = Button(header, text="Home", font="bold 14", bg='#00AAFF',foreground='#FFF',activebackground='#00AAFF', command=home)
    menu.config(width=8, height=1)
    menu.place(x=0, y=0)

    profile = Button(nav, text="Profile", bg='#000', foreground="white", font='bold 15', command=Profile)  # Button 2
    profile.config(width=27, height=2)
    profile.place(x=-7, y=240)

    Student = Button(nav, text="Student Management", bg='#000', foreground="white", font='bold 15',command=about1)  # Button 3
    Student.config(width=27, height=2)
    Student.place(x=-7, y=300)

    classManage = Button(nav, text="Adminstrative Manager", bg='#000', foreground="white", font='bold 15',command=home)  # Button 4
    classManage.config(width=27, height=2)
    classManage.place(x=-7, y=360)

    School = Button(nav, text="Class Management", bg='#000', foreground="white", font='bold 15',command=Profile)  # Button 5
    School.config(width=27, height=2)
    School.place(x=-7, y=420)

    admin = Button(nav, text="School Management", bg='#000', foreground="white", font='bold 15',command=home)  # Button 6
    admin.config(width=27, height=2)
    admin.place(x=-7, y=480)

    subject = Button(nav, text="Subject Management", bg='#000', foreground="white", font='bold 15',command=home)  # Button 7
    subject.config(width=27, height=2)
    subject.place(x=-7, y=540)

    view = Button(nav, text="View Records", bg='#000', foreground="white", font='bold 15', command=view1)  # Button 8
    view.config(width=27, height=2)
    view.place(x=-7, y=600)

    about = Button(nav, text="About us", bg='#000', foreground="white", font='bold 15',command=about1)  # Button 9
    about.config(width=27, height=2)
    about.place(x=-7, y=660)





def dush1():
    header = Frame(width=1280, height=40, bg='#00AAFF').place(x=0, y=0)
    time = Label(header, text=f"{datetime.datetime.today()}", font="bold 14", bg='#00AAFF', foreground='white').place(x=930, y=5)
    menu = Button(header, text="Menu", font="bold 14", bg='#00AAFF', foreground='#FFF', activebackground='#00AAFF',command=navigator)
    menu.config(width=8, height=1)
    menu.place(x=0, y=0)
    background = Frame(width=1280, height=680, background='#FFFFFF').place(x=0, y=40)
    one2 = Button(text="Profile", font="bold 10",width=15, height=7, command=about1).place(x=200, y=100)
    one3 = Button(text="Student Registeration", font="bold 10", width=15, height=7, command=about1).place(x=350, y=100)
    one4 = Button(text="Class Manager", font="bold 10", width=15, height=7, command=about1).place(x=500, y=100)
    one5 = Button(text="Subject Manager", font="bold 10", width=15, height=7, command=about1).place(x=650, y=100)
    one6 = Button(text="Calendar", font="bold 10", width=15, height=7, command=about1).place(x=800, y=100)
    one7 = Button(text="View Users", font="bold 10", width=15, height=7, command=about1).place(x=800, y=100)
    one8 = Button(text="Result Manager", font="bold 10", width=15, height=7, command=about1).place(x=950, y=100)

    one20 = Button(text="Class ", font="bold 10",width=15, height=7, command=about1).place(x=200, y=500)
    one21 = Button(text="Student Registeration", font="bold 10", width=15, height=7, command=about1).place(x=350, y=500)
    one22= Button(text="Class Manager", font="bold 10", width=15, height=7, command=about1).place(x=500, y=500)
    one23 = Button(text="Subject Manager", font="bold 10", width=15, height=7, command=about1).place(x=650, y=500)
    one24= Button(text="Calendar", font="bold 10", width=15, height=7, command=about1).place(x=800, y=500)
    one25 = Button(text="View Users", font="bold 10", width=15, height=7, command=about1).place(x=800, y=500)
    one26 = Button(text="Result Manager", font="bold 10", width=15, height=7, command=about1).place(x=950, y=500)

    close1 = Button(header, text="Exit", font="bold 15", background="#00AAFF", foreground="#FFF", command=back)
    close1.pack()
    close1.config(width=6, height=1)
    close1.place(x=1210, y=0)



def Profile():
    header = Frame(width=1280, height=40, bg='#00AAFF').place(x=0, y=0)
    time = Label(header, text=f"{datetime.datetime.today()}", font="bold 14", bg='#00AAFF', foreground='white').place(x=930, y=5)
    menu = Button(header, text="Menu", font="bold 14", bg='#00AAFF', foreground='#FFF', activebackground='#00AAFF',command=navigator)
    menu.config(width=8, height=1)
    menu.place(x=0, y=0)
    background = Frame(width=1280, height=680, background='#FFF').place(x=0, y=40)

    me = Label(background,background='white',text="School Management System",font="bold 40").place(x=320,y=300)
    me = Label(background, background='#FFF', text="The program has been written with Python Programming Language by Suleman Sadat From Afghanistan.✅",font="bold 15").place(x=190, y=550)


def view1():
    header = Frame(width=1280, height=40, bg='#00AAFF').place(x=0, y=0)
    time = Label(header, text=f"{datetime.datetime.today()}", font="bold 14", bg='#00AAFF', foreground='white').place(x=930, y=5)
    menu = Button(header, text="Menu", font="bold 14", bg='#00AAFF', foreground='#FFF', activebackground='#00AAFF',command=navigator)
    menu.config(width=8, height=1)
    menu.place(x=0, y=0)
    background = Frame(width=1280, height=680, background='#FFF').place(x=0, y=40)
    follow = Label(text="Follow me in Instagram, Facebook, Twitter",bg='#fff').place(x=500,y=400)


def Student1():
    header = Frame(width=1280, height=40, bg='#00AAFF').place(x=0, y=0)
    time = Label(header, text=f"{datetime.datetime.today()}", font="bold 14", bg='#00AAFF', foreground='white').place(x=930, y=5)
    menu = Button(header, text="Menu", font="bold 14", bg='#00AAFF', foreground='#FFF', activebackground='#00AAFF',command=navigator)
    menu.config(width=8, height=1)
    menu.place(x=0, y=0)
    background = Frame(width=1280, height=680, background='#FFF').place(x=0, y=40)
def about1():
    header = Frame(width=1280, height=40, bg='#00AAFF').place(x=0, y=0)
    time = Label(header, text=f"{datetime.datetime.today()}", font="bold 14", bg='#00AAFF', foreground='white').place(x=930, y=5)
    menu = Button(header, text="Menu", font="bold 14", bg='#00AAFF', foreground='#FFF', activebackground='#00AAFF',command=navigator)
    menu.config(width=8, height=1)
    menu.place(x=0, y=0)
    background = Frame(width=1280, height=680, background='#FFF').place(x=0, y=40)

    me = Label(background,background='white',text="SULEMAN SADAT\nWeb Developer\nGraphic Designer\nSoftware Engineer\n\nCONTACT",font="bold 30").place(x=450,y=220)
    me = Label(background, background='white', text="E-mail: slemansadat779@gmail.com\nPhone: +93787721209",font="bold 12").place(x=490, y=520)


    close1 = Button(header, text="Exit", font="bold 15", background="#00AAFF", foreground="#FFF", command=back)
    close1.pack()
    close1.config(width=6, height=1)
    close1.place(x=1210, y=0)

def back():
    exit()



def home():
    header = Frame(width=1280, height=40, bg='#00AAFF').place(x=0, y=0)
    time = Label(header, text=f"{datetime.datetime.today()}", font="bold 14", bg='#00AAFF', foreground='white').place(x=930,y=5)
    menu = Button(header, text="Menu", font="bold 14", bg='#00AAFF',foreground='#FFF',activebackground='#00AAFF', command=navigator)
    menu.config(width=8, height=1)
    menu.place(x=0, y=0)
    background = Frame(width=1280, height=680, background='#DDD').place(x=0, y=40)
    close1 = Button(header, text="Exit", font="bold 15",background="#00AAFF",foreground="#FFF",command=back)
    close1.pack()
    close1.config(width=6,height=1)
    close1.place(x=1210, y=0)

    one1 = Button(text="Profile", font="bold 10", width=15, height=7, command=Profile).place(x=50, y=100)
    one2 = Button(text="Class Management", font="bold 10",width=15, height=7, command=about1).place(x=200, y=100)
    one3 = Button(text="Student Registeration", font="bold 10", width=15, height=7, command=about1).place(x=350, y=100)
    one4 = Button(text="Class Manager", font="bold 10", width=15, height=7, command=about1).place(x=500, y=100)
    one5 = Button(text="Subject Manager", font="bold 10", width=15, height=7, command=about1).place(x=650, y=100)
    one6 = Button(text="Calendar", font="bold 10", width=15, height=7, command=about1).place(x=800, y=100)
    one7 = Button(text="View Users", font="bold 10", width=15, height=7, command=about1).place(x=800, y=100)
    one8 = Button(text="Result Manager", font="bold 10", width=15, height=7, command=about1).place(x=950, y=100)
    one9 = Button(text="Adminstration", font="bold 10", width=15, height=7, command=about1).place(x=1100, y=100)

    one10= Button(text="Rules", font="bold 10", width=15, height=7, command=about1).place(x=50, y=300)
    one11 = Button(text="Fee Management", font="bold 10",width=15, height=7, command=about1).place(x=200, y=300)
    one12 = Button(text="System Management", font="bold 10", width=15, height=7, command=about1).place(x=350, y=300)
    one13 = Button(text="Online System", font="bold 10", width=15, height=7, command=about1).place(x=500, y=300)
    one14 = Button(text="Data Management", font="bol 10", width=15, height=7, command=about1).place(x=650, y=300)
    one15 = Button(text="Payments", font="bold 10", width=15, height=7, command=about1).place(x=800, y=300)
    one16 = Button(text="Online Class", font="bold 10", width=15, height=7, command=about1).place(x=800, y=300)
    one17= Button(text="Teachers", font="bold 10", width=15, height=7, command=about1).place(x=950, y=300)
    one18 = Button(text="Services", font="bold 10", width=15, height=7, command=about1).place(x=1100, y=300)

    one19 = Button(text="Student Mark", font="bold 10", width=15, height=7, command=about1).place(x=50, y=500)
    one20 = Button(text="Location", font="bold 10",width=15, height=7, command=about1).place(x=200, y=500)
    one21 = Button(text="Social Media", font="bold 10", width=15, height=7, command=about1).place(x=350, y=500)
    one22= Button(text="Lessons", font="bold 10", width=15, height=7, command=about1).place(x=500, y=500)
    one23 = Button(text="File Management", font="bold 10", width=15, height=7, command=about1).place(x=650, y=500)
    one24= Button(text="School Information", font="bold 10", width=15, height=7, command=about1).place(x=800, y=500)
    one25 = Button(text="Student Inforamtion", font="bold 10", width=15, height=7, command=about1).place(x=800, y=500)
    one26 = Button(text="Emails", font="bold 10", width=15, height=7, command=about1).place(x=950, y=500)
    one27 = Button(text="About", font="bold 10", width=15, height=7, command=about1).place(x=1100, y=500)



    system.mainloop()

home()




def exit():

    header = Frame(system, width=1280, height=40, bg='red').place(x=0, y=0)

