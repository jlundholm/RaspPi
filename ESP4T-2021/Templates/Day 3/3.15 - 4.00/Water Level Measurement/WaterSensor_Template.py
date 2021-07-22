#Implementing a Water measuring sensor
#Import a MCP3008 module from the gpiozero library
from gpiozero import MCP3008
from time import sleep

if __name__ == '__main__':
    Water = MCP3008(0)
    RawValue = 0
    MAX_RAWVALUE = 1023
    while True:
         #instantiate water object from
                                   #raw_value that changes RawValue
        print("The water level is ")
         #check if RawValue is below 500
            print("low") #print low
         #check if between 500 & 560      
            print("Medium") #print medium
         #check if between 560 and 570    
            print("High") #print High
        else:
             #print Too High
        
        sleep(1.0)