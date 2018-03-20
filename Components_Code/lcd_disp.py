#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
import time
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

lcd.message('Hello\n    Dear')
# Wait 5 seconds

time.sleep(3.0)
lcd.clear()
text=input("Input something to display: ")
lcd.message(text)

# Wait 3 seconds
time.sleep(3.0)
lcd.clear()
lcd.message('Best of\n    Luck')

time.sleep(3.0)
lcd.clear()
