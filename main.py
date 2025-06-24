from machine import Pin
from machine import I2C
import time
from RGB1602 import RGB1602
from dht import DHT11, InvalidChecksum
 
sensor = DHT11(Pin(2, Pin.OUT, Pin.PULL_DOWN))
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
lcd = RGB1602(2, 16)

def show_r_g_b(lcd):
    #set red color on lcd
    lcd.set_rgb(255, 0, 0)
    time.sleep(2)
    #set green color on lcd
    lcd.set_rgb(0, 255, 0)
    time.sleep(2)
    #reset white color on lcd
    lcd.set_rgb(255, 255, 255)
    time.sleep(2)

def animated_banner(lcd):
    # Show first line for temperature
    for string in "Temperature:{:3.0f}C".format(t):
        lcd.printout(string)
        time.sleep(0.3)
        
          # Show second line for humidity
    lcd.at(1, 1)
    for string in "Humidity:{:3.0f}%".format(h):
        lcd.printout(string)
        time.sleep(0.3) 

while True:
    t, h: float
    t  = (sensor.temperature)
    h = (sensor.humidity)
    lcd.at(0, 0).printout(str(0) + "Temperature:{:3.0f}C".format(t) + str(1))
    lcd.at(2, 1).printout(str(1) + " Humidity: {:3.0f}%".format(h) + str(2))
    
    #time.sleep(1)
    lcd.clear()
    time.sleep(2)
    lcd.clear()
    animated_banner(lcd)
    time.sleep(3)
    show_r_g_b(lcd)
    lcd.clear()
    