"""
ESP4T, University of Wyoming
Brady Wagstaff
June, 2019

This program uses the SenseHat to make a marble maze game
in order to add more levels you need to create a new matrix and fill
it in using the number system explained before the first one
Also the two places noted by the #----------------- comments
must be edited with new levels added
the accelerometer on the SenseHat is used in order to control
movement of the ball

1 - White - maze wall, cannot move through, can touch
2 - Red - bomb, can move on top of but will result in death
3 - Blue - starting point of the ball
4 - Green - finishing location

Levels 11 and 12 have multiple frames to complete before finishing
"""


from sense_hat import SenseHat #Import the SenseHat Library
import time  #Import time library
import math  #Import the math library

hat = SenseHat() #creating an object of type SenseHat

white = (150,150,150)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
orange = (255, 85, 0)
off = (0,0,0)

ballx = 0
bally = 0
start = [0,0]
diffCnt = 45

hat.clear() #turn off all SenseHat LEDs

#matrices that are used to draw on whole board
# blank matrix to make new ones easily
blank =[[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]

win = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]

win1 = [[1, 2, 1, 2, 1, 2, 1, 2],
        [2, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 2],
        [2, 1, 2, 1, 2, 1, 2, 1]]

win2 = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 1, 2, 1, 2, 0],
        [0, 2, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 2, 0],
        [0, 2, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 2, 0],
        [0, 2, 1, 2, 1, 2, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]

win3 = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 1, 2, 0, 0],
        [0, 0, 2, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 2, 0, 0],
        [0, 0, 2, 1, 2, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]

win4 = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]


"""The Matrix below signifies the mazes that will be created
    1 = maze wall
    2 = bomb
    3 = start location
    4 = finish location
    """
maze0 =[[3, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4]]

maze1 =[[3, 1, 2, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 2, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 2],
        [0, 0, 1, 1, 0, 1, 0, 0],
        [2, 0, 0, 0, 0, 1, 1, 4]]

maze2 =[[3, 1, 0, 0, 0, 2, 1, 4],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 2, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 1, 2, 0],
        [2, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [2, 0, 0, 0, 0, 0, 0, 2]]

maze3 =[[3, 2, 0, 0, 1, 2, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 0],
        [0, 2, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 2, 2, 0, 0],
        [2, 2, 1, 2, 0, 0, 0, 2],
        [0, 0, 1, 2, 4, 2, 2, 2]]

maze4 =[[3, 1, 2, 0, 0, 0, 2, 2],
        [0, 1, 2, 0, 1, 0, 0, 2],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [2, 0, 1, 2, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 2, 0, 1, 2, 0, 2],
        [0, 1, 0, 0, 1, 2, 0, 0],
        [0, 0, 0, 1, 4, 0, 0, 2]]

maze5 =[[3, 2, 4, 0, 0, 0, 0, 0],
        [0, 1, 2, 1, 2, 2, 2, 0],
        [0, 2, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 2, 0, 2, 2, 1],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 2, 1, 2, 1, 0],
        [0, 0, 0, 2, 0, 0, 0, 0],
        [2, 2, 0, 0, 0, 1, 2, 2]]

