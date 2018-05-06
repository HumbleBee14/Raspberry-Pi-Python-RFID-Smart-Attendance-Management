
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import * #GUI package
import sqlite3 as sq #For tables and database
import datetime
from sqlite3 import Error
#from PIL import Image, ImageTk

window = tk.Tk()
window.title(" SDMS ") 
window.geometry('800x600+0+0')
window.iconbitmap(r'D:\Education\bvulogoicon.ico')  

#USE GRID to tabulor form
##REFER THIS FOR TABLE using GRID: https://stackoverflow.com/questions/36590476/taking-data-from-a-database-and-putting-into-a-table-in-a-gui
# REFER http://www.mypythonadventure.com/category/tkinter/
  

image1 = tk.PhotoImage(file=r"C:\Users\Chota_Don\Documents\student.gif")  #always use gif image else use PIL to read other formats
panel1 = tk.Label(window, image=image1)
panel1.pack(side='bottom', fill='both', expand='no')
panel1.image = image1


header = Label(window, text="Student Database\nManagement System", font=("arial",26,"bold","underline"), fg="steelblue").pack()

Tops = Frame(window,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

Label(window, text = "Made By- ADC ©",font=("arial",10,"italic"),fg="black").place(x=680,y=580)
Label(window, text = "[BVUCOEP]",font=("arial",14,"bold"),fg="brown").place(x=15,y=15)
Label(window, text = "(◥▶╭╮◀◤)",font=("arial",14,"bold")).place(x=695,y=550)

con = sq.connect('project.db') #dB browser for sqlite needed
c = con.cursor() #SQLite command, to connect to db so 'execute' method can be called


L1 = Label(window, text = "Branch", font=("arial", 18)).place(x=10,y=100)
L2 = Label(window, text = "Name", font=("arial",18)).place(x=10,y=150)
L3 = Label(window, text = "RollNo", font=("arial",18)).place(x=10,y=200)
L4 = Label(window, text = "Division", font=("arial",18)).place(x=10,y=250)
L5 = Label(window, text = "Semester", font=("arial",18)).place(x=10,y=300)
L6 = Label(window, text = "RFID/UID", font=("arial",18)).place(x=10,y=350)
#####################
L9 = Label(window, text = "Branch", font=("arial",10)).place(x=110,y=468)
L10 = Label(window, text = "Sem", font=("arial",10)).place(x=185,y=468)
L11 = Label(window, text = "Div", font=("arial",10)).place(x=250,y=468)
L12 = Label(window, text = "Enter UID", font=("arial",10)).place(x=220,y=520)

#####################
errlabel=StringVar()
errlabel.set("ERROR: Please Enter Correct Data")


#Create variables for each list
comp = StringVar(window)#For 1st dd   - Branch (TOP-MENU)
comp.set('----') #Inital placeholder for field

compdiv = IntVar(window)#For 2st dd - DIVISION
compdiv.set('0') #Inital placeholder for field

compsem = IntVar(window)#For 3st dd  - SEMESTER
compsem.set('0') #Inital placeholder for field
########################FOR DATABASE VIEWING###############
compdb = StringVar(window)#4nd dropdown list   - DB-BRANCH  (BOTTOM-MENU)
compdb.set('----')          #Intializing

compdbsem = IntVar(window)
compdbsem.set('0')

compdbdv = IntVar(window)
compdbdv.set('0')

uid1 = IntVar(window)
uid1.set('0')
###########################################################

name = StringVar(window)
roll = IntVar(window)
#div = IntVar(window)
#sem = IntVar(window)
uid = IntVar(window)

#Dictionary for drop down list
compound = {"CS","IT","EC","EE","ME","CV","PD"}
compoundv= {1,2}
compoundsem={1,2,3,4,5,6,7,8}

compd = OptionMenu(window, comp, *compound) #For 1st drop down list -BRANCH
compd.place(x=180,y=105)

compdv = OptionMenu(window, compdiv, *compoundv) #For 2nd drop down list -DIVISION
compdv.place(x=180,y=255)

compsm = OptionMenu(window, compsem, *compoundsem) #For 3rd drop down list  -SEMESTER
compsm.place(x=180,y=305)

###############################FOR DATABASE VIEWING#######################
compdbase = OptionMenu(window, compdb, *compound)#For 4th drop down list  -BRANCH_DB
compdbase.place(x=100,y=488)

compdbase1 = OptionMenu(window, compdbsem, *compoundsem)#For 4th drop down list  -Semester_DB
compdbase1.place(x=180,y=488)

compdbase2 = OptionMenu(window, compdbdv, *compoundv)#For 4th drop down list  -DIVISION_DB
compdbase2.place(x=240,y=488)

###########################################################################

rl=Spinbox(window, from_=0, to=120, textvariable=roll)
rl.pack()
rl.place(x=180,y=205)

#Entry for 'input' in GUI
nameT = Entry(window,bd=4, textvariable=name)
nameT.place(x=180,y=155)

#rollT = Entry(window,bd=4, textvariable=roll)
#rollT.place(x=220,y=205)

#divT = Entry(window,bd=4, textvariable=div)
#divT.place(x=220,y=255)

#semT = Entry(window,bd=4, textvariable=sem)
#semT.place(x=220,y=305)

uidT = Entry(window,bd=4, textvariable=uid)
uidT.place(x=180,y=355)

############
uidST = Entry(window,bd=4, textvariable=uid1)
uidST.place(x=180,y=542)
#############

#get func to isolate the text entered in the entry boxes and submit to database
def get():
    try:
        #c.execute('CREATE TABLE IF NOT EXISTS student_db (Name TEXT, RollNo INTEGER, Div INTEGER, Sem INTEGER,UID INTEGER)') #SQL syntax
        c.execute('CREATE TABLE IF NOT EXISTS student_db (Name TEXT NOT NULL,RollNo INTEGER NOT NULL UNIQUE,UID INTEGER UNIQUE,BRANCH TEXT CHECK (BRANCH IN("CS","IT","EC","EE","ME","CV","PD")),DIVISION INTEGER CHECK (DIVISION IN(1,2)),SEMESTER INTEGER)')
        #date = datetime.date(int(year.get()),int(month.get()), int(day.get())) #Date in format from 'import datetime'

        #INCLUDE RFID UID READING FUNCTION HERE baby!!
        #c.execute('INSERT INTO ' +comp.get()+ ' (Datestamp, MaxWeight, Reps) VALUES (?, ?, ?)',
        #          (date, weight.get(), reps.get())) #Insert record into database.
        #c.execute('INSERT INTO ' +comp.get()+ ' (Name,RollNo,Div,Sem,UID) VALUES (?, ?, ?, ?, ?)',
        #          (name.get(),roll.get(),compdiv.get(),compsem.get(),uid.get())) #Insert record into database.
        c.execute('INSERT INTO student_db (Name,RollNo,UID,BRANCH,DIVISION,SEMESTER) VALUES (?,?,?,?,?,?)',
                  (name.get(),roll.get(),uid.get(),comp.get(),compdiv.get(),compsem.get())) #Insert record into database.
        con.commit()
        print("You have Submitted Data")
        L12 = Label(window, text = " DATA SUBMITTED ", font=("arial",11)).place(x=50,y=440)
        window.after(4000, clear_label) #Clears Label after 5 seconds
    
    except sq.Error as e:
        print (" ERROR: ENTER CORRECT DATA ")
        #L12 = Label(window, text = "ERROR: Please Enter Correct Data", font=("arial",10)).place(x=50,y=440)
        L12=Label(window,textvariable=errlabel,font=("arial",11)).place(x=50,y=440)
        window.after(4000,clear_label) #Clears Label after 5 seconds
        
    finally:
        #con.close()
      #  print("You have submitted a record")
      #  L11 = Label(window, text = "Div", font=("arial",10)).place(x=250,y=480)
        
#Reset fields after submit
        comp.set('----')  #BRANCH
        compdiv.set('0')
        compsem.set('0')
        name.set('')
        roll.set('0')
        #div.set('')
        #sem.set('')
        uid.set('0')
        #####
        compdb.set('----')   #Branch_Database
        compdbsem.set('0')
        compdbdv.set('0')
        uid1.set('0')

        
def clear_label():
    #Removes TExt/Label
    L12 = Label(window, text="                                                            ", font=("arial",10)).place(x=50,y=440)
    #errlabel.set("")
    
#Clear boxes when submit button is hit
def clear():
    comp.set('----')   #Branch
    compdiv.set('0')
    compsem.set('0')
    name.set('')
    roll.set('0')
    #div.set('')
    #sem.set('')
    uid.set('0')
    ####
    compdb.set('----')   #Branch_Database
    compdbsem.set('0')
    compdbdv.set('0')
    uid1.set('0')
    ####
    
def record():
    #c.execute('SELECT * FROM ' +compdb.get()) #Select from which ever compound lift is selected
    b=compdb.get() #Branch
    s=compdbsem.get()
    d=compdbdv.get()
    c.execute('SELECT * FROM student_db WHERE BRANCH=? AND SEMESTER=? AND DIVISION=?',[b,s,d])
    frame = Frame(window)
    frame.place(x= 370, y = 150)
    
    Lb = Listbox(frame, height = 14, width = 40,font=("arial", 12)) 
    Lb.pack(side = RIGHT, fill = Y)
    
    scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command = Lb.yview)
    scroll.pack(side =RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set)  
     

    Lb.insert(0, '    Name      RollNo        UID      Branch    Div   Sem') #first row in listbox
    
    data = c.fetchall() # Gets the data from the table
    
    for row in data:      
        
        Lb.insert(1,row[0]+"      "+str(row[1])+"      "+str(row[2])+"      "+str(row[3])+"      "+str(row[4])+"      "+str(row[5]))# Inserts record row by row in list box

    L7 = Label(window, text = ' STUDENT DATABASE ', 
               font=("arial", 16)).place(x=450,y=100) # Title of list box, given which compound lift is chosen

    L8 = Label(window, text = "* They are ordered from most recent", 
               font=("arial", 12)).place(x=400,y=430)
    con.commit()
