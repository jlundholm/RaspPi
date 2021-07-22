from gpiozero import MCP3008      #GardenBot Version 2 Skeleton Code
from gpiozero import LED          #Updated 5/27/2021
from time import sleep
import Adafruit_DHT
import sys 
import os
import csv
import string
from datetime import datetime, timedelta

def makeDirectory(usbName, local):
    #create a  datetime object representing today
    folderDate = datetime.now()
    #create a string to represent the folder name
    folder = folderDate.strftime("%Y-%m-%d")
    #Variable to increment as we loop through the previous week
    day = 7
    #initialize a variable to store the path to the folder that will be created
    folderpath=''
    if local:
        #print statement to inform the user that they are saving locally
        print('You have selected to save locally')
        #folderpath = "/home/pi/"+folder
        #check to see if a folder already exists for the current week
        while day >= 0 :
            #variable to hold a changing date
            tempFolderDate = folderDate - timedelta(days = day)
            #create a string containing a date to use as a folder name
            folder = tempFolderDate.strftime("%Y-%m-%d")
            #concantenate the folder name with the rest of the path to create a complete path
            folderpath = "/home/pi/"+folder
            #print(folderpath) #printStatement for testing
            #look for existing directory within one week of today
            if os.path.exists(folderpath):
                #inform the user that the folder was found and already exists
                print("Directory " , folder ,  " already exists")
                #exit the loop
                day = -1
                break  
            #increment day 
            day = day -1
            
        #If no working directory was found, create one
        if not os.path.exists(folderpath):
            os.mkdir(folderpath)
            print("Directory " , folder ,  " Created ")  
    else:
        #concatenate folder name with a path representing a usb
        folderpath = "/media/pi/"+usbName+"/" + folder  
        #print(folderpath) #printStatement for testing
        
        #check to see if a folder already exists for the current week
        while day >= 0 :
            tempFolderDate = folderDate - timedelta(days = day)
        
            folder = tempFolderDate.strftime("%Y-%m-%d")
            folderpath = "/media/pi/"+usbName+"/" + folder
            #print(folderpath) #printStatement for testing
            if os.path.exists(folderpath): #look for existing directory within one week of today
                print("Directory " , folder ,  " already exists")
                day = -1
                break  #exit the loop if a path was found
            day = day -1 #increment day
        
        if not os.path.exists(folderpath): # if no working directory was found, create one
            os.mkdir(folderpath)
            print("Directory " , folder ,  " Created ")
        
        #print statment to inform user of current working directory
        print("Working path: ",folderpath) 

    #Create list to return multiple values
    List = [folderDate, folderpath]
    return List
    
def writeDataToFile(dirPath, temp, humidity, soilMoisture1,soilMoisture2,soilMoisture3,soilMoisture4,co2,light):
    #funtion to write multiple values to a .csv file
    now = datetime.now()
    fileName = now.strftime("%m-%d")+".csv"
    fullpath=dirPath + "/" +fileName
    #create string representing the current time
    time = now.strftime("%H:%M")
    #the data tp be written into the csv file
    row = [time,temp,humidity,soilMoisture1,soilMoisture2,soilMoisture3,soilMoisture4,light,co2]  
    if os.path.exists(fullpath): #if the file exists
        with open(fullpath, 'a') as csvFile:
            #creating a writer object to write to the csv file
            writer = csv.writer(csvFile)
            #write the data into the csv file
            writer.writerow(row) 
        csvFile.close()
    else: #if the file doesn't exist
        path = dirPath
        #create csv file
        file = open(fullpath,"w+")
        file.close()
        #header for csv file
        row1 = ['Time', 'Temperature' , 'Humidity', 'Soil Moisture1',
                'Soil Moisture2','Soil Moisture3','Soil Moisture4','Light Level']
        with open(fullpath, 'a') as csvFile: #'a'means append file
            writer = csv.writer(csvFile)
            #header row
            writer.writerow(row1)
            #this will be very first data row
            writer.writerow(row) 
        csvFile.close()

