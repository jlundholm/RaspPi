# ESP4T
# 07/05/2018
# Learn Fractions GUI Version
# Compare two fractions or decimal numbers


import tkinter as tk #Need tkinter for guis
from fractions import Fraction #Need this for fractions
import random


class Compare:
    def __init__(self, root):
        self.root = root
        self.root.title("Learn Fractions")
                
        #Keep track of scores
        self.score = 0
        
        self.setup_interface()
    
    #Set up graphical user interface
    def setup_interface(self):
        s_width = self.root.winfo_screenwidth() # get screen width and height
        s_height = self.root.winfo_screenheight()
        
        #Width and height of window
        w_width = 800
        w_height = 500
        
        #Set up window width, height, x and y positions
        self.root.geometry("{0}x{1}+{2}+{3}".format(w_width, w_height,
                                s_width//2 - w_width//2, s_height//2 - w_height//2))
         
        #Labels to show numbers to compare
        self.number1_label = tk.Label(self.root, text="Number1", height=10, width=20,
                           font=("Helvetica", 16), bg="orange")
        self.number1_label.grid(row=0, column=0, rowspan=3, sticky="nsew")
        
        self.number2_label = tk.Label(self.root, text="Number2", height=10, width=20,
                           font=("Helvetica", 16), bg="purple")
        self.number2_label.grid(row=0, column=2, rowspan=3, sticky="nsew")
        
        
        #Comparison buttons (less, equal, greater)
        button_height = 1
        self.less = tk.Button(self.root, bg="white", text="<", height=button_height, width=20,
                              command=lambda: self.check("less"))
        self.less.grid(row=0, column=1, sticky="nsew")
        
        self.equal = tk.Button(self.root, bg="white", text="=", height=button_height, width=20,
                               command=lambda: self.check("equal"))
        self.equal.grid(row=1, column=1, sticky="nsew")
        
        self.greater = tk.Button(self.root, bg="white", text=">", height=button_height, width=20,
                                 command=lambda: self.check("greater"))
        self.greater.grid(row=2, column=1, sticky="nsew")
        
        message = "Score = " + str(self.score)
        self.track_score = tk.Label(self.root, text=message, height=1, width=10,
                           font=("Helvetica", 10), bg="green")
        self.track_score.place(relx=0.8, rely=0.0, anchor="nw")
        
        #Need this to make windows resizable
        self.root.grid_columnconfigure(0, weight=1, uniform="group1")
        self.root.grid_columnconfigure(1, weight=1, uniform="group2")
        self.root.grid_columnconfigure(2, weight=1, uniform="group3")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
    
    
    #Check if answer is right
    #Compare two numbers based on actions
    def check(self, action):
        #Blink pressed button and generate new numbers if corect
        if (action == "greater" and self.number1 > self.number2):
            self.blink(action, True)
            
            #Update current score
            self.score += 1
            self.update_score()
            
            generate_numbers(self)
        elif(action == "less" and self.number1 < self.number2):
            self.blink(action, True)
            
            self.score += 1
            self.update_score()
            generate_numbers(self)
        elif(action == "equal" and self.number1 == self.number2):
            self.blink(action, True)
            
            self.score += 1
            self.update_score()
            generate_numbers(self)
        else:
            #Blink pressed button with red
            self.blink(action, False)
    
    
    #Update score label
    def update_score(self):
        message = "Score = " + str(self.score)
        self.track_score.configure(text=message)
    
    #Make button blink red or green depending on correctness
    def blink(self, action, correct):
        wait_time = 500
        if(action == "greater"):
            #if action was greater and it's right, blink green. Red otherwise
            if (correct == True):
                self.greater.configure(state="normal", relief="raised", bg="green")
            else:
                self.greater.configure(state="normal", relief="raised", bg="red")
            self.root.after(wait_time, lambda: self.greater.configure(bg="white"))
        elif(action == "equal"):
            if(correct == True):
                self.equal.configure(state="normal", relief="raised", bg="green")
            else:
                self.equal.configure(state="normal", relief="raised", bg="red")
            self.root.after(wait_time, lambda: self.equal.configure(state="normal", relief="raised", bg="white"))
        elif(action == "less"):
            if(correct == True):
                self.less.configure(state="normal", relief="raised", bg="green")
            else:
                self.less.configure(state="normal", relief="raised", bg="red")
            self.root.after(wait_time, lambda: self.less.configure(bg="white"))
            
    
    
    #Change numbers on labels
    def update_number(self, number1, number2, equal=False):
        #Format number into string
        self.number1 = number1
        self.number2 = number2
        
        #Do print formatting if two numbers are equal
        if (equal == True):
            #Make second number decimal, if first is Fraction
            if type(self.number1) is Fraction:
                num_str1 = str(self.number1.numerator) + "\n" + "-" * int(1.5 * len(str(self.number1.numerator))) + "\n" + str(self.number1.denominator)
                
                #Get remainders for first number when converted into decimal
                result = convert(self.number2)
                
                #Print decimal if it's not repeating decimal number
                if (result == None):
                    num_str2 = str(self.number2.numerator / self.number2.denominator)
                else:
                    #Do some fancy formatting
                    str_result = "".join(map(str, result))
                    num_str2 = " " * len(str(self.number2.numerator//self.number2.denominator)) + "  " + "_" * int(1.2*len(str_result)) + "\n" + str(self.number2.numerator // self.number2.denominator) + "." + str_result                
            else:
                num_str1 = str(self.number1)
                frac = Fraction.from_float(self.number2).limit_denominator()
                num_str2 = str(frac.numerator) + "\n" + "-" * int(1.5*len(str(frac.numerator))) + "\n" + str(frac.denominator)      
        else:
            if type(self.number1) is Fraction:
                num_str1 = str(self.number1.numerator) + "\n" + "-" * int(1.5*len(str(self.number1.numerator))) + "\n" + str(self.number1.denominator)
            elif not(type(self.number1) is Fraction):
                num_str1 = str(self.number1)
                
            if type(self.number2) is Fraction:
                num_str2 = str(self.number2.numerator) + "\n" + "-" * int(1.5*len(str(self.number2.numerator))) + "\n" + str(self.number2.denominator)
            elif not(type(self.number2) is Fraction):
                num_str2 = str(self.number2)
           
        #Show numbers
        self.number1_label.config(text=num_str1)
        self.number2_label.config(text=num_str2)


#Given a Fraction, convert to decimal 
def convert(frac):
    #Create dictionary to store remainders and its position
    remainders = {}        
    result = [] #Store repeating digits        
    rem = frac.numerator % frac.denominator #First remainder
    
    #Keep repeating while rem is not zero and rem is not is dictionary of remainders
    while(rem != 0 and not(rem in remainders.values())):
        #Store remainder in dictionary
        remainders[len(result)] = rem
        
        #Multiply remainder by 10
        rem = rem * 10
        
        #Update result (remainder / denominator)
        result.append(rem // frac.denominator)
        
        #Update remainder
        rem = rem % frac.denominator
        
    #If rem == 0, this means that there is no repeating decimal 
    if rem == 0:
        return None
    else:
        return result


#Return fraction type
def make_fraction(high, less_one=False):
    if less_one == True:
        bottom = random.randint(1, high)
        top = random.randint(0, bottom-1)
    else:
        top = random.randint(1, high)
        if top > 1:
            bottom = random.randint(1, top-1)
        else:
            bottom = random.randint(1, top)
    return Fraction(top, bottom)


#Generates numbers and shows them on window
def generate_numbers(compare):
    #Can generate natural number, float, or fraction
    #0 - fraction
    #1 - float
    
    #List to store two numbers
    numbers = []
    equal = random.randrange(5)
   
    #Define lower and upper bound for numbers
    high = 10
    
    for i in range(2):            
        choice = random.randrange(2)
        
        #Randomly make two numbers equal to each other with different representation
        if (i == 1 and equal == 0):                                
            #If first number is Fraction, make second float and vice versa
            #But store both of them as same type
            #numbers.append(round(number, 1))
            numbers.append(numbers[0])         
        else:
            if (i == 1 and type(numbers[0]) is float):
                #If one number is decimal, second should be fraction
                if numbers[0] < 1:
                    numbers.append(make_fraction(high, True))
                else:
                    numbers.append(make_fraction(high, False))
            elif choice == 0:
                #Make random ints for top and bottom of fraction
                if i == 1 and numbers[0] < 1:
                    #Make fraction less than 1
                    numbers.append(make_fraction(high, True))
                else:
                    numbers.append(make_fraction(high, False))
            elif choice == 1:
                #Make random float and round it to one decimal place
                if i == 1 and numbers[0] < 1:
                    number = random.uniform(0.0, 1.0)
                else:
                    number = random.uniform(0.0, high)
                numbers.append(round(number, 1))
            
    #Update numbers as needed
    if (equal == 0):
        compare.update_number(numbers[0], numbers[1], equal=True)
    else:
        compare.update_number(numbers[0], numbers[1], equal=False)

    

def main():  
    """ Graphical User Interface """
    root = tk.Tk()
    compare = Compare(root)
    
    #Start program
    root.after(1000, generate_numbers(compare))
    
    root.mainloop()
    

if __name__ == '__main__':
    main()
