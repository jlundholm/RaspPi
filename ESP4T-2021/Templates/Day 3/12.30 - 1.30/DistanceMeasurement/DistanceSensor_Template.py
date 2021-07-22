#Program to demonstrate measuring distance using Ultrasonic Sensor
#Key Studio SR01 UltraSonic Sensor = Ks0206
#Distance Range: 2 centimeters - 2 meters

#Import DistanceSensor from the GPIOzero library

#Imports sleep from the time library
from time import sleep

if __name__ == "__main__":
    """Create a Distance Sensor object with
            echo input pin connected to pin 12,
            and trigger output pin connected to pin 16"""
     
    try:
        while(True): #creates an infinite time loop
            """Measure the distance from a physical object capable of
                reflecting the sound wave"""
            
            #Display the measured distance in centimeters
            
            #Sleep for a second before measuring again
            sleep(1)
    #allows user to exit the program when ctrl-c is pressed
    except KeyboardInterrupt: 
        print("All Done") #tells user the program is all done   
