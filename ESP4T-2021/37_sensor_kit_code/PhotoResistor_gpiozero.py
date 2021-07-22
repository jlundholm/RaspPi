#Import the MCP3008 module from the gpiozero library
from gpiozero import MCP3008
#Import the sleep function from time library
from time import sleep
#Setting up the channel
analog_input = MCP3008(channel=0)
if __name__ == '__main__':
    try:
        while True:
            Ref = 4500
            MaxValue = 1023
            #Reading the analog value
            reading = analog_input.raw_value
            #converting the analog reading to the voltage
	    voltage = (reading * Ref/MaxValue)
	    #Finding the value of resistance of the photoresistor
            Resistance = 10000*((3.3/voltage)-1)
            #Displaying the required information
            print("Resistance={:.2f}".format(Resistance))
            #pausing the program for 1 second
            sleep(1)
    except KeyboardInterrupt:
            print('Exit')

