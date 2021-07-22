#Code for KeyStudio Analog Temperature Sensor with MCP3008 ADC Chip

#KeyStudio Analog Temperature Sensor = KY-013 Sensor
#Operating Voltage = 5 V
#Temperature measurement range = -55C to 125C / -67F to 257F

from time import sleep #import sleep from time library to be able to add breaks
from gpiozero import MCP3008 #import MCP3008(the ADC converter chip) from the gpiozero library

deg = chr(176)+'F' #for adding the degree symbol and F to the output
#sets up the channel number and SPI chip select device. the device is default 0.
tmp = MCP3008(channel=0, device=0) #define the object tmp for temperature measurements

try:
    while True: #starts loop
        temerature = 0 #declare the temperature variable as zero
        temperature = ((180/1023)*tmp.raw_value)-55 #calculate the temperature from the raw voltage value
        tempF = 0 #declare the tempF variable as zero
        tempF = (1.8*(temperature))+32 #convert into fahrenheit and store as tempF
        
        print('{:.1F}' .format(tempF), deg, 10 * ' ') #print the temperature in fahrenheit and shortens it to one decimal
        sleep(0.1) #force a sleep for 0.1 seconds to slow down the printing so we can see it
except KeyboardInterrupt: #use control C to stop the outputs
    print ("All Done") #print a statement to show the interrupt went through
