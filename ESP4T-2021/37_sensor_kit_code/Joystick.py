"""
This program may be used to connect a Joystick to the Raspberry Pi in a script. To keep the
use open, no actions are preformed from inputs made on the joystick. The program will return
the raw values produced by the joy stick which range from 0-1023 with the neutral position
being 500-540. The button is state is either 0 or 1 with neutral being 0.
Serial Programmable Interface is used to achieve stable connection between the ADC Chip and Pi.
One 16-pin ADC chip(MSP3008) may be used to control 4 joysticks
Made by Tyler James UWYO CEAS-ECE. Contact tjames15@uwyo.edu if needed.
"""
#Import sleep from time
from time import sleep
#Import Serial Programmable Interface module from the Adafruit SPI library
import Adafruit_GPIO.SPI as SPI
#Import the MCP3008 module from the Adafruit library
import Adafruit_MCP3008
#Import the GPIO module from RPi.GPIO as io
import RPi.GPIO as io

#A class to instantiate channel objects
class Channel:
    def __init__(self,name,chnNumber,chnRef):
        self.__ChannelName = name #Give the Channel a name for future referance
        self.__Channel = chnNumber - 1 #Setting the channel number to computer numbering
        self.__RefValue = chnRef #The reference voltage value
    #Property method to access Channel Number    
    @property
    def Number(self):
        return self.__Channel #Returning the Channel number in computer numbering
    #Property method to access Channel Reference Value 
    @property
    def RefValue(self):
        return self.__RefValue #Returning the reference voltage for the ADC Chip
        
#Class to Instantiate a ADC Object
class ADC:
    def __init__(self,port,device):
        self.__SPI_Port = port #Where is it connected?
        self.__SPI_Dev = device #What device number is it?
        self.__adc = Adafruit_MCP3008.MCP3008(spi = SPI.SpiDev(self.__SPI_Port,self.__SPI_Dev)) #Setting up the ADC chip 
        self.__MaxRawValue = 1023 #The number of possible decimal values
        self.__Channels = [] #The number of channels
        
    def ChannelSetup(self,Name,Num,Ref):
        if(Num > 0 and Num <= 8):
            self.__Channels.append(Channel(Name,Num,Ref)) #Setting up the channel on the ADC
        else:
            print('Channel number is not valid')
    
    def ReadChannel(self,Num):
        #Check whether the channel exists
        raw = 0 #Instantiating the raw value varible
        for chn in self.__Channels: #Checking the channel
            if(Num - 1) == chn.Number: #Polling the channel number to read
                raw = self.__adc.read_adc(chn.Number) #Raw value will be digital output code or decimal value
        return raw #Returning value

#Class to make a joystick
class Joystick:
    def __init__(self,Port,Device,Channel,RefVolt,Button):
        self.__adc = ADC(Port,Device) #Setting up the ADC Chip for use
        self.__ChnY = Channel #Setting the Channel for the Y axis
        self.__ChnX = Channel+1 #Setting the Channel for the X axis
        self.__Y = self.__adc.ChannelSetup('Y',self.__ChnY,RefVolt) #Setting up Channel Y
        self.__X = self.__adc.ChannelSetup('X',self.__ChnX,RefVolt) #Setting up Channel X
        self.__Z = Button #Setting the Button pin
        io.setup(self.__Z,io.IN) #Setting button pin to output
        
    def Position(self):
        rawValueY = self.__adc.ReadChannel(self.__ChnY) #Getting the raw value from Channel Y
        rawValueX = self.__adc.ReadChannel(self.__ChnX) #Getting the raw value from Channel X
        rawValueZ = io.input(self.__Z) #Getting the state of the button
        return rawValueY,rawValueX,rawValueZ #Returning the values read
    
                
"""
To use the joystick in a script, call 'Joystick(Port,Device,Channel,RefVolt,Button)'
Port is saying where the ADC Chip is connected to the Pi
Device names the Chip
Channel is for the first channel used by the joystick as it uses two channels, one for the y-axis and one for the x-axis
RefVolt is the referance voltage for the ADC Chip. Set this to the voltage that is being used to power the joystick
Button is a digital input to which the button on the joystick is connected to.


if __name__ == '__main__':
    io.setmode(io.BCM)
    joystick = Joystick(0,0,1,3.3,21)
    
    
    print('Reading Position')
    try:
        while True:
            rawValueY,rawValueX,rawValueZ = joystick.Position()
            print('Raw Value Y = {:4d} Raw Value X = {:4d} Raw Value Z = {:1d}'.format(rawValueY,rawValueX,rawValueZ))
            sleep(0.10)
    
        
    except KeyboardInterrupt:
        print('Exit')
"""

