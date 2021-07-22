#Code for Speedometer module
#Import warnings to ignore warnings
import warnings
#Import Adafruit_CharLCD library (Adafruit_CharLCD.py)
import Adafruit_CharLCD as LCD
#Import DistanceSensor, LED, OutputDevice from gpiozero library
from gpiozero import DistanceSensor, LED, OutputDevice
#Import time to pause or delay the program
from time import sleep
#LCD display pin setup:
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2
#Initialize the lcd object
lcd = LCD.Adafruit_CharLCD(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns,lcd_rows,lcd_backlight)
if __name__ == '__main__':
    #Ignore the warnings when echo doesn't receive the input
    warnings.filterwarnings("ignore")
    #Set the pin for Ultrasonic sensor where echo is in pin 6 and trigger is in pin 5
    # --> 
    #Set the red LED to pin 4
    # --> 
    #Set the red LED to pin 13
    # --> 
    #Set the vibration module to pin 26
    # --> 
    #Display the message on the LCD screen
    lcd.message('Starting the\nSpeedometer')
    #Pause the program for a while
    sleep(1)
    #Clear the message on the LCD screen
    lcd.clear()
    #Display the message on the LCD screen
    lcd.message('CTRL + X -> Exit')
    #Pause the program for a while
    sleep(1)
    #Clear the message on the LCD screen
    lcd.clear()
    try:
        while True:
            #Find the distance in cm by multiplying with 100
            Distance1 = float(sensor.distance * 100)
            #Time interval of 0.5 seconds
            sleep(0.5)
            #Again, find the next distance in cm by multiplying with 100
            Distance2 = float(sensor.distance*100)
            #Calculate the speed by subtracting two distance and dividing by time interval
            # --> 
            #Display the message on LCD screen
            lcd.message('Speed:')
            #Round the speed to two decimal place and convert it to string for displaying
            lcd.message(str(round(speed,2)))
            #Display the SI unit of speed
            lcd.message(' cm/s')
            #Pause the program for a while
            sleep(0.35)
            #Condition when speed is less than 30.0 cm/s
            if (speed < 30.0):
                #Turn off warning red light
                # -->
                #Turn on safe green light
                # -->
             #Condition when speed is greater than 30.0 cm/s
            else:
                #Turn off safe green light
                green.off()
                #Turn on vibration
                vibration.on()
                #Clear the LCD and display warning message
                lcd.clear()
                lcd.message('LIMIT REACHED!\nREDUCE SPEED')
                #Blinking the warning red LED
                for i in range (4):
                    red.on()
                    sleep(0.2)
                    red.off()
                    sleep(0.2)
                #Clear the LCD
                lcd.clear()
                #Turn off vibration
                vibration.off()
            #Completely turn off vibration
            vibration.off()
            #Clear the screen
            lcd.clear()
    #When CTRL + X is entered
    except KeyboardInterrupt:
        #Turn off everything
        vibration.off()
        lcd.clear()
        red.off()
        green.off()
        print('Exiting')