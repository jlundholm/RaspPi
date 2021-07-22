#Code for KeyeStudio Digital Tilt Sensor
#This code demonstrates the Tilt Sensor by telling the user
#when the sensor is tilted down vs when it is tilted up.

#KeyeStudio Digital Tilt Sensor = Ks0025
#Operating Voltage = 3.3V - 5.0V
#Interface Type = Digital

#Imports LED and LineSensor from GPIOzero Library
from gpiozero import LED
from gpiozero import LineSensor
#Imports sleep from time library
from time import sleep

if __name__ == '__main__':
    sensor = LineSensor(12) #sets sensor as object to read value from pin 12
    try:
        while(True): #starts an infinite loop
            sensor.when_line = lambda: print("The device is tilting up.") #reads if the device has been tilted
            #if the device has been tilted, an LED one the sensor will light up read
            sensor.when_no_line = lambda: print("The device is tilting down.") #reads if device has been tilted back
            #if the device is tilted down, the LED on the device is very dim
    except KeyboardInterrupt: #allows the user to exit the program with Ctrl C
        print("All Done") #prints out the message
