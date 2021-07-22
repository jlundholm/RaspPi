#noisemeter module using MCP3008 and Analog Sound sensor

#IMPORT SLEEP FROM TIME
from timE

from gpiozero import MCP3008 #import MCP3008 from gpiozero
from gpiozero import LED #import LED from gpiozero

sound = MCP3008(channel=0,device=0) #define the object sound for the sound measurement
led1 = LED(23) #declare the white LED

#DECLARE LED2(24), LED3(25), AND LED4(12) LIKE LED1




smoothing = .9 #smoothing value
AvgVol = 0 #set average volume to zero initially

print("Reading Sound Sensor Values")

try:
    while True:
        led1.off() #start will all LEDs turned off
        
        #TURN OFF LED2, LED3, AND LED4
        
        
        
        
        raw_value = sound.raw_value #get the raw_value of the sound sensor
        sample = abs(raw_value-380) #convert to quiet volume to a value of zero
        AvgVol = AvgVol*smoothing+((1-smoothing)*sample)
        print(AvgVol) #print the calculated value
        
        if AvgVol < 50: #if the average value is less than 50 turn the first LED on
            led1.on()
        elif AvgVol >= 50 and AvgVol < 150:
            led1.on()
            led2.on()
        elif AvgVol >= 150 and AvgVol < 300:
            led1.on()
            led2.on()
            led3.on()
        else:
            #TURN ON ALL LEDS
            
            
            
            
            
        sleep(1)
except KeyboardInterrupt: #use control C to stop the program
    print("All Done")
