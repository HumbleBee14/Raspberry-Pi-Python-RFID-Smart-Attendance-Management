#!/usr/bin/env python
import RPi.GPIO as GPIO
import sqlite3
import time
import datetime
import Adafruit_CharLCD as LCD  #LCD Library
import sys
sys.path.insert(1, '/home/pi/MFRC522-python')
import SimpleMFRC522            #RFID Library
#SDA ==> Pin 24    GPIO= 8
#SCK ==> Pin 23    GPIO= 11
#MOSI ==> Pin 19   GPIO= 10
#MISO ==> Pin 21   GPIO= 9
#GND ==> Pin 6     GPIO= GND
#RST ==> Pin 22    GPIO= 25
#3.3v ==> Pin 1    GPIO= 3.3V

from sqlite3 import Error

#import subprocess
#from datetime import date

# Raspberry Pi GPIO-PIN setup
lcd_rs = 5     #PIN=29
lcd_en = 24    #PIN=18
lcd_d4 = 23    #PIN=16
lcd_d5 = 17    #PIN=11
lcd_d6 = 18    #PIN=12
lcd_d7 = 22    #PIN=15
#(RW) goes to the ground GND
lcd_backlight = 2
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
#**************************#
'''
temp=0
reader = SimpleMFRC522.SimpleMFRC522()
#print("Current Date & Time: "+str(datetime.datetime.now()))
print("Today's Date: "+str(datetime.date.today()))
print("Current Time Now : "+str(datetime.datetime.now().time()))
GPIO.setwarnings(False)
while(1):
    
    id, text = reader.read()
    if temp==id:

        print("Already Scanned Dude,Move On!")
        lcd.message('Already Scanned')
        time.sleep(2)
        lcd.clear()
        if temp==783778026390:
            print("STOPPING READER")
            lcd.message("Stopping Reader")
            time.sleep(3)
            lcd.clear()
            for i in range(16):
                print(".",end=" ")
                lcd.message(".")
                time.sleep(0.3)
            lcd.clear()
            break;
    else:
        print(id)
        print(text)
        lcd.message(str(id))
        temp=id
        time.sleep(2)
        lcd.clear()
        if temp==783778026390:
            print("If U Scan this ID again,Reader STOPS")
            lcd.message("SCAN IT AGAIN\nTO STOP READER")
            time.sleep(3)
            lcd.clear()
            
GPIO.cleanup()    #ALways Use it once & usually @ END
#***************************************************************#
'''

#  ................. DATABASE SQLite Functions .................#

print("DATE : "+str(datetime.date.today()))


def connect_db():
    global conn
    global c
    conn=sqlite3.connect('rfid_data.db')
    print("Connected To Database")
    c=conn.cursor()
    time.sleep(1)

def check_id(UID):
    connect_db()
    try:
        c.execute("SELECT * FROM table1 WHERE RFID=?",str(UID))
        person=c.fetchall()
        c.close()
        conn.close()
        return print(person)
        
    except Error as e:
        print(e)
        c.close()
        conn.close()
        print("Connection Closed")
    finally:
        conn.close()
    
        
def create_table():
    connect_db()
    c.execute("CREATE TABLE IF NOT EXISTS table1 (Name text NOT NULL,RFID int NOT NULL PRIMARY KEY,Date text)")
    print("Table Created")
    watch_table()

def data_entry():
    connect_db()
    #Tdate=date.today()
    try:
        name=input("Enter Student Name: ")
        print("Scan RFID Card")
        #GPIO.setwarnings(False)
        reader = SimpleMFRC522.SimpleMFRC522()
        uid, info = reader.read()
        c.execute("INSERT INTO table1 (Name,RFID,Date,Time) VALUES (?,?,date('now'),time('now'))",[name,uid])  #NOTE:  [name] OR (name,)Without the comma, (name) is just a grouped expression, not a tuple, and thus the img string is treated as the input sequence,Which could bring Error without comma.You need to pass a tuple, and it's commas that make tuples, not parentheses.
        conn.commit()
        print("Data Entered & Here is the Updated Table")
        time.sleep(1)
        watch_table()
        GPIO.cleanup()
    except sqlite3.IntegrityError:
        print("RFID Already Assigned To Other")
        GPIO.cleanup()
        c.close()
        conn.close()
    except:
        print("There's some issue in Reading")
        
def watch_table():
    connect_db()
    #c.execute("PRAGMA table_info(table1)")
    #info=c.fetchall()
    c.execute("SELECT * from table1")  #Just to get Column Names first!
    info=next(zip(*c.description))  #To get list of Column Names of Table || Guess What? It took me 2 hours to get this NAME(only) code
    print("   "+info[0]+"   "+info[1]+"    "+info[2]+"        "+info[3]+"   "+info[4])
    time.sleep(1)
    
    c.execute("SELECT * FROM table1")
    data=c.fetchall()
    #print(data)    #To Watch whole Table in single line
    for row in data:
        print(row)
    c.close()
    conn.close()
    print("Connection Closed")
    
def update_table(ID):
    connect_db()
    #for i in range(1,7):
    c.execute("UPDATE table1 SET ATTENDANCE=1,Date=date('now'),Time=time('now') WHERE RFID=?",str(ID))   #Date=date('now')
    conn.commit()  #Always Commit whenever changing AnyThing in Table
    print("Attendance Marked")
    print("Data Updated in Table")
    watch_table()

def delete_data():
    connect_db()
    c.execute("DELETE FROM table1 WHERE RFID=44")
    conn.commit()
    print("Data Deleted")
    watch_table()

def alter_table():
    connect_db()
    c.execute("ALTER TABLE table1 ADD Attendance int DEFAULT 0")   #Adding New Column 'Time'
    print("New Column Added")
    watch_table()
    

def get_attendance(ID):
    connect_db()
    c.execute("SELECT NULL FROM table1 WHERE EXISTS (SELECT * FROM table1 WHERE RFID=?)",str(ID))  #Just to Check if DATA EXISTS or NOT
    status=c.fetchall()  
    
    if status==[]:     # Note: '[]' represents EMPTY set=> Data Doesn't Exists
        print("Data Unavailable")
    else:
        c.execute("SELECT Name FROM table1 WHERE RFID=?",str(ID))
        disp=c.fetchall()
        print(str(disp)+" PRESENT")
    c.close()
    conn.close()
    
#Un_Comment the BELOW Functions as per the need ! :D
    
#create_table()
#data_entry()
#update_table()
#delete_data()
#alter_table()
#watch_table()
#check_id(4)
#get_attendance(4)

#............ EXPERIMENT AREA BELOW ...........#
connect_db()
c.execute("SELECT Name FROM table1 WHERE RFID=6")
for nm in c.fetchall():        # OR To Get Name as a String, Just use c.fetchone() & directly print it
    str =  ''.join(nm)
    print (str)
    

#**********************************************#
"""
** Hey, Make Sure to CLOSE Connection & Cursor only once
    & that too at the end of Program c/conn.close()
 
** If you are using more than One functions at a Time
    make sure to remove/comment the c/conn.close()
    in every function except the last one to be executed.

"""
