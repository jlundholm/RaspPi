# A Python script to display the date and time of the day on the Sense Hat Matrix Display.
#Import the SenseHat Module from the sense_hat library and name it as SenseHat
from sense_hat import SenseHat
#Import the datatime Module and name the object as datetime
from datetime import datetime
# Create an instance or object of the type SenseHat.
# -->
#Set the color in which the time and date will be displayed
# A color of type RGB is created by combining the individual values of Red, Blue and Green
# The individual range for Red, Blue and Green is 0 to 255.
#The time_color represents Blue Color
time_color = (0,0,255)
#The date_color represents Red Color
date_color = (255,0,0)
#Clear the 8x8 LED Matrix
# --> 
if __name__ == '__main__':
    try:
        while True:
            #Obtain the current time and day information by calling the function now on the datetime object
            # -->     
            #Format the curr_datetime for display on the 8x8 LED Matrix
            #%d - Day of the month, %B - Month, %Y - Year
            date_message = '{:%d %B %Y}'.format(curr_datetime)
            #%H - Hour (24-hour clock), %M - Minute, %S - Second
            time_message = '{:%H:%M:%S}'.format(curr_datetime)
            #Display date by calling the show_message function on the object hat.
            # -->
            #Display time by calling the show_message function on the object hat.
            # -->
    except KeyboardInterrupt:
        hat.clear()



