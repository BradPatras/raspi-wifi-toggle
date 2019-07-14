import RPi.GPIO as gpio
import time
import socket
import datetime

relay = 37

gpio.setmode(gpio.BOARD)
gpio.setup(relay, gpio.OUT)

def start():
    setRelayClosed()
    try:
        while True:
            if isInternetConnected() == True:
                print("Internet connection established")
                time.sleep(15)
            else:
                print("Internet connection failed, toggling relay")
                writeLog()
                setRelayOpen()
                time.sleep(20)
                setRelayClosed()
                time.sleep(120)
            
    except KeyboardInterrupt:
        print
        
    finally:
        gpio.cleanup()

def isInternetConnected():
    try:
        socket.create_connection(("www.google.com", 443))
        return True
    except OSError:
        pass
    return False

def setRelayClosed():
    if gpio.input(relay) != gpio.HIGH:
        print("Relay closing circuit")
        gpio.output(relay, gpio.HIGH)

def setRelayOpen():
    if gpio.input(relay) != gpio.LOW:
        print("Relay opening circuit")
        gpio.output(relay, gpio.LOW)
   
def writeLog():
    logFile = open("wifi-toggle.txt", "a")
    nowDate = datetime.datetime.now()
    
    logFile.write("\n")
    logFile.write(nowDate.strftime("%Y-%m-%d %H:%M:%S"))
    
    logFile.close()

start()