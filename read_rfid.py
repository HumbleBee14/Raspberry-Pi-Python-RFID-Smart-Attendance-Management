#!/usr/bin/env python

import RPi.GPIO as GPIO
import datetime
import sys
sys.path.insert(1, '/home/pi/MFRC522-python')
import SimpleMFRC522
temp=0
reader = SimpleMFRC522.SimpleMFRC522()
#print("Current Date & Time: "+str(datetime.datetime.now()))
print("Today's Date: "+str(datetime.date.today()))
print("Current Time Now : "+str(datetime.datetime.now().time()))
GPIO.setwarnings(False)
while(1):
    
    try:
            id, text = reader.read()
            
            if temp==id:
                print("Already Scanned Dude,Move On!")
            else:
                print(id)
                print(text)
            temp=id
            time.sleep(3)
    finally:
            GPIO.cleanup()
     
