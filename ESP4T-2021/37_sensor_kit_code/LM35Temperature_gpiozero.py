#Import the MCP3008 module from the gpiozero library
from gpiozero import MCP3008
#Import the sleep function from time library
from time import sleep
#Setting up the channel
analog_input = MCP3008(channel=0)
if __name__ == '__main__':
    try:
        while True:
            VRef = 3.3
            MaxValue = 1023
            #Reading the analog value
            reading = analog_input.raw_value
            #converting the analog reading to the voltage
            voltage = (reading * VRef/MaxValue)
            #converting the voltage to temperature to degree celsius
            temp_c = (voltage)/(10/1000)
            #converting the temperature to degree fahrenheit
            temp_f = (temp_c * 9.0) / 5.0 + 32
            #Displaying the required information
            print("Temp C={:.2f}\tTemp F={:.2f}".format(temp_c, temp_f))
            #pausing the program for 1 second
            sleep(1)
    except KeyboardInterrupt:
            print('Exit')

