#Code for KeyeStudio Capactive Button
#This module demonstrates the capacitve touch button
#and tells the user how long the button has been held.

#KeyeStudio Capacitive Touch Sensor = Ks0031
#Operating Voltage = 3.3V to 5.0V
#Interface Type =  Digital

#imports Button from GPIOzero library
from gpiozero import Button
#imports sleep from Time Library to add breaks
from time import sleep

#this code reads for how long a capacitive touch button has been touched
if __name__ == "__main__":
    button = Button(17) #declares button as an object to read from pin 17
    pn = 1 #sets variable value as 1
    try:
        while(True): #creates an infinite loop
            button.wait_for_release() #stops the device proceeding until button has been released
            print("The button has been touched for", pn, "seconds") #prints the message in ""
            pn = pn + 1 #increments the variable for how long the button has been pressed
            sleep(1) #forces the device to sleep for 1 second so a button release can be read
    except KeyboardInterrupt: #allows user to exit the program
        print("All Done") #tells user the program is all done