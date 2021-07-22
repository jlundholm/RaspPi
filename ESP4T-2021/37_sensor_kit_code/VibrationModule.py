#Code to run KeyeStudio Vibration Module. 
#Controlling the intensity of vibration using a potentiometer

#KeyeStudio Vibration Module = Ks0487
#Operating Voltage & Current: 5V DC Max / 35mA
#Max power: .5 W

#Import sleep from the time library
from time import sleep

 #Import PWMLED and MCP3008 Object from gpiozero library
from gpiozero import PWMLED as Haptic, MCP3008 as MCP

#Name analog input channel 0
analog_input = MCP(channel = 0)
#"Haptic" connected to Pin 5 of Pi
Hap = Haptic(5)

if __name__ == "__main__":
 
    while (True):
            #Set the potentiometer output to the haptic input
            Hap.value = analog_input.value
            #Print analog output (0 to 1)
            print("Output Value = {}".format(analog_input.value))
	    #sleep for a tenth of a second
            sleep(.1)
        
