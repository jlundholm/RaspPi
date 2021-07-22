#Implementing a pulse measuring sensor t
#Import a MCP3008 module from the gpiozero library
from gpiozero import MCP3008
from time import sleep

if __name__ == '__main__':
    PulseRate = MCP3008(0)
    while True:
        print(PulseRate.raw_value)
        sleep(1.0)