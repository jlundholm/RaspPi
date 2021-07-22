#Code for KeyeStudio Passive Buzzer

#KeyeStudio Passive Buzzer Module = Ks0019
#Working Voltage = 3.3V - 5.0V
#Interface Type = Digital

#Imports TonalBuzzer from GPIOzero library
from gpiozero import TonalBuzzer
#Imports tones from GPIOzero library
from gpiozero.tones import Tone
#Imports sleep from time library
from time import sleep

if __name__ == '__main__':
    b = TonalBuzzer(12) #sets variable as output signal on pin 12
    try:
        while(True): #creates an infinite loop
            b.play(Tone("A4")) #tells buzzer which note to play
            b.play(Tone(220.0)) #This is in hertz
            b.play(Tone(60))
            print("Playing A4") #prints out which note is played
            sleep(1) #forces the device to play for 1 second
            b.play(Tone("A3")) #tells buzzer which note to play
            b.play(Tone(220.0)) #tells which hertz to play at
            b.play(Tone(60))
            print("Playing A3") #prints out which note is being played
            sleep(1) #forces buzzer to play for 1 second
            b.stop() #stops the buzzer from making any noice
            sleep(2) #forces the buzzer to sleep for 2 seconds
    except KeyboardInterrupt: #allows user to exit the program
        print("All Done") #tells user the program is all done