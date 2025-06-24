from machine import Pin
from machine import I2C
import time
from RGB1602 import RGB1602
from dht import DHT11, InvalidChecksum
import network
import socket

ssid = 'VODAFONE_9689' #ssid name
password = '77xte4dprf79e7cr' #wifi password

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

sensor = DHT11(Pin(6, Pin.OUT, Pin.PULL_DOWN))
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
lcd = RGB1602(2, 16)

def webpage(t,h):
   t  = (sensor.temperature)
   h = (sensor.humidity) 
  
html = """<!DOCTYPE html>
   <html>
    <head>
    <title>Pico W Weather Station</title>
    </head>
    <body> <h1>Rasberry Pi Pico W Weather Station Server</h1>
    <p style= "font-size:32px;"> Temperature: {t}C </p>
    <p style= "font-size:32px;"> Humidity: {h}% </p>
    </body>
    </html>
"""
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
    
# Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        print('Connected')
        status = wlan.ifconfig()[0]
        print( 'ip = ' + status )
        t  = (sensor.temperature)
        h = (sensor.humidity)
        print("Tem:{:3.0f}'C Hu:{:3.0f}%".format(t,h))
    
    
# Open socket
#addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
#s = socket.socket()
#s.bind(addr)
#s.listen(1)
   
# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
#s.bind(addr)
s.listen(1)
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
    # Show first line for ip server address
    for string in "IP:{}".format(status):
        lcd.printout(string)
        time.sleep(0.3)
        
          # Show second line for temperature and humidity
    lcd.at(0, 1)
    for string in "Tem:{:3.0f}C Hu:{:3.0f}%".format(t,h):
        lcd.printout(string)
        time.sleep(0.3) 
#def webpage(t,h):
  # t  = (sensor.temperature)
  # h = (sensor.humidity) 
  
    #return html
while True:
    t, h: float
    t  = (sensor.temperature)
    h = (sensor.humidity)
    #lcd.at(0, 0).printout(str(0) + "Temperature:{:3.0f}C".format(t) + str(1))
    #lcd.at(2, 1).printout(str(1) + " Humidity: {:3.0f}%".format(h) + str(2))
    #time.sleep(1)

    lcd.clear()
    time.sleep(2)
    lcd.clear()
    animated_banner(lcd)
    time.sleep(3)
    show_r_g_b(lcd)
    lcd.clear()
    time.sleep(2)
    
        #addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        #s = socket.socket()
        #s.bind(addr)
        #s.listen(1)
    # Open socket
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    #s.bind(addr)
    s.listen(1)
    #print('listening on', addr)
    #html= webpage(t,h)
    #print(html)


    


        
   
    



        
    