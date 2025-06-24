from machine import Pin
from machine import I2C
import time
import urequests
from RGB1602 import RGB1602
from dht import DHT11, InvalidChecksum
import network
import socket

ssid = 'VODAFONE_9689' #ssid name
password = '77xte4dprf79e7cr' #wifi password
#ssid = 'Hot_Public' #ssid name
#password = 'Hot2022@' #wifi password


sensor = DHT11(Pin(6, Pin.OUT, Pin.PULL_DOWN))
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
lcd = RGB1602(2, 16)
  
def connect():

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    #while wlan.isconnected() == False:
         #print('waiting for connection...')
         #time.sleep(1)
    max_wait = 10
    while max_wait > 0:
         if wlan.status() < 0 or wlan.status() >= 3:
             #break
             max_wait -= 1
             print('waiting for connection...')
             time.sleep(1)      
             ip = wlan.ifconfig()[0]
             #print ('f connected on {ip}')
         if wlan.status() != 3:
              raise RuntimeError('network connection failed') 
         else:
              print('Connected')
              status = wlan.ifconfig()[0]
              print( 'ip = ' + status )
              t  = (sensor.temperature)
              h = (sensor.humidity)
              print("Tem:{:3.0f}'C Hu:{:3.0f}%".format(t,h))
              time.sleep(0.3)
              for string in "IP:{}".format(status):
                   lcd.printout(string)
                   time.sleep(0.3)
    # Show second line for temperature and humidity
              lcd.at(0, 1)
              for string in "Tem:{:3.0f}C Hu:{:3.0f}%".format(t,h):
                    lcd.printout(string)
                    time.sleep(0.3)
              time.sleep(4)
              lcd.clear()

    return ip

def open_socket(ip):
    address = socket.getaddrinfo('0.0.0.0', 80)#(ip, 80)
    connection = socket.socket()
    #connection.bind(address)
    connection.listen(1)
    return connection

def webpage(t,h):
    t, h: float
    t  = (sensor.temperature)
    h = (sensor.humidity)
    html = """
   <!DOCTYPE html>
   <html>
   <head>
   <title>Pico W Weather Station</title>
   <meta http-equiv="refresh" content="10">
   </head>
   <body> 
   <p{"Tem:{:3.0f}C Hu:{:3.0f}%".format(t,h)}</p> 
   </body>
   </html> 
  """
    return str(html)
def serve(connection):
    while True:
        #try:
            t, h: float
            t  = (sensor.temperature)
            h = (sensor.humidity)
            client = connection.accept()[0]
            request = client.recv(1024)
            request = str(request)
            if wlan.status() < 0 or wlan.status() >= 3:
             #break
             max_wait -= 1
             print('waiting for connection...')
             time.sleep(1)      
             ip = wlan.ifconfig()[0]
             #print ('f connected on {ip}')
             if wlan.status() != 3:
              raise RuntimeError('network connection failed') 
             else:
              print('Connected')
              status = wlan.ifconfig()[0]
              print( 'ip = ' + status )
              t  = (sensor.temperature)
              h = (sensor.humidity)
              print("Tem:{:3.0f}'C Hu:{:3.0f}%".format(t,h))
              time.sleep(0.3)
            html = webpage(t,h)
            client.send(html)
            client.close()
            for string in "IP:{}".format(status):
                   lcd.printout(string)
                   time.sleep(0.3)
    # Show second line for temperature and humidity
            lcd.at(0, 1)
            for string in "Tem:{:3.0f}C Hu:{:3.0f}%".format(t,h):
                    lcd.printout(string)
                    time.sleep(0.3)
              #time.sleep(4)
            lcd.clear()
        
       
try:
    #ip = connect()
    #time.sleep(2)
    #animated_banner(lcd)
    #time.sleep(3)
    #show_r_g_b(lcd)
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
    

    


    

