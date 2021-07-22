#Code for KeyeStudio Line Tracking Sensor

#KeyeStudio Line Tracking Sensor = Ks0050
#Operating Voltage = +5V
#Operating Current = <10mA
#Operating Temperature Range = 0Celcius - 50Celcius

#Imports LineSensor from GPIOzero library
from gpiozero import LineSensor

#when a line is detected, the led turns on, otherwise it is dim
if __name__ == '__main__':
    #Creates sensor object as an input from pin 12
    sensor = LineSensor(12)
    #if line is detected, prints Line Detected and waits
    sensor.when_line = lambda: print('Line Detected')
    #if line isn't detected, prints No Line Detected and waits
    sensor.when_no_line = lambda: print('No Line Detected')
