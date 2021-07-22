#Code for the KeyeStudio UltraSound Ranger

#KeyeStudio SR01 UltraSonic Sensor = Ks0206
#Working Voltage = DC 5V
#Working Current = 15mA
#Working Frequency = 40 Hz
#Distance Range = 2centimeters - 5meters

#Imports DistanceSensor from the GPIOzero library
from gpiozero import DistanceSensor
#Imports sleep from the time library
from time import sleep

if __name__ == "__main__":
    sensor = DistanceSensor(echo = 12, trigger = 16) #sets echo input as pin 12 and trigger output as pin 16
    try:
        while(True): #creates an infinite time loop
            print('Distance: ', sensor.distance * 100) #outputs the distance found
            sleep(1) #forces the device to sleep for 1 second
    except KeyboardInterrupt: #allows user to exit the program
        print("All Done") #tells user the program is all done   
