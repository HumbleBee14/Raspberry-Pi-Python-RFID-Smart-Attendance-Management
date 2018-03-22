from __future__ import print_function
import sqlite3
connection = sqlite3.connect("survey.db")
cursor = connection.cursor()
cursor.execute("create table if not exists scale (long float,lat float);")
cursor.execute("insert into scale values (34.5,56.2);")
cursor.execute("insert into scale values (123.7,86.9);")
cursor.execute("insert into scale values (34.1,122.0);")
cursor.execute("select * from scale;")
i=1
for row in cursor.fetchall():
	print ("Row "+str(i)+": " +str(row))
	i=i+1

cursor.close()
connection.close()
