
# coding: utf-8

# In[91]:


from tkinter import * #GUI package
import sqlite3 as sq #For tables and database
import datetime
import time

window = Tk()
window.title("Attendance Management System") 
window.geometry('800x600+0+0')
header = Label(window, text="Attendance Database\nManagement System", font=("arial",26,"bold","underline"), fg="steelblue").pack()

Tops = Frame(window,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

Label(window, text = "Made By- ADC",font=("arial",10,"italic"),fg="black").place(x=690,y=10)

con = sq.connect('bharati.db') #dB browser for sqlite needed
c = con.cursor() #SQLite command, to connect to db so 'execute' method can be called


L1 = Label(window, text = "Branch", font=("arial", 18)).place(x=10,y=100)
L2 = Label(window, text = "Name", font=("arial",18)).place(x=10,y=150)
L3 = Label(window, text = "RollNo", font=("arial",18)).place(x=10,y=200)
L4 = Label(window, text = "Division", font=("arial",18)).place(x=10,y=250)
L5 = Label(window, text = "Semester", font=("arial",18)).place(x=10,y=300)
L6 = Label(window, text = "RFID/UID", font=("arial",18)).place(x=10,y=350)


#Create variables for each list
comp = StringVar(window)#For 1st dd
comp.set('----') #Inital placeholder for field

compdiv = StringVar(window)#For 2st dd
compdiv.set('--') #Inital placeholder for field

compsem = StringVar(window)#For 3st dd
compsem.set('--') #Inital placeholder for field

compdb = StringVar(window)#4nd dropdown list
compdb.set('----')

name = StringVar(window)
roll = StringVar(window)
#div = StringVar(window)
#sem = StringVar(window)
uid = StringVar(window)

#Dictionary for drop down list
compound = {'ECE','EE', 'MECH', 'IT','CS','IT','CIVIL','PROD'}
compoundv= {1,2}
compoundsem={1,2,3,4,5,6,7,8}

compd = OptionMenu(window, comp, *compound) #For 1st drop down list -BRANCH
compd.place(x=220,y=105)

compdv = OptionMenu(window, compdiv, *compoundv) #For 1st drop down list -DIVISION
compdv.place(x=220,y=255)

compsm = OptionMenu(window, compsem, *compoundsem) #For 1st drop down list  -SEMESTER
compsm.place(x=220,y=305)

compdbase = OptionMenu(window, compdb, *compound)#For 2nd drop down list  -BRANCH_DB
compdbase.place(x=100,y=500)

#Entry for 'input' in GUI
nameT = Entry(window, textvariable=name)
nameT.place(x=220,y=155)

rollT = Entry(window, textvariable=roll)
rollT.place(x=220,y=205)

#divT = Entry(window, textvariable=div)
#divT.place(x=220,y=255)

#semT = Entry(window, textvariable=sem)
#semT.place(x=220,y=305)

uidT = Entry(window, textvariable=uid)
uidT.place(x=220,y=355)

#get func to isolate the text entered in the entry boxes and submit to database
def get():
        print("You have submitted a record")
        
        c.execute('CREATE TABLE IF NOT EXISTS ' +comp.get()+ ' (Name TEXT, RollNo INTEGER, Div INTEGER, Sem INTEGER,UID INTEGER)') #SQL syntax
        
        #date = datetime.date(int(year.get()),int(month.get()), int(day.get())) #Date in format from 'import datetime'

        #INCLUDE RFID UID READING FUNCTION HERE baby!!
        #c.execute('INSERT INTO ' +comp.get()+ ' (Datestamp, MaxWeight, Reps) VALUES (?, ?, ?)',
        #          (date, weight.get(), reps.get())) #Insert record into database.
        c.execute('INSERT INTO ' +comp.get()+ ' (Name,RollNo,Div,Sem,UID) VALUES (?, ?, ?, ?, ?)',
                  (name.get(),roll.get(),compdiv.get(),compsem.get(),uid.get())) #Insert record into database.
        con.commit()

#Reset fields after submit
        comp.set('----')
        compdiv.set('--')
        compsem.set('--')
        compdb.set('----')
        name.set('')
        roll.set('')
        #div.set('')
        #sem.set('')
        uid.set('')

#Clear boxes when submit button is hit
def clear():
    comp.set('----')
    compdiv.set('--')
    compdb.set('----')   #Branch_Database
    compsem.set('--')
    name.set('')
    roll.set('')
    #div.set('')
    #sem.set('')
    uid.set('')
    
def record():
    c.execute('SELECT * FROM ' +compdb.get()) #Select from which ever compound lift is selected

    frame = Frame(window)
    frame.place(x= 370, y = 150)
    
    Lb = Listbox(frame, height = 15, width = 40,font=("arial", 12)) 
    Lb.pack(side = RIGHT, fill = Y)
    
    scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command = Lb.yview)
    scroll.pack(side =RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set)  
     
    

    Lb.insert(0, '   Name    RollNo  Div  Sem   UID') #first row in listbox
    
    data = c.fetchall() # Gets the data from the table
    
    for row in data:
        Lb.insert(1,row) # Inserts record row by row in list box

    L7 = Label(window, text = '[ '+compdb.get()+' Branch ]', 
               font=("arial", 16)).place(x=500,y=100) # Title of list box, given which compound lift is chosen

    L8 = Label(window, text = "* They are ordered from most recent", 
               font=("arial", 12)).place(x=400,y=450)
    con.commit()

button_1 = Button(window, text="Submit",command=get)
button_1.place(x=100,y=400)

button_2 = Button(window,text= "Clear",command=clear)
button_2.place(x=10,y=400)

button_3 = Button(window,text="Open DB",command=record)
button_3.place(x=10,y=500)


window.mainloop() #mainloop() -> make sure that window stays open

