#Code for KeyeStudio DHT11 Temperature and Humidity Sensor

#KeyeStudio DHT11 Temperature and Humidity Sensor = Ks0034
#Supply voltage = 3.3V
#Temperature Range = 0-50C
#Humidity Range = 20-90%
#Interface = Digital

from time import sleep #Imports sleep from time library
import Adafruit_DHT #Imports Adafruit_DHT library
import board #Imports board library

if __name__ == '__main__':
                 #Sets the input value frjom pin 17
    print("Measuring Temperature and Humidity")
                                    #Create a Temperature and Humidity Sensor Object
    try:
        while True: #creates an infinite loop
                                                                          #creates variables from library
            if humidity is not None and temperature is not None: #if statement testing if values are coming
                                                                 #in from the sensor itself
                print("Temperature = {0:0.1f}C, Humidity = {1:0.1f}%".format(temperature,humidity))
                #prints out the results from the sensor if coming in
            else:
                                           #prints out that the sensor isn't getting any values
            sleep(3) #forces the device to sleep for 3 seconds
    except KeyboardInterrupt: #allows user to exit the program
        print("All Done") #tells user the program is all done