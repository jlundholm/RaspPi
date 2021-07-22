#Code to read the Digital Output of the MQ-135 gas sensor
#Import sleep module from time library to pause the program
from time import sleep
#Import LED Module and DigitalInputDevice module from gpiozero library
from gpiozero import LED, DigitalInputDevice
#Activating the function that controls the CO2 sensor connected to pin 12
# --> 
#Activating function that controls the white LED connected to pin 21
# --> 
if __name__ == '__main__':
    try:
        while True:
            #Condition when the sensor is active
            if (Sensor.is_active):
                #Display the info
                # --> 
                #Turn on LED
                # -->
            #Condition when the sensor is inactive
            else:
                #Display the info
                # --> 
                #Turn LED off
                # --> 
            #wait 1 second between readings 
            sleep(1) 
    except KeyboardInterrupt:
        #Turn off the LED
        White.off()
        print('Exiting the program')