#Implementing a Water measuring sensor
#Import a MCP3008 module from the gpiozero library
from gpiozero import MCP3008
from time import sleep

if __name__ == '__main__':
    Water = MCP3008(0)
    RawValue = 0
    MAX_RAWVALUE = 1023
    while True:
        RawValue = Water.raw_value
        
        print("The water level is ")
        if RawValue < 500:
            print("low")
        elif 500 < RawValue < 560:           
            print("Medium")
        elif 560 < RawValue < 570:           
            print("High")
        else:
            print("Too high")
        
        sleep(1.0)