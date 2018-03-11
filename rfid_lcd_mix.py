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

#   LCD Library
import Adafruit_CharLCD as LCD

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