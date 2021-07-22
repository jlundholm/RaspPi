#ESP4T 2021, Fletcher Wadsworth
#Detects a black line on white background using Line Tracking Sensor

#Import line sensor library
from gpiozero import LineSensor
#Create a line sensor object tied to Pin 6


#Main function
if __name__ == '__main__':
    while True:
        #Pause script until line is detected
        sensor.wait_for_line()
        #Print message indicating a line
        
        #Pause script until no line is detected
        
        #Print message indicating no line is detected
        