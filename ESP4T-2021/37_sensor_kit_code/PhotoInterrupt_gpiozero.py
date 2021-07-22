#Photo Interrupt module
#Import LED Module from gpiozero library
from gpiozero import LED
#A Module for sleeping the Pi
from time import sleep
#Import DigitalInputDevice Module from gpiozero library
from gpiozero import DigitalInputDevice
if __name__ == '__main__':
    #Activating the function that controls the PhotoInterrupt Sensor connected to pin 17
    sensor = DigitalInputDevice(17)
    #Activating function that controls the red LED connected to pin 12
    Led_Red = LED(12)
    try:
        while True:
        Led_Red.on()
        sensor.wait_for_active()
        print("Signal Detected")
        sensor.wait_for_inactive()
        Led_red.toggle()
        print("Not detected")
    except KeyboardInterrupt:
           print("Cleaning up")
           io.cleanup()


