#Code for KeyeStudio Motion Sensor

#KeyeStudio PIR Motion Sensor = Ks0052
#Input Voltage: 3.3V - 18V
#Working Current = 15 uA
#Working Temperature = -20C - +85C
#Detection Distance = 3-4 meters

#Imports the MotionSensor from the GPIOzero library
from gpiozero import MotionSensor
#Imports sleep from the time library
from time import sleep

if __name__ == "__main__":
    try:
        while(True): #Creates an infinite time loop
            pir = MotionSensor(12) #Sets pir as variable from motionsensor
                                    #to be read as an input from pin 12
            pir.wait_for_motion() #Waits for mo tion to be detected from sensor
            print("Motion Detected") #Lets the user know motion was detected
            exit() #exits the program, must restart every time motion detected
    except KeyboardInterrupt: #allows user to exit the program
        print("All Done") #tells user the program is all done
