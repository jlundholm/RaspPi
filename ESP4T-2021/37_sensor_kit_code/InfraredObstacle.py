#Code for KeyeStudio Infrared Obstacle Avoidance Sensor

#KeyeStudio Infrared Obstacle Avoidance Sensor = Ks0051
#Operating Voltage = 3.3V - 5V
#Operating Current = >20mA
#Operating Temperature Range = -10Celcius - +50Celcius
#Detection Distance = 2-40cm
#IO Interface = 4 pin

#Imports LED and LineSensor from GPIOzero library
from gpiozero import LED, LineSensor
#Imports pause from the signal library
from signal import pause
#Imports GPIo from the RPi.GPIO library
import RPi.GPIO as GPIO
#Imports sleep from time library
from time import sleep

#Sets mode of the GPIO as BCM
GPIO.setmode(GPIO.BCM)
#Sets the internal resistor type of the device as Pull Down
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#Sets the LED output as pin 21
engageSensor = LED(21)
#Turns on the infrared sensor
engageSensor.on()

try:
    while(True): #Starts an infinite loop
        output = GPIO.input(20) #Creates object with input from pin 20
        if(output != 1): #if statement checking whether the variable in
                         #output has changed from 1 to 0
            print("Object Ahead!") #prints message saying infrared object detected
            sleep(1)
except KeyboardInterrupt: #allows user to exit the program
    print("All Done") #tells user the program is all done