# import needed libraries
from picar import front_wheels
from picar import back_wheels
import picar
import RPi.GPIO as GPIO
import sys
from keyboard_press import keypress

# setup configurations for the car
keyp = keypress()
picar.setup()
front_w = front_wheels.Front_Wheels(db='config')
back_w = back_wheels.Back_Wheels(db='config')

speed = 60  # sets how fast the car goes works in a range of 20 - 100
straight = 90  # sets the angle at which the front wheels are straight it may need to be adjusted
turn_angle = 30  # sets the angle at which the car is able to turn

# turn the front wheels straight
front_w.turn(straight)

# this loops until escape is pressed
def main():
    # save the key pressed by a user
    key_pressed = keyp.run()

    # if key_pressed is not an empty string output the string
    if(key_pressed is not None):
        print("output",key_pressed)
    # if up arrow is pressed drive straight forward
    if(key_pressed is 'up'):
        back_w.speed = speed # sets the speed of the back wheels
        back_w.forward() # tells the car to drive forward
        front_w.turn(straight)
    # if down arrow is pressed drive straight backwards
    ''' create an else if statement to check if 'down' is pressed '''
        ''' set the speed '''
        ''' have the car drive backwards instead of forward using backward() '''
        ''' turn straight '''
    # if left arrow is pressed the current speed is maintained but the car turns left    
    elif(key_pressed is 'left'):
        front_w.turn(straight-turn_angle)
    # if right is pressed the current speed is maintained but the car turns right
    ''' create an else if statement to check if 'right' is pressed '''
        ''' tell the car to turn right '''
    
    #if escape is pressed the car is stopped and the program is exited
    elif(key_pressed is 'esc'):
        print('You pressed escape. Terminating program.')
        back_w.stop() # stops the car
        sys.exit()
    # if any other key is pressed stop the car
    elif(key_pressed is not ''):
        ''' have the car stop with stop() '''
     
# run the main loop
if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        back_w.stop( )
        front_w.turn(straight)