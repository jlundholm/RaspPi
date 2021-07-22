from picar import front_wheels
from picar import back_wheels
import time
import picar
import RPi.GPIO as GPIO
import sys

# setup configurations for the car
picar.setup()
front_w = front_wheels.Front_Wheels(db='config')
back_w = back_wheels.Back_Wheels(db='config')

speed = 60  # sets how fast the car goes works in a range of 20 - 100
straight = 90  # sets the angle at which the front wheels are straight it may need to be adjusted
turn_angle = 40  # sets the angle at which the car is able to turn
wait_time = 4.3 # how long the car turns for
time_passed = 0 # initialize the amount of time passed
tic = time.time() # initialize tic at current clock time
      
# returns the time difference between each time it is called
def time_change():
    global tic
    toc = tic # update toc to what tic was last
    tic = time.time() # update tic
    time_dif = tic - toc # calculated the difference between tic and toc
    return time_dif

# this loops until escape is pressed
def main():
    while True:
        global time_passed
        back_w.forward()
        ''' set back_w.speed to speed '''
        time_passed += time_change()
        print(time_passed)
        if(time_passed >= 2*wait_time): # reset time_passed
            ''' set time_passed to zero '''
        ''' make an else if statement for if time_passed is greater than or less than wait_time '''
            front_w.turn(straight - turn_angle)
        else: # turn right
            ''' turn front wheels right '''

# run the main loop
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        back_w.stop()
        front_w.turn(straight)
