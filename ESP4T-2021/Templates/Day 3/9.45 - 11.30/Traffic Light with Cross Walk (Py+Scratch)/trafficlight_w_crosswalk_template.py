#module for a traffic light with a capacitive touch sensor as a crosswalk -- TEMPLATE CODE

#IMPORT LED FOR THE TRAFFIC LIGHTS FROM THE GPIOZERO LIBRAY
from gpiozero

from gpiozero import DigitalInputDevice #import DigitalInputDevice for the capacitive touch sensor for the cross walk

#IMPORT SLEEP FROM TIME TO CREATE PAUSES IN THE PROGRAM
from time

if __name__ == '__main__': #start main function
    Red = LED(12) #declare the gpio pin for the red led object
    
    #DECLARE THE GPIO PIN FOR THE YELLOW(16) AND GREEN(21) LEDS AS SHOWN ABOVE
    
    
    
    cross_walk = DigitalInputDevice(18) #declare the gpio pin for the touch sensor and create cross_walk object
    
    try:
        while(True): #start loop
            Green.on() #starts with the green led on
            print("Do not walk") #message from the cross walk
            cross_walk.wait_for_active() #the sensor is waiting to sense if it is being touched
            cross_walk.wait_for_inactive() #wait until it's no longer being touches so it has been pressed
            print("Cross walk needed") #message so you know the cross walk has been sensed
            sleep(2) #sleep to pause the program
            Green.off() #green is turned off
            
            #TURN THE YELLOW LED ON AND SLEEP FOR TWO SECONDS BEFORE TURNING IT OFF AGAIN
            
            
            
            
            Red.on() #red is turned on
            print("Walk now") #message from cross walk
            print("5") #begin count down
            sleep(1) #sleep so that is is actually a one second pause
            print("4")
            sleep(1)
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("1")
            sleep(1)
            print("Stop walking!") #message from the cross walk
            
            #TURN THE RED LED OFF AND TURN THE GREEN LED BACK ON
            
            
            
            sleep(1) #a pause in the program and then it starts all over again
    except KeyboardInterrupt: #use control C to stop the outputs
        print ("All Done") #print a statement to show the interrupt went through
            
            
