#Program to find temperature, pressure and humidity using Sense HAT
#Importing SenseHat module from sense_hat library
from sense_hat import SenseHat
#Import module for sleeping the Pi
from time import sleep
#Initialize the SenseHat object
# -->
if __name__ == '__main__':
    try:
        while True:
                #Get the temperature
                # -->
                #Convert the temperature to Fahrenheit
                t=(t*(9.0/5.0))+32.0
                #Round the temperature to two decimal points
                t=round(t,2)
                #Get the pressure
                # -->
                #Round the pressure to two decimal points
                p=round(p,2)
                #Get the humidity
                # -->
                #Round the humidity to two decimal points
                h=round(h,2)
                #Collectively create a text displaying Temp, Pressure and Humidity
                # -->
                sleep(0.6)
    except KeyboardInterrupt:
        sense.clear()
        print('Exiting the Sense HAT')