#Code for KeyStudio Active Buzzer
#This code turns on the Active Buzzer after a second break for
#one second and then turns it off for 3 more seconds.

#KeyeStudio Buzzer Beeper = Ks0018
#Operating Voltage = 3.3V - 5.0V
#Interface Type: Digital

#Imports Buzzer from GPIOzero library
from gpiozero import Buzzer
#Imports sleep from time library
from time import sleep

if __name__ == '__main__':
    #sets Buzz_Beeper as buzzer object on pin 12
    Buzz_Beeper = Buzzer(12)
    try:
        while(True): #infinite loop
            sleep(1) #forces the device to sleep for 1 second
            Buzz_Beeper.on() #turns on the buzzer
            print("Buzzer is on.") #tells user the buzzer is on
            sleep(1) #forces the device to sleep for 1 second
            Buzz_Beeper.off() #turns off the buzzer
            print("Buzzer is off.") #tells user the buzzer is off
            sleep(3) #forces the device to sleep for 3 seconds
    except KeyboardInterrupt: #allows user to exit the program
        print("All Done") #tells user the program is all done