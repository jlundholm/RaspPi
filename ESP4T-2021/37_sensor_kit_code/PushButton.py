#Code to read from KeyeStudio Push Button

#KeyeStudio Digital Push Button = Ks0029
#Interface = Digital
#Supply Voltage = 3.3V - 5V
#Simple and Easy to Operate

#Imports Button from GPIOzero library
from gpiozero import Button
#Imports sleep from the time library
from time import sleep

#this code reads for how long a capacitive touch button has been touched
if __name__ == "__main__":
    button = Button(12) #creates variable from button object on pin 12
    pn = 1 #sets a variables value as 1
    try:
        while(True): #creates an infinite loop
            button.wait_for_press() #waits for the button to be pressed
            #Will print out how many times the button has been pressed
            print("The button has been pressed this many times: ", pn)
            pn = pn + 1 #increments pn by 1 to tell how many times the
                        #the button has been pressed
            sleep(1) #waits for 1 second so no switch bounce
    except KeyboardInterrupt: #allows user to exit the program
        print("All Done") #tells user the program is all done