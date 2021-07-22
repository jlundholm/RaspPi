#Module to find the Analog rotation ranging from 0-1023 using ADC
from gpiozero import MCP3008
#Import the sleep function from time library
from time import sleep
#Setting up the channel
analog_input = MCP3008(channel=0)
if __name__ == '__main__':
    try:
        while True:
            #Reading the analog value
            reading = analog_input.raw_value
            #Displaying the required information
            print("Analog Value:{0}".format(reading))
            #pausing the program for 1 second
            sleep(1)
    except KeyboardInterrupt:
            print('Exit')
