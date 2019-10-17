import RPi.GPIO as GPIO
import time
import distance_sensor as ultrasound
import lcd.lcddriver 

# Defines maximum depth of container
BOTTLESIZE = 21

def check_empty():
   temp_distance = ultrasound.find_distance()
   if(BOTTLESIZE <= temp_distance):
      lcd_empty()
      return True, BOTTLESIZE
   return False, (BOTTLESIZE - temp_distance)

def lcd_empty():
   print("Please refill the container, it is empty")

def display_lcd():
   print("test")

def refill_action():
   condition, distance = check_empty()
   if(condition == False):
      print(str(distance))

refill_action()
