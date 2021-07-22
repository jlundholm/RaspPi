#!/usr/bin/env python
from SunFounder_Light_Follower import Light_Follower
from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from picar import front_wheels
from picar import back_wheels
from picar import ADC
import time
import picar
import sys

# setup configurations for the car
ultrasonic = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
picar.setup()
front_w = front_wheels.Front_Wheels(db='config')
back_w = back_wheels.Back_Wheels(db='config')

# parameters for robot
turning_angle = 40 # angle at which robot turns
forward_speed = 70
backward_speed = 60
straight = 90 # angle for when the robot is going straight (~90)
back_distance = 20 # distance for when the robot goes in reverse
turn_distance = 40 # distance for when the robot turns

# set condition based on distances recieved from sonic sensor
def state_sonic():
    distance = ultrasonic.get_distance()
    if 0<=distance<back_distance: # backward
        avoid_flag = 2
    elif back_distance<distance<turn_distance : # turn
        avoid_flag = 1
    else:                       # forward
        avoid_flag = 0
    print('distance = ',distance)
    return avoid_flag

def main():
    while True:
        avoid_flag = state_sonic()
        
        # touch obstruction, back up and turn left
        if avoid_flag is 2: 
            back_w.backward()
            back_w.speed = backward_speed
            front_w.turn(straight - turning_angle)
            print("touch obstruction")
            time.sleep(1) # pi does nothing for 1 sec 

        # near obstruction, turn right
        ''' make an else if checking if avoid_flag is 1 '''
            front_w.turn(straight + turning_angle)
            ''' have the car drive forward '''
            ''' set the speed for the back wheels '''
            print("near obstruction")
            ''' wait for 0.6 seconds '''

        # no obstruction, drive straight
        ''' add an else statement '''
            ''' have the car turn the front wheels straight '''
            ''' have the car drive forward '''
            ''' set the speed for the back wheels '''

# run the main loop
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        ''' stop the car '''
        front_w.turn(straight)
