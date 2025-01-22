from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_dosa.delete(0,END)
    entry_cookies.delete(0,END)
    entry_tea.delete(0,END)
    entry_coffee.delete(0,END)
    entry_shake.delete(0,END)
    entry_idli.delete(0,END)
    entry_uttapam.delete(0,END)

def Total():
    try:a1=int(dosa.get())
    except: a1=0

    try:a2=int(cookies.get())
    except: a2=0

    try:a3=int(tea.get())
    except: a3=0

    try:a4=int(coffee.get())
    except: a4=0

    try:a5=int(shake.get())
    except: a5=0

    try:a6=int(idli.get())
    except: a6=0

    try:a7=int(uttapam.get())
    except: a7=0

    #define cost of each item per quantity
    c1=120*a1
    c2=40*a2
    c3=20*a3
    c4=40*a4
    c5=80*a5
    c6=60*a6
    c7=90*a7

    lbl_total=Label(f2,font=("aria",20,"bold"),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=("aria",20,"bold"),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)

    

Label(text="BILL MANAGEMENT",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

#MENU CARD
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

l1=Label(f,font=("Lucida calligraphy",15,"bold"),text="Dosa.......Rs.120/plate",fg="black",bg="lightgreen").place(x=10,y=80)
l2=Label(f,font=("Lucida calligraphy",15,"bold"),text="Cookies....Rs.40/plate",fg="black",bg="lightgreen").place(x=10,y=110)
l3=Label(f,font=("Lucida calligraphy",15,"bold"),text="Tea........Rs.20/cup",fg="black",bg="lightgreen").place(x=10,y=140)
l4=Label(f,font=("Lucida calligraphy",15,"bold"),text="Coffee.....Rs.40/cup",fg="black",bg="lightgreen").place(x=10,y=170)
l5=Label(f,font=("Lucida calligraphy",15,"bold"),text="Shake......Rs.80/glass",fg="black",bg="lightgreen").place(x=10,y=200)
l6=Label(f,font=("Lucida calligraphy",15,"bold"),text="Idli.......Rs.60/plate",fg="black",bg="lightgreen").place(x=10,y=230)
l7=Label(f,font=("Lucida calligraphy",15,"bold"),text="Uttapam....Rs.90/plate",fg="black",bg="lightgreen").place(x=10,y=260)

#BILL
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=("calibri",20),bg="lightyellow")
Bill.place(x=120,y=10)

#ENTRY WORK
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

dosa=StringVar()
cookies=StringVar()
tea=StringVar()
coffee=StringVar()
shake=StringVar()
idli=StringVar()
uttapam=StringVar()
Total_bill=StringVar()

#LABEL
lb1_dosa=Label(f1,font=("aria",20,"bold"),text="Dosa",width=12,fg="blue4")
lb1_cookies=Label(f1,font=("aria",20,"bold"),text="Cookies",width=12,fg="blue4")
lb1_tea=Label(f1,font=("aria",20,"bold"),text="Tea",width=12,fg="blue4")
lb1_coffee=Label(f1,font=("aria",20,"bold"),text="Coffee",width=12,fg="blue4")
lb1_shake=Label(f1,font=("aria",20,"bold"),text="Shake",width=12,fg="blue4")
lb1_idli=Label(f1,font=("aria",20,"bold"),text="Idli",width=12,fg="blue4")
lb1_uttapam=Label(f1,font=("aria",20,"bold"),text="Uttapam",width=12,fg="blue4")
lb1_dosa.grid(row=1,column=0)
lb1_cookies.grid(row=2,column=0)
lb1_tea.grid(row=3,column=0)
lb1_coffee.grid(row=4,column=0)
lb1_shake.grid(row=5,column=0)
lb1_idli.grid(row=6,column=0)
lb1_uttapam.grid(row=7,column=0)

#ENTRY
entry_dosa=Entry(f1,font=("aria",20,"bold"),textvariable=dosa,bd=6,width=8,bg="lightpink")
entry_cookies=Entry(f1,font=("aria",20,"bold"),textvariable=cookies,bd=6,width=8,bg="lightpink")
entry_tea=Entry(f1,font=("aria",20,"bold"),textvariable=tea,bd=6,width=8,bg="lightpink")
entry_coffee=Entry(f1,font=("aria",20,"bold"),textvariable=coffee,bd=6,width=8,bg="lightpink")
entry_shake=Entry(f1,font=("aria",20,"bold"),textvariable=shake,bd=6,width=8,bg="lightpink")
entry_idli=Entry(f1,font=("aria",20,"bold"),textvariable=idli,bd=6,width=8,bg="lightpink")
entry_uttapam=Entry(f1,font=("aria",20,"bold"),textvariable=uttapam,bd=6,width=8,bg="lightpink")
entry_dosa.grid(row=1,column=1)
entry_cookies.grid(row=2,column=1)
entry_tea.grid(row=3,column=1)
entry_coffee.grid(row=4,column=1)
entry_shake.grid(row=5,column=1)
entry_idli.grid(row=6,column=1)
entry_uttapam.grid(row=7,column=1)

#Buttons
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,"bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,"bold"),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)



root.mainloop()
