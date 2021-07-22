#Use a photoresistor and a laser diode to measure hand flicks
import time
from gpiozero import DigitalInputDevice
#Create a digital input device object
pr_pin = DigitalInputDevice(26)

laser_detected = True
count = 0

try:
    input("Press any key to Start")
    #Record start time
    
    #Repeat until 10 handflicks are detected
    while(count < 10):
        while True:
            if (pr_pin.is_active):

                
                break
        time.sleep(0.5)
    #Record end time
    
    #Calculate elapsed time
    ElapsedTime = ((end - start) - (count*0.5))
    SamplesPerSec = float(count)/ElapsedTime
    print("Elapsed Time = {:.2f} secs\t Flicks/sec = {:.2f}".format(ElapsedTime,SamplesPerSec))
    print("Shutting down the program")
except KeyboardInterrupt:
    print("Shutting down the program")
    
