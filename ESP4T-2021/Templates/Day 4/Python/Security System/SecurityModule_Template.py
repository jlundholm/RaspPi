#Code for Security System Module

#Componenets of system include:
#KeyeStudio Ultrasonic Ranger
#KeyeStudio PushButton
#KeyeStudio Active Buzzer
#KeyeStudio White LED

#Lines 10-14 import content from the GPIOzero library
from gpiozero import Button
from gpiozero import DistanceSensor
from gpiozero import Buzzer
from time import sleep

if __name__ == "__main__":
    try:
        ##create a sensor object with the echo pin set at 12 and the
        ##trigger pin set at 16
        
        ##create a button object on pin 13
        
        ##create a buzzer with the name Buzzer_Beeper on pin 26
        
        bp = 0 #creates a variable of bp with a value of 0
        button.wait_for_press() #waits for the button to be pressed
        bn = 1 #changes button presses to 1
        if(bn != 0):
            print("The system has been armed.")
            print("You have five seconds to clear the area.")
            sleep(1)
            print("You have four seconds to clear the area.")
            sleep(1)
            print("You have three seconds to clear the area.")
            sleep(1)
            print("You have two seconds to clear the area.")
            sleep(1)
            print("You have one second to clear the area.")
            sleep(1)
            
            ##Write 1 line of code that will create a variable
            ##indi that is the sensors distance
            
            print("The security system is active.")
            while(True): #creates an infinite loop
                
                #Write 1 line that wil create a variable cur
                #that is the current sensors distance
                
                print("The system hasn't been tripped.")
                
                ##Write 1 line of code that compares if indi
                ##and cur are not the same value
                    
                    while(True): #creates an infinite loop
                        print("The system has been tripped!")
                        Buzz_Beeper.on() #turns buzzer on
                        sleep(1) #stays in current state for a second
                        Buzz_Beeper.off() #turns off the buzzer
                        sleep(0.5) #sleeps for half a second
    except KeyboardInterrupt: #allows user to exit the program
        Buzz_Beeper.off() #turns buzzer off if on
        print("Security System Deactivated") #tells user the program is all done
