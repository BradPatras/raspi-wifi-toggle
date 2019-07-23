import RPi.GPIO as gpio
import time
import socket
import datetime

relay = 37

gpio.setmode(gpio.BOARD)
gpio.setup(relay, gpio.OUT)

def start():
    setRelayClosed()
    while True:
        if isInternetConnected() == True:
            time.sleep(15)
        else:
            writeLog()
            setRelayOpen()
            time.sleep(20)
            setRelayClosed()
            time.sleep(240)

def isInternetConnected():
    try:
        socket.create_connection(("www.google.com", 443))
        return True
    except socket.error:
        pass
    return False

def setRelayClosed():
    if gpio.input(relay) != gpio.HIGH:
        gpio.output(relay, gpio.HIGH)

def setRelayOpen():
    if gpio.input(relay) != gpio.LOW:
        gpio.output(relay, gpio.LOW)
   
def writeLog():
    logFile = open("wifi-toggle.txt", "a")
    nowDate = datetime.datetime.now()
    
    logFile.write("\n")
    logFile.write(nowDate.strftime("%Y-%m-%d %H:%M:%S"))
    
    logFile.close()

start()