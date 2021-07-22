#Import LED Module from gpiozero library
from gpiozero import LED
#Import DigitalInputDevice Module from gpiozero library
from gpiozero import DigitalInputDevice
from time import sleep

if __name__ == '__main__':
    
    #Create Red and Yellow LED Object
    Led_Red = LED(12)
    Led_Yellow = LED(16)
    #Create a Touch Surface Connected to GPIO 18
    touch_srf = DigitalInputDevice(18)
    while(True):
        Led_Red.on()
        touch_srf.wait_for_active()
        print("Button Touched")
        Led_Red.toggle()
        Led_Yellow.on()
        touch_srf.wait_for_inactive()
        print("Button Not Touched")
        Led_Yellow.toggle()
        
        
        
            
        
        
        
        
        