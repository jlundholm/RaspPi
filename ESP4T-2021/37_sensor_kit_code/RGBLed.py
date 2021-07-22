#Dode to use the KeyeStudio RGB LED

#KeyeStudio RGB LED = Ks0032
#Primary Colors = Red, Green, Blue
#Voltage = 5V
#Input = Digital, Active High

#Imports RGBLED from the GPIOzero library
from gpiozero import RGBLED
#Imports sleep from the time library
from time import sleep

if __name__ == '__main__':
    #Selects the GPIO Pins for each LED
    led = RGBLED(12, 16, 21)
    try:
        while(True): #creates an infinite loop
            led.color = (0,1,1) #sets outputs as red on
            print("Red LED is on") #prints what led is on
            sleep(3) #forces the device to sleep for 3 seconds
            led.color = (1,0,1) #sets ouput as green on, turns red off
            print("Green LED is on") #prints what led is on
            sleep(3) #forces the device to sleep for 3 seconds
            led.color = (1,1,0) #sets output as blue on, turns green off
            print("Blue LED is on") #prints what led is on
            sleep(3) #forces the device to sleep for 3 seconds
    except KeyboardInterrupt: #allows user to exit the program
        print("All Done") #tells user the program is all done