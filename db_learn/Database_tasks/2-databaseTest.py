import sqlite3
import time

conn=sqlite3.connect('turorial.db')
print("Database Connected/Created Bro")
c=conn.cursor()
time.sleep(1)

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS table1 (id integer NOT NULL PRIMARY KEY AUTOINCREMENT,date text,value real)")
    print("Table Created")
    watch_table()

def data_entry():
    c.execute("INSERT INTO table1 (date,value) VALUES ('2012-03-06',39)") #id is auto_incremented,hence not entered here
    conn.commit()
    print("Data Entered & Here is the Updated Table")
    time.sleep(1)
    watch_table()

def watch_table():
    #c.execute("PRAGMA table_info(table1)")
    #info=c.fetchall()
    c.execute("SELECT * from table1")  #Just to get Column Names first!
    info=next(zip(*c.description))  #To get list of Column Names of Table || Guess What? It took me 2 hours to get this NAME(only) code
    print(info)
    time.sleep(1)
    
    c.execute("SELECT * FROM table1")
    data=c.fetchall()
    #print(data)    #To Watch whole Table in single line
    for row in data:
        print(row)
    c.close()
    conn.close()
    print("Connection Closed")
    
def update_table():
    c.execute("UPDATE table1 SET value=92 WHERE id=1")
    conn.commit()  #Always Commit whenever changing AnyThing in Table
    print("Data Updated in Table")
    watch_table()

def delete_data():
    c.execute("DELETE FROM table1 WHERE id=5")
    conn.commit()
    print("Data Deleted")
    watch_table()
    
#Un_Comment the BELOW Functions as per the need ! :D

#create_table()
#data_entry()
update_table()
#delete_data()
#watch_table()
    
#**********************************************#
"""
** Hey, Make Sure to CLOSE Connection & Cursor only once
    & that too at the end of Program c/conn.close()
 
** If you are using more than One functions at a Time
    make sure to remove/comment the c/conn.close()
    in every function except the last one to be executed.

"""
