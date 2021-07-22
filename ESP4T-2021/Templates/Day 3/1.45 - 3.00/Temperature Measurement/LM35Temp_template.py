#Import the MCP3008 module from the gpiozero library
from gpiozero import MCP3008
#Import the sleep function from time library
from time import sleep
#Setting up the channel
analog_input = MCP3008(channel=0)
if __name__ == '__main__':
    try:
        while True:
            #Set the voltage reference
            
            MaxValue = 1023
            #Reading the analog value
            
            #converting the analog reading to the voltage
            
            #converting the voltage to temperature to degree celsius
            
            #converting the temperature to degree fahrenheit
            
            #Displaying the required information
            print("Temp C={:.2f}\tTemp F={:.2f}".format(temp_c, temp_f))
            #pausing the program for 1 second
            sleep(1)
    except KeyboardInterrupt:
            print('Exit')