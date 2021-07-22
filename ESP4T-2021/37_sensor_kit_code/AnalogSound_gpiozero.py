'''
    For finding the relationship between ADC and Decibels,
    we used the following website as a reference:
    https://circuitdigest.com/microcontroller-projects/arduino-sound-level-measurement
'''
#Import the MCP3008 module from the gpiozero library
from gpiozero import MCP3008
#Import the sleep function from time library
from time import sleep
#Setting up the channel
analog_input = MCP3008(channel=0)
reading = 0
if __name__ == '__main__':
    try:
        while True:
            VRef = 3.3
            MaxValue = 1023
            #Reading the analog value
            reading = analog_input.raw_value
            #converting the analog reading to the voltage
            voltage = reading * (VRef/MaxValue)
            #Converting ADC to dB using linear regression.
            #Please refer to the reference website on finding out how the below formula is derived.
            dB = (voltage + 83.2073) / 11.003
            #Displaying the required information
            print("Raw value:{:.2f}\tSound in Decibels:{:.2f}".format(voltage, dB))
            #pausing the program for 1 second
            sleep(1)
    except KeyboardInterrupt:
            print('Exit')

