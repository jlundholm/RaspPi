#Code to turn on KeyeStudio White LED

#KeyeStudio White LED = Ks0016
#Voltage = 3.3V - 5.0V
#LED color = White

#Imports LED from GPIOzero object
from gpiozero import LED
#Imports sleep from time library
from time import sleep

if __name__ == '__main__':
    Led_White = LED(12) #Sets Led_White as ouput signal on pin 12
    try:
        while(True): #Creates an infinite time loop
            Led_White.on() #outputs an on signal to pin 12
            print("White LED is on") #tells the user the led is on
            sleep(4) #forces the device to stay in this setting
            Led_White.off() #quits outputting a signal to pin 12
            print("White LED is off") #tells the user the LED is off
            sleep(2) #keeps the device in this state for 2 seconds
    except KeyboardInterrupt: #allows user to exit the program
        print("All Done") #tells user the program is all done