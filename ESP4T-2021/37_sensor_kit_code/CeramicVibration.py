#Code for KeyeStudio Analog Ceramic Vibration Sensor

#KeyeStudio Analog Piezoelectric Ceramic Vibration Sensor = Ks0272
#Supply Voltage = 3.3V - 5V
#Working Current = <1mA
#Working Temperature Range = -10C - +70C
#Output Signal = Analog Signal

#Imports MCP3008 from GPIOzero library
from gpiozero import MCP3008
#Imports sleep from time library
from time import sleep

#defines variable vib as value from MCP3008
vib = MCP3008(channel = 0, device = 0)

try:
    while(True): #creates infinite time loop
        vibration = 0 #sets value to zero initially
        vibration = vib.raw_value #changes value to the sensor value
        print("The vibration detected is: ", vibration) #prints values
        sleep(1) #forces device to stop for 1 second
except KeyboardInterrupt: #allows user to exit the program
    print("All Done") #tells user the program is all done