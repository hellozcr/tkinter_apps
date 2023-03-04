from tkinter import *
import sqlite3 as sq
from tkinter import ttk

#------connecting to database----
conn = sq.connect("register.db")
print("Database created")

curr =conn.cursor()

# --------creating table------
# curr.execute('CREATE TABLE REGISTER(NAME CHAR,ROLL INT PRIMARY KEY,AGE INT,CLASS CHAR,MARKS INT)')
# print("Table created...")



#------created by santo rabidas-----
root = Tk()
root.minsize(height=400, width=500)
root.title("Registration")

rollList =[]
data = conn.execute('SELECT * FROM REGISTER');
for col in data:
    rollList.append(col[1])

name=StringVar()
roll=IntVar()
age=IntVar()
clas=StringVar()
marks=IntVar()
sroll = IntVar()

def submit():
    conn = sq.connect("register.db")
    print("connection established")

    curr =conn.cursor()
    # global name1,roll1,age1,clas1,marks1
    name1 = name.get()
    
    roll1 = roll.get()
    age1 = age.get()
    clas1 = clas.get()
    marks1 = marks.get()
    curr.execute('INSERT INTO REGISTER(NAME,ROLL,AGE,CLASS,MARKS)VALUES(?,?,?,?,?)',(name1,roll1,age1,clas1,marks1))
    conn.commit()
    print("query updated")


def clear():
    
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)


def show():
    win = Tk()
    win.title("Reg DB")

    # win.geometry("700x350")
    s = ttk.Style()
    s.theme_use('clam')
    
    tree = ttk.Treeview(win, column=(win,"c1", "c2", "c3","c4","c5"), show='headings', height=5)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="NAME")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="ROLL")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="AGE")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="CLASS")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="MARKS")

    data = conn.execute('SELECT * FROM REGISTER');
    for col in data:
        tree.insert('', 'end', text="1", values=(col[0], col[1], col[2],col[3],col[4]))
    # for col in data:
    #     print("ID=",col[0],end="")
    #     print("NAME=",col[1],end="")
    #     print("AGE=",col[2],end="")
    #     print("ADDRESS=",col[3],end="")
    #     print("SALARY=",col[4],end="")
    tree.pack()
   
def update():
    conn = sq.connect("register.db")
    print("connection established")

    curr =conn.cursor()
    name1 = name.get()
    roll1 = roll.get()
    age1 = age.get()
    clas1 = clas.get()
    marks1 = marks.get()
    sroll1 = sroll.get()
    # print(sroll1)
    ab = (name1,roll1,age1,clas1,marks1,sroll1)
    print(ab)
    
    # update = 'UPDATE REGISTER SET NAME=%s WHERE ROLL=%s'%(ab)
    # row=curr.execute("SELECT * FROM REGISTER WHERE ROLL=%s",ab)
    # curr.execute("UPDATE REGISTER set NAME=%s,AGE=%s,CLASS=%s,MARKS=%s WHERE ROLL=%s",(ab))
    curr.execute("UPDATE REGISTER set NAME='{}',AGE={},CLASS='{}',MARKS={} WHERE ROLL={}".format(name1,age1,clas1,marks1,sroll1));
    
    conn.commit()
    print("New value updated...")
    # s = row.fetchone() # row details as tuple
    
    # curr.execute('UPDATE REGISTER set NAME=Nisha WHERE ROLL=%s',e6);
    

def delete():
    sroll1 = sroll.get()
    curr.execute("DELETE FROM REGISTER WHERE ROLL={} ".format(sroll1));
    conn.commit()
    print("Entry Deleted")
   
def find():

    
    sroll1 = sroll.get()
    data = conn.execute('SELECT * FROM REGISTER');
    for col in data:
        if col[1]==sroll1:
            print(col)
            e1.insert(0,col[0])
            e2.insert(0,col[1])
            e3.insert(0,col[2])
            e4.insert(0,col[3])
            e5.insert(0,col[4])
            

# ---------text fields---------

l1 = Label(root, text="Name:", font=2)
e1 = Entry(root, font=2,textvariable=name)

l2 = Label(root, text="Roll:", font=2)
e2 = Entry(root, font=2,textvariable=roll)

l3 = Label(root, text="Age:", font=2)
e3 = Entry(root, font=2,textvariable=age)

l4 = Label(root, text="Stream:", font=2)
e4 = Entry(root, font=2,textvariable=clas)

l5 = Label(root, text="Marks:", font=2)
e5 = Entry(root, font=2,textvariable=marks)

l6 = Label(root,text="Select Roll No:", font=2)
e6 = ttk.Combobox(root,values=rollList,textvariable=sroll)




l1.grid(row=1, column=1)
e1.grid(row=1, column=2)


l2.grid(row=2, column=1)
e2.grid(row=2, column=2)

l3.grid(row=3, column=1)
e3.grid(row=3, column=2)

l4.grid(row=4, column=1)
e4.grid(row=4, column=2)

l5.grid(row=5, column=1)
e5.grid(row=5, column=2)

l6.grid(row=6, column=1)
e6.grid(row=6, column=2)


# ----add button--
button1 = Button(root, text=' Add ', fg='black', bg='red',
                    command=lambda:submit(), height=1, width=7)
button1.grid(row=1,column=3)
# ------clear button----
button2 = Button(root, text=' Clear ', fg='black', bg='red',
                    command=lambda:clear(), height=1, width=7)
button2.grid(row=1,column=4)
#--------exit button----
button3 = Button(root, text=' exit ', fg='black', bg='red',
                    command=lambda:root.destroy(), height=1, width=7)
button3.grid(row=1,column=5)
#-------show db button-----
button4 = Button(root, text=' show DB ', fg='black', bg='red',
                    command=lambda:show(), height=1, width=7)
button4.grid(row=2,column=4)
#-------update button------
button5 = Button(root, text=' Update ', fg='black', bg='red',
                    command=lambda:update(), height=1, width=7)
button5.grid(row=6,column=3)
#-------Delete Entry-------
button6 = Button(root, text=' Delete ', fg='black', bg='red',
                    command=lambda:delete(), height=1, width=7)
button6.grid(row=6,column=4)
#--------find entry--------
button7 = Button(root, text=' Find ', fg='black', bg='red',
                    command=lambda:find(), height=1, width=7)
button7.grid(row=6,column=5)




root.mainloop()
