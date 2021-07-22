#Blinking Multiple LEDs on the Traffic Light Sensor
#Import a Traffic Light Module from gpiozero library

from time import sleep

if __name__ == '__main__':
    #Define Traffic Light Connections
    Red = 12
    Amber = 16
    Green = 21
    #Create a Traffic Light Object
    
    #Turn on Green
    
    while True:
        sleep(5)
        #Turn off green and Turn on Amber
        lights.green.off()
        lights.amber.on()
        sleep(2)
        #Turn off Amber and Turn on Red
        
        sleep(5)
        #Turn off Red and Turn on Green
        
    