maze6 =[[2, 2, 2, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 2, 0],
        [0, 1, 0, 2, 0, 2, 0, 0],
        [0, 2, 3, 2, 4, 1, 0, 2],
        [0, 0, 1, 0, 2, 1, 0, 0],
        [2, 0, 2, 0, 0, 0, 2, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [2, 0, 0, 0, 2, 2, 0, 2]]

maze7 =[[0, 0, 0, 0, 0, 0, 2, 1],
        [0, 2, 2, 2, 2, 0, 0, 0],
        [0, 0, 1, 0, 2, 1, 1, 0],
        [2, 0, 2, 0, 1, 4, 2, 0],
        [3, 0, 2, 0, 1, 0, 2, 0],
        [2, 0, 2, 0, 1, 0, 1, 0],
        [2, 0, 0, 0, 2, 0, 0, 0],
        [1, 2, 1, 0, 2, 0, 2, 0]]

maze8 =[[3, 0, 0, 0, 0, 0, 0, 0],
        [1, 2, 0, 1, 2, 2, 2, 0],
        [4, 0, 2, 0, 0, 0, 0, 0],
        [2, 0, 2, 0, 1, 2, 0, 2],
        [0, 0, 2, 0, 0, 0, 1, 1],
        [0, 2, 2, 1, 2, 0, 0, 2],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [2, 2, 2, 2, 0, 0, 0, 2]]

maze9 =[[3, 0, 2, 0, 2, 0, 2, 2],
        [0, 0, 0, 0, 0, 2, 0, 2],
        [2, 0, 2, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2],
        [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 2, 0, 2, 0],
        [2, 0, 0, 2, 0, 0, 0, 4]]

maze10=[[3, 0, 0, 2, 0, 2, 0, 2],
        [0, 2, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 2, 0],
        [2, 0, 2, 0, 0, 0, 2, 0],
        [0, 0, 0, 2, 0, 2, 0, 0],
        [0, 2, 2, 0, 0, 2, 0, 2],
        [0, 0, 0, 0, 0, 2, 0, 0],
        [2, 0, 0, 0, 2, 0, 2, 4]]

maze11=[[4, 2, 0, 2, 0, 0, 0, 2],
        [0, 0, 2, 0, 0, 2, 0, 0],
        [2, 0, 2, 0, 2, 0, 0, 2],
        [0, 0, 2, 0, 2, 0, 0, 2],
        [0, 2, 3, 0, 0, 2, 0, 0],
        [0, 0, 2, 0, 2, 0, 2, 0],
        [2, 0, 0, 2, 0, 0, 0, 0],
        [2, 2, 0, 0, 0, 2, 0, 2]]

maze11_2 = [[3, 2, 0, 0, 0, 0, 0, 2],
            [0, 0, 2, 0, 2, 2, 0, 0],
            [2, 0, 2, 0, 0, 0, 2, 0],
            [0, 0, 2, 2, 0, 2, 0, 0],
            [0, 2, 0, 0, 0, 2, 0, 2],
            [0, 2, 4, 2, 2, 2, 0, 0],
            [0, 0, 2, 0, 0, 0, 2, 0],
            [2, 0, 0, 0, 2, 0, 0, 0]]

maze12=[[0, 0, 0, 2, 0, 2, 0, 4],
        [0, 2, 0, 0, 2, 0, 0, 2],
        [0, 0, 2, 0, 2, 2, 0, 0],
        [2, 0, 2, 0, 2, 0, 0, 2],
        [0, 0, 2, 0, 0, 0, 2, 0],
        [0, 2, 0, 0, 2, 2, 2, 0],
        [0, 0, 2, 2, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 2, 0, 3]]

maze12_2 = [[3, 2, 0, 0, 2, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 0],
            [2, 0, 2, 2, 0, 2, 2, 0],
            [0, 0, 2, 0, 0, 2, 0, 0],
            [0, 2, 0, 0, 2, 0, 0, 2],
            [0, 2, 0, 0, 2, 0, 2, 4],
            [0, 0, 2, 0, 2, 0, 2, 0],
            [2, 0, 0, 0, 2, 0, 0, 0]]

maze12_3 = [[2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 2, 0, 2, 4],
            [0, 2, 0, 0, 2, 0, 0, 2],
            [0, 0, 2, 0, 0, 2, 0, 0],
            [0, 0, 0, 2, 0, 0, 2, 0],
            [3, 2, 0, 2, 0, 2, 2, 0],
            [0, 2, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 0, 0, 2]]

def levelPick():
    """ Function to allow user to pick which level they start on

        Input:  nothing
        Returns:  nothing
    """
    global maze
    choice = input("Choose level 0-12 then press enter:     ")
    if int(choice) == 0:
        maze = maze0
    elif int(choice) == 1:
        maze = maze1
    elif int(choice) == 2:
        maze = maze2
    elif int(choice) == 3:
        maze = maze3
    elif int(choice) == 4:
        maze = maze4
    elif int(choice) == 5:
        maze = maze5
    elif int(choice) == 6:
        maze = maze6
    elif int(choice) == 7:
        maze = maze7
    elif int(choice) == 8:
        maze = maze8
    elif int(choice) == 9:
        maze = maze9
    elif int(choice) == 10:
        maze = maze10
    elif int(choice) == 11:
        maze = maze11
    elif int(choice) == 12:
        maze = maze12
    #------------------------------------------------
    else:
        maze = maze1


def difficultyPick():
    """ Prompts user for difficulty level and assigns sensitivity
    and speed levels to change difficulty of game

    Input:  nothing
    Returns:  int maxdiffCntCnt 
    """
    global diff6
    global threshold
    global delay
    global diffCnt
    
    diff6 = True
    difficulty = input("Choose difficulty 1-6 (6 for masters only):    ")
    if int(difficulty) == 1:
        threshold = .30
        delay = .35
    elif int(difficulty) == 2:
        threshold = .25
        delay = .3
    elif int(difficulty) == 3:
        threshold = .2
        delay = .25
    elif int(difficulty) == 4:
        threshold = .17
        delay = .2
    elif int(difficulty) == 5:
        threshold = .08
        delay = .15
    elif int(difficulty) == 6:
        threshold = .08
        delay = .15
        diff6 = True
        diffCnt = 0
    else:
        #Difficulty settings, smaller is harder
        threshold = .25 #how steep you must tilt board (must be between 0-1)
        delay = .1  #time between movements, (must be >= 0)

def drawMatrix(matrix, color1, color2, color4):
    """ Function designed to draw a matrix onto the SenseHat
        depending on the values in each locatoin and to start
        finish locations.
        
        Inputs:  8x8 matrix, 3 RGB colors
        Returns:  Nothing
    """
    global ballx
    global bally
    
    for x in range(0,8):
        for y in range(0,8):
            
            if matrix[y][x] == 1:
                hat.set_pixel(x,y,color1)
            elif matrix[y][x] == 2:
                if diff6:
                    hat.set_pixel(x,y,color2)
                else:
                    hat.set_pixel(x,y,off)
            elif matrix[y][x] == 3:
                start[0] = x
                start[1] = y
            elif matrix[y][x] == 4:
                hat.set_pixel(y,x,color4)
            if matrix[x][y] == 0 or matrix[x][y] == 3:
                if x == bally and y == ballx:
                    hat.set_pixel(y,x,blue)
                else:
                    hat.set_pixel(y,x,off)
                    
            
def defineStart(matrix):
    """ Function used to redefine the start location
        to make sure ball starts in correct location.
        
        Inputs:  Matrix containing a 3 in the start position
        Returns:  Nothing
    """
    for y in range(0,8):
        for x in range(0,8):
            if matrix[x][y] == 3:
                start[0] = x
                start[1] = y
            
def drawBall():
    """ Draw the ball on  the SenseHat
    
        Inputs:  Nothing
        Returns:  Nothing
    """
    hat.set_pixel(ballx,bally,blue)
    
def moveBall():
    """ Determines if the modules is tilted and moves the ball
        accordingly if there isnt a wall in the way
        
        Inputs:  Nothing
        Returns:  Nothing
        """
    global ballx
    global bally
    
    accel= hat.get_accelerometer_raw()
    # acceleration of gravity is equal to 1
    X = accel['x']
    Y = accel['y']
    # deciding which direction to move the ball if any
    if X > threshold and ballx < 7:
        if maze[bally][ballx + 1] != 1:
            ballx += 1
    
    if X < -threshold and ballx > 0:
        if maze[bally][ballx - 1] != 1:
            ballx -= 1
    
    if Y > threshold and bally < 7:
        if maze[bally + 1][ballx] != 1:
            bally += 1
    
    if Y < -threshold and bally > 0:
        if maze[bally - 1][ballx] != 1:
            bally -= 1
    
def checkFinish():
    """ If you are on the finish marker this function will determine what
        level to move you on to and display the winner animation

        Input:  nothing
        Returns:  nothing
    """
    global maze
    global ballx
    global bally
    if maze[ballx][bally] == 4:
        if maze == maze11 or maze == maze12 or maze == maze12_2:
            time.sleep(1)
        else:
            levelEnd()
            hat.clear()
            
        if maze == maze12_3:
            maze = maze1
            winner()
            print("\nYOU WIN!!")
        #------------------------------------------------
        elif maze == maze12_2:
            maze = maze12_3
            print("\nOn to Stage 3")
        elif maze == maze12:
            maze = maze12_2
            print("\nOn to Stage 2")
        elif maze == maze11_2:
            maze = maze12
            print("\nOn to FINAL MAZE") 
        elif maze == maze11:
            maze = maze11_2
            print("\nStage two")
        elif maze == maze10:
            maze = maze11
        elif maze == maze9:
            print("\nOn to maze 11!")
            maze = maze10
        elif maze == maze8:
            print("\nOn to maze 9!")
            maze = maze9
        elif maze == maze7:
            print("\nOn to maze 8!")
            maze = maze8
        elif maze == maze6:
            print("\nOn to maze 7!")
            maze = maze7
        elif maze == maze5:
            print("\nOn to maze 6!")
            maze = maze6
        elif maze == maze4:
            print("\nOn to maze 5!")
            maze = maze5
        elif maze == maze3:
            print("\nOn to maze 4!")
            maze = maze4
        elif maze == maze2:
            print("\nOn to maze 3!")
            maze = maze3
        elif maze == maze1:
            print("\nOn to maze 2!")
            maze = maze2
        elif maze == maze0:
            maze = maze1
            print("\nPractice Complete on to Stage 1")
        else:
            maze = maze0
        hat.clear()
        defineStart(maze)
        ballx = start[0]
        bally = start[1]
        return True
    else:
        return False
        
def checkBomb(matrix):
    """ Checks to see if the ball is on a bomb and takes the
        necessary steps to reset the level if it is
        
        Inputs: 8x8 matrix
        Returns: nothing
    """
    global ballx
    global bally
    if matrix[bally][ballx] == 2:
        boom(ballx,bally)
        print("Bomb!")
        bally = start[0]
        ballx = start[1]
        return True
    else:
        return False
        
def boom(x,y):
    """ Creates an animation based off of the input bomb
        location to show that you hit the bomb
    
        Input:   two values indicating x,y position of bomb
        Returns:  nothing
    """
    hat.set_pixel(x,y,red)
    if x+1 <= 7: 
        hat.set_pixel(x+1, y, orange)
    if y+1 <= 7:
        hat.set_pixel(x, y+1, orange)
    if x-1 >=0:
        hat.set_pixel(x-1, y, orange)
    if y-1 >=0:
        hat.set_pixel(x, y-1, orange)
    time.sleep(1)
    hat.clear()
    
                
def levelEnd():
    """ Makes a check mark on the SenseHat to
        show you completed a level
        
        Inputs:  Nothing
        Returns:  Nothing
    """
    drawMatrix(win, green,off,off)
    time.sleep(1.5)
    hat.clear()
    
def winner():
    """ Creates an animation to show that you won the game
    
        Input:  nothing
        Returns:  nothing
    """
    hat.clear()
    drawMatr(win1, green, red, off)
    time.sleep(1)
    hat.clear()
    drawMatr(win2, green, red, off)
    time.sleep(1)
    hat.clear()
    drawMatr(win3, green, red, off)
    time.sleep(1)
    hat.clear()
    drawMatr(win4, green, red, off)
    time.sleep(1)
    defMatr(maze)
    
levelPick()
difficultyPick()

ballx = start[0]
bally = start[1]

try:
    while True:
        
        if diffCnt < 40 and diff6 == True:
            diffCnt += 1
        elif diffCnt > 41:
            diff6 = True
        else:
            diff6 = False
        
        drawMatrix(maze, white, red, green)
        
        defineStart(maze)

        drawMatrix(maze,white,red,green)
        
        drawBall()
        
        moveBall()
        
        if checkFinish():
            diff6 = True
            diffCnt = 0
            
        if checkBomb(maze):
            diffCnt = 30
            diff6 = True
        
#Ctrl+C is the keyboard interrupt that will terminate the program
except KeyboardInterrupt: 
    print("Cleaning Up")
    hat.clear()
        