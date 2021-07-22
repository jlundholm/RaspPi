#!/usr/bin/env python

# import needed libraries
from SunFounder_Line_Follower import Line_Follower
from picar import front_wheels
from picar import back_wheels
import time
import picar
from calibrate_5_sensors import cali
from keyboard_press_nowait import keypress
import sys
import pynput
from pynput import keyboard

# update the REFERENCES after the robot is calibrated at least once
# to calibrate the robot set, place front 5 sensors over a black line (electrical tape)
# then the robot will drive forward and calibrate form the surface around the line (preferably white)
# copy and paste the values printed in the shell intmo the REFERENCES variable
REFERENCES = [27.0, 20.5, 23.5, 20.0, 20.5]
calibrate = False # set this to True to calibrate
forward_speed = 80 # set the forward speed
backward_speed = 20 # set the backwards speed
outer_angle = 20 # set the angle at which the robot turns
inner_angle = 42 # set the angle at which the robot turn
delay = 0.0005 # how long the robot waits before running through the program
# delay is needed for the sensors so don't change it

# setup for the robot
picar.setup()
keyp = keypress()
front_w = front_wheels.Front_Wheels(db='config')
back_w = back_wheels.Back_Wheels(db='config')
line_follower = Line_Follower.Line_Follower()
line_follower.references = REFERENCES
front_w.ready()
back_w.ready()

front_w.turning_max = 45 # max turning angle for the robot
straight = 90 # the set angle for when the robot goes straight

# setup calibrates the sensors if calibrate is set to true
def setup():
    if calibrate:
        line_follower.references = cali() #set references to the values recieved by calibrate

# main loop that controls the line following program
''' make a main function '''
    global turning_angle
#     print("references:",line_follower.references)
    back_w.speed = forward_speed
    keyp.run()
    
    i = 0 # initialize counter value
    back_w.forward()
    while True:
        lt_status_now = line_follower.read_digital() # reads the five front sensor values
        pin0 = lt_status_now[0] # sets the values of a sensor to a variable for use later
        pin1 = lt_status_now[1]
        pin2 = lt_status_now[2]
        pin3 = lt_status_now[3]
        ''' set up pin 4 '''
        
        if(i%20 == 0): # only print sensor values every 20th value
            print(lt_status_now,i)
        i += 1
        
        # Angle calculations
        # set right turn angle
        if pin1 is 1:
            turning_angle = straight + inner_angle
        elif pin0 is 1:
            ''' turn right with outer_angle '''
        # set left turn angle
        elif pin3 is 1:
            ''' turn left with inner_angle '''
        elif pin4 is 1:
            ''' turn left with outer_angle '''
        elif pin2 is 1:
            time.sleep(0.001)
        # set straight turn angle
        else:
            ''' turn straight '''

        # turn by previously set angle
        front_w.turn(turning_angle)
        time.sleep(delay)
        
        # save the key pressed by a user
        key_pressed = keyp.get_key()
        #if escape is pressed the car is stopped and the program is exited
        if(key_pressed is 'esc'):
            print('You pressed esc. Terminating program.')
            back_w.stop()
            sys.exit()
        elif(key_pressed is 'ctrl_r'):
            ''' stop the car '''
        elif(key_pressed is 'up'):
            back_w.speed = forward_speed
            back_w.forward()
# run the main loop
if __name__ == '__main__':
    try:
        while True:
            setup()
            ''' run the main funciton '''
    except KeyboardInterrupt:
        ''' stop the car '''

