#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import datetime
import sys
sys.path.insert(1, '/home/pi/MFRC522-python')
import SimpleMFRC522
#SDA ==> Pin 24    GPIO= 8
#SCK ==> Pin 23    GPIO= 11
#MOSI ==> Pin 19   GPIO= 10
#MISO ==> Pin 21   GPIO= 9
#GND ==> Pin 6     GPIO= GND
#RST ==> Pin 22    GPIO= 25
#3.3v ==> Pin 1    GPIO= 3.3V
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
            GPIO.cleanup()
    finally:
            GPIO.cleanup()
     
