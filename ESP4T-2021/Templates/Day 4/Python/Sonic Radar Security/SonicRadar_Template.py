#Code for the sonic radar security scanner module
#Import AngularServo, DistanceSensor, RGBLED, TonalBuzzer from gpiozero library
from gpiozero import AngularServo, DistanceSensor, RGBLED, TonalBuzzer
#Import Tone module to play simple tune from the buzzer
from gpiozero.tones import Tone
#Import time to pause or delay the program
from time import sleep
#Import warnings to ignore warnings 
import warnings
#Import App, Slider, Text, PushButton, warn, info modules from guizero library
from guizero import App,Slider,Text,PushButton, warn, info
#Set the pin for RGBLED, where red is in GPIO 5, green in 6, and blue in 13
led = RGBLED(red = 5, green = 6, blue = 13, initial_value=(1, 1, 1))
#Set the pin for TonalBuzzer in 22
b = TonalBuzzer(22)
#Distance function which returns the distance measured from the ultrasonic sensor
def Distance():
    #Pause the program for a moment
    sleep(0.01)
    #Set the pin for Ultrasonic sensor where echo is in pin 24 and trigger is in pin 18
    # -->
    #Ignore the warnings when echo doesn't receive the input
    warnings.filterwarnings("ignore")
    #Find the distance in cm by multiplying with 100
    # --> 
    #Return the final distance
    return distance
#Function to glow up LED and play the siren sound
def siren():
    #Activate the red color
    led.color = (0, 1, 1)
    #Play the highest frequency that the buzzer supports
    b.play(Tone(frequency=880))
    #Pause the program for a while
    sleep(0.15)
    #Stop the tonal buzzer
    b.stop()
    #Play the medium frequency that the buzzer supports
    b.play(Tone(frequency=440))
    #Pause the program for a while
    sleep(0.15)
    #Stop the tonal buzzer
    b.stop()
    #Pause the program for a while again
    sleep(0.15)
    #Activate the blue color
    led.color = (1, 1, 0)
    #Play the lowest frequency that the buzzer supports
    b.play(Tone(frequency=220))
    #Pause the program for a while again
    sleep(0.15)
    #Stop the tonal buzzer
    b.stop()
    #Pause the program for a while again
    sleep(0.15)
#Function that scnas the environment using Ultrasonic Sensor
def scanner():
    #Deactivate the servo motor for a while
    servo.detach()
    #Read the value returned by the Distance() function
    final = float(Distance())
    #If the distance is less than 15 centimeters
    if (final <= 15.0):
        #Popup a warning with the format (title, message)
        warn("UNAUTHORIZED ENTRY", "Trespasser Detected\nCalling 911 Immediately")
        for i in range (8):
            #Call the siren function inside a loop to run it multiple times
            # --> 
        #Turn off the LED
        led.color = (1, 1, 1)
        #Turn off the buzzer
        # --> 
        #Popup an info with the format (title, message)
        info("CAUGHT","The trespasser has been caught and taken into custody")
    #If the distance is not less than or equal to 15 centimeters
    else:
        #Popup an info with the format (title, message)
        info("NOT FOUND","Seems like no one is there!")
#Function which changes the angle of servo motor when the slider is used
def slide(value):
    #Assign the value from the slider to Pos_DC
    Pos_DC = int(value)
    #Assign the value from Pos_DC to servo.angle
    # -->
#Function which once the top right cross button is clicked (program is closed)
def OnExit():
    print('Stopping the program')
    #Close the servo motor
    servo.close()
    #Turn off the LED
    led.color = (1, 1, 1)
    #Turn off the tonal buzzer
    b.stop()
if __name__ == '__main__':
    #Initialize the servo with AngularServo module with pin connected to GPIO 21
    # --> 
    #Initialize the app with App module
    app = App(title = 'Security Scanner',width = 800,height = 350)
    #Initialize the text, text2 and text3 with Text module 
    text = Text(app, text="SECURITY SCANNER FOR PRIVATE PROPERTY", size=14, font="Arial")
    text2 = Text(app, text="Use the slider to scan the environment to find the trespassers crossing the fence", size=14, font="Arial")
    #Initialize the slider with Slider module
    slider = Slider(app,start = -90,end = 90,command = slide,width = 'fill',height = 50)
    text3 = Text(app, text="Anyone trespassing within 15 cm range will be prosecuted",size=14, font="Arial")
    #Initialize the button with PushButton module 
    button = PushButton(app, text="Click here to scan", command=scanner)
    #Displaying the application created
    # --> 
    #When the application is closed, OnExit() function is called
    app.when_closed = OnExit()
        