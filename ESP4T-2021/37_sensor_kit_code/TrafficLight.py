#Simulating a Traffic Light behavior
#Import a Traffic Light Module from gpiozero library
from gpiozero import TrafficLights as TL
from time import sleep

if __name__ == '__main__':
    #Define Traffic Light Connections
    Red = 12
    Amber = 16
    Green = 21
    #Create a Traffic Light Object
    lights = TL(Red,Amber,Green)
    lights.green.on() #Turn on Green
    
    try:
        while True:
            lights.green.on() #Turn on Green
            print("Green on, you can go.") #prints message
            sleep(5)
            #Turn off green and Turn on Amber
            lights.green.off()
            lights.amber.on()
            print("Green off, Yellow on.") #prints message
            sleep(2)
            #Turn off Amber and Turn on Red
            lights.amber.off()
            lights.red.on()
            print("Yellow off, Red on.") #prints message
            sleep(5)
            #Turn off Red
            lights.red.off()
    except KeyboardInterrupt: #allows user to exit the program
        print("All Done") #tells user the program is all done
