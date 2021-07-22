#Implementing a Voltage measuring sensor t
#Import a MCP3008 module from the gpiozero library
from gpiozero import MCP3008
from time import sleep

if __name__ == '__main__':
    Voltage = MCP3008(0)
    RawValue = 0
    MAX_RAWVALUE = 1023
    VRef = 3.3
    MeasuredVoltage = 0.0
    while True:
        RawValue = Voltage.raw_value
        MeasuredVoltage = (VRef/MAX_RAWVALUE)*RawValue
        print("Binary Value = {0:d}\tVoltage: {1:.2f}".format(RawValue,MeasuredVoltage))
        print("Binary Value = {0:d}\tVoltage: {1:.2f}".format(RawValue,(VRef*Voltage.value)))
        sleep(1.0)