def monitorSoil(ChannelNumber):
    #function to get soil moisture level and activate valve until moisture level is above 75%
    #Call the read_adc function on the object mcp to read the analog volatge on Channel = ChannelNumber
    RawValue = 0
    VREF = 3.3 #reference voltage
    MAX_RAWVALUE = 1023
    Voltage = MCP3008(ChannelNumber)
    RawValue = Voltage.raw_value
    #Convert the read decimal value to its equivalent analog value
    voltage = (RawValue*VREF)/MAX_RAWVALUE
    #Display the raw value and its equivalent analog value for testing
    #print("Binary Value= {:d}\tVoltage = {:.4f}".format(raw_value,voltage)) 
    wet = 1.5
    dry = 2.8
    moistureLevel = 40 #This is moisture level you want the system to maintain
    
    #conditionals to make small corrections to values
    if percentMoisture > 100.0:
        percentMoisture = 100
    elif percentMoisture < 0.0:
        percentMoisture = 0.0
    if(percentMoisture < moistureLevel ):
        #turn on indicator LED when soil is getting dry
        
    else:
        #turn off indicator LED when soil is wet
        
        
    sleep(0.5)
    return percentMoisture

def monitorLight(ChannelNumber):
    
    #function to monitorlighting conditions and activate a relay to turn on lights when its to dark
    isItBright = False
    lightlevel = 0.0
    RawValue = 0
    VREF = 3.3 #reference voltage
    MAX_RAWVALUE = 1023
    
    RawValue = Voltage.raw_value
    #Convert the read decimal value to its equivalent analog value
    voltage = (RawValue*VREF)/MAX_RAWVALUE
    #aproximate full sun and darkness
    lightlevel = (voltage/3.0) * 100
    lightThreshold = 50 # This is 50% of full sunlight, it is the point at which the "lamp" turns on
    #print("pr voltage:",voltage) #print statement for testing
    if(lightlevel > lightThreshold):
        
    List = [isItBright, lightlevel]
    return List

moistness1 = 0.0 #variable to hold the moisture level from the moisture sensor
humidity = 0.0 #variable to save humidity
tempC = 0.0 #variable to store temperature in celcius
tempF = 0.0 #variable to store temperature in Farenheit
co2Level = 0.0 #variable to co2 data, not used in open systems
lightLevel = 0.0 #variable to store the level of the light as a percentage of full sun light
lightchannel = 7 #adc channel for reading light level from the photo resistor
soilchannel1 = 0 #channel for reading the soil moisture data from plant 1
usb = '' #intitialize variable to store USB drive name
#Create a Temperature and Humidity Sensor Object
DHT_Sensor = Adafruit_DHT.DHT11
DHT_Pin = 18

waitForAns = True #Boolean to control while loop that collects user input
local = True #Default setting for saving location

while waitForAns: #Waiting for some user input
    response = input('Do you wish to use a USB drive for data storage?, Y/N: ')
    if(response.upper() == 'Y'):
        #set local to false to let the program know not to save locally
        local = False 
        #get user to enter USB name, the name must match the USB name exactly
        usb = input("Enter the name of your USB device: ") 
        #break out of the loop and continue with program
        
        waitForAns = False 
        break
    else: #for any response that isn't Y, save locally to avoid errors
        local = True
        #break out of loop and continue program
        waitForAns = False 
        break
#Create the first folder and get the path to the folder 
folderDate, currentPath = makeDirectory(usb,local) 
#ask the user for the time between samples                          
sampleRate = int(input('Please enter the time (in seconds) between samples: '))
lightTime = int(input('Please enter a total time (in hours) you want to illuminate your plants: '))
waterLED = LED(6)

try:

    while True:
        
        
        if date >= (folderDate + timedelta(days = 7)): #if its been one week make a new folder to store .csv files in
            folderDate, currentPath = makeDirectory(usb,local) #make new directory
        #first minute is datetime object representing 05:30 AM of the current day  
        firstMinute = date.replace(hour = 5, minute = 30, second =0, microsecond = 0)
        #lastMinute is a datetime object representing a time that is a specified time after 05:30AM 
        lastMinute = firstMinute + timedelta(hours = lightTime)
        #variable to store the percent moisture value returned by the monitorSoil function
        
        
        sleep(2)
        #print('Moisture Level: {0:0.1f} %'.format(moistness)) print statements for testing
        
        #read DHT sensor and store returned values into variables humidity, tempC
        
        sleep(1)
        #error handeling for nonetypes read from sensor
        if humidity is None and temperature is None:
            continue
        #convert temp to fahrenheit
        
        
        #call monitorLight and save its output as the boolean itIsBright and the the float lightLevel
        itIsBright, lightLevel = monitorLight(lightchannel)
        #Error Handling for null values
        if((itIsBright is None) or (lightLevel is None)):
            continue
        
        #Write data to file 
        writeDataToFile(currentPath, tempF, humidity, moistness1,0,0,0,co2Level,lightLevel)
        sleep(sampleRate)
      
except KeyboardInterrupt:
    waterLED.off() #Turn off indicator LED when system is inactive
    print('Exiting program')
   

