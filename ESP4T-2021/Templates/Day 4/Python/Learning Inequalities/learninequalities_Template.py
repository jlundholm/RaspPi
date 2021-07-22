# Learn Inequalities module
# Compare fractions and floating point numbers

from fractions import Fraction
import random

if __name__ == '__main__':
    print("Learn Fractions")
    print("Indicate if the first number is greater than or less than or equal to the second number using '<', '>', or '='")
    print("Press Ctrl+C to exit game")
    
    #SET SCORE TO ZERO

    correct = True #Boolean to indicate correctness
    
    while True: #Main loop
        try: #Need try loop so we can use except at the end
            if(correct): #Generate two numbers if previous answer is correct
                high = 10 #Define upper bound for numbers
                
                #Randomly select whether number is float or fraction: 0 = float, 1 = fraction
                float_fraction = random.randint(0, 1)
                
                if(float_fraction == 0): #For float
                    #Using uniform distribution, generate a floating point number between 0.0 and high
                    number1 = random.uniform(0.0, high)
                    number1 = round(number1, 1) #Round it to 1 decimal place
                    
                else: #For fraction
                    #Generate two random integers using randint function from random library
                    bottom = random.randint(1, high)
                    top = random.randint(0, high)
                    #Using the two integers generated above, make a fraction
                    number1 = Fraction(top, bottom)
                    
                #REPEAT THE SAME CODE AS ABOVE.
                
                
                
            print(number1, " and ", number2) #Print the two numbers
            answer = input("Answer: ") #Ask user for answer
            
            #Check if user's answer is right
            if(answer == ">" and number1 > number2):        
                correct = True
                score += 1 #Update current score if answer is right
            elif(answer == "<" and number1 < number2):
                #SET CORRECT TO TRUE AND INCREMENT THE SCORE BY ONE.
                
            #Comparisons to check if random numbers are equal
            elif(answer == "=" and (rand_number == 0 or number1 == number2)):
                correct = True
                score += 1 #Update current score if answer is right
            else:
                correct = False
                print("Answer is wrong!")
                
            if(score == 10):
                print("Congrats you won!")
                break
            
            print() #Adds a break in the output        
        except KeyboardInterrupt:
            break
    
    print("\nYour score is " + str(score))

