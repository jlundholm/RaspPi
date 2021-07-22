#Import sleep object from time library to pause the program
from time import sleep
#Import MCP3008 Object from gpiozero library
from gpiozero import MCP3008
#Import PWMLED object from gpiozero library
#-->
#Instantiate an object (Abstract Representation) of the MCP3008 ADC
analog_input = MCP3008(channel=0)
#Largest Analog Voltage measured at Channel 0
VREF = 3.3
#Largest discrete value measured at Channel 0
MaxVal = 1023
#Instantiate the LED object on the pin 16
#-->
if __name__ == '__main__':
    print("Reading MCP3008 Channel 0 Values")
    try:
        while True:
            #Use the included object function to get the raw value of the ADC"""
            reading = analog_input.raw_value
            #Convert the read decimal value to its equivalent analog value
            voltage = reading*VREF/MaxVal
            #Display the raw value and its equivalent analog value
            print("Raw Value = {:0}\tVoltage = {:.2f}".format(reading,voltage))
            #Convert the voltage value between 0.0 and 1.0 that will vary the LED brightness
            #-->
            #Pause the program for a few miliseconds
            sleep(0.01)
    except KeyboardInterrupt:
        #Turn off the LED
        LED.value = 0.0
        print('Exiting the program')

    