#################################
    
def record1():
    
    sid=uid1.get() #Branch
    c.execute('SELECT * FROM student_db WHERE UID=?',[sid])
    frame = Frame(window)
    frame.place(x= 370, y = 150)
    
    Lb = Listbox(frame, height = 14, width = 40,font=("arial", 12)) 
    Lb.pack(side = RIGHT, fill = Y)
    
    scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command = Lb.yview)
    scroll.pack(side =RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set)  
     

    Lb.insert(0, '    Name      RollNo        UID      Branch    Div   Sem') #first row in listbox
    
    data = c.fetchone() # Gets the data from the table
    
    row=data    
    Lb.insert(1,row[0]+"      "+str(row[1])+"      "+str(row[2])+"      "+str(row[3])+"      "+str(row[4])+"      "+str(row[5]))# Inserts record row by row in list box

    L7 = Label(window, text = ' STUDENT DATABASE ', 
               font=("arial", 16)).place(x=450,y=100) # Title of list box, given which compound lift is chosen

    #L8 = Label(window, text = "* They are ordered from most recent", 
    #           font=("arial", 12)).place(x=400,y=450)
    #con.commit()    
####################################    
    
button_1 = Button(window, text="Submit",fg = "brown",
		 bg = "white",command=get)
button_1.place(x=100,y=400)

button_2 = Button(window,text= "Clear",fg = "brown",
		 bg = "white",command=clear)
button_2.place(x=10,y=400)

button_3 = Button(window,text="Open DB",fg='brown',command=record)
button_3.place(x=10,y=490)

button_4 = Button(window,text="Search Student",fg='dark blue',command=record1)
button_4.place(x=10,y=542)


window.mainloop() #mainloop() -> make sure that window stays open

