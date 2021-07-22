#Import sleep object from time library to pause the program
from time import sleep
#Import MCP3008 Object from gpiozero library
from gpiozero import MCP3008 
#Instantiate an object (Abstract Representation) of the MCP3008 ADC
# -->
#Largest Analog Voltage measured at Channel 0
VREF = 3.3
#Largest discrete value measured at Channel 0
MaxVal = 1023
if __name__ == '__main__':
    print("Reading MCP3008 Channel 0 Values")
    try:
        while True:
            #Use the included object function to get the raw value of the ADC
            # -->
            #Convert the read decimal value to its equivalent analog value
            # -->
            #Display the raw value and its equivalent analog value
            print("Raw Value = {:0}\tVoltage = {:.2f}".format(reading,voltage))
            sleep(0.5)
    except KeyboardInterrupt:
        print('Exiting the program')

    
