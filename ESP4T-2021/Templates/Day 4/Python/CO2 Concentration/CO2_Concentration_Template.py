#Code to read the Analoge Output of the MQ-135 gas sensor
#Import sleep module from time library to pause the program
from time import sleep
#Import LED Module module from gpiozero library
from gpiozero import LED
#Import MCP3008 Object from gpiozero library
from gpiozero import MCP3008
#Instantiate an object (Abstract Representation) of the MCP3008 ADC
analog_input = MCP3008(channel=0)
#Largest Air Quality level measured by MQ-135 Sensor
REF = 500
#Largest discrete value measured at Channel 0
MaxVal = 1023
if __name__ == '__main__':
    print("Reading MCP3008 Channel 0 Values")
    try:
        while True:
            #Use the included object function to get the raw value of the ADC
            # -->
            #Convert the read decimal value to its equivalent air quality level
            # -->
            #Display the raw value and its equivalent CO2 Level
            print("Raw Value = {:0}\tAir Quality CO2 Level= {:.2f}".format(reading,quality))
            #wait 1 second between readings 
            sleep(1.0)
    except KeyboardInterrupt:
        print('Exiting the program')