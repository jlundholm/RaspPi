#Code for KeyeStudio Capactive Button
#This module demonstrates the capacitve touch button
#and tells the user how long the button has been held.

#KeyeStudio Capacitive Touch Sensor = Ks0031
#Operating Voltage = 3.3V to 5.0V
#Interface Type =  Digital

#imports Button from GPIOzero library
from gpiozero import Button
#imports sleep from Time Library to add breaks
import time
    
#this code reads for how long a capacitive touch button has been touched
if __name__ == "__main__":
    #DECLARE BUTTON AS AN OBJECT TO READ FROM PIN 17
    
    #CREATE A 'PRESSED' VARIABLE FOR THE TIME THE SENSOR IS PRESSED AND SET TO ZERO TO START
    
    
    try:
        while(True): #creates an infinite loop
            button.wait_for_press() #stops the device proceeding until button has been pressed
            
            while button.is_pressed == True: #enters a loop once the button is pressed
                pressed = pressed + 0.01 #increment the variable pressed by 0.1 seconds to represent the time
                time.sleep(0.01) #sleep the pi for 0.1 seconds

            #STOP THE DEVICE FROM PROCEEDING UNTIL THE BUTTON HAS BEEN RELEASED
            
            print("The button has been touched for ", pressed, " seconds") #prints the message in ""
            
            #RESET THE 'PRESSED' VARIABLE TO ZERO
            
    except KeyboardInterrupt: #allows user to exit the program
        print("All Done") #tells user the program is all done


