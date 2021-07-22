#Library Modules to implement the Web Server - Bottle
from bottle import route,run,template
#Importing SenseHat module from sense_hat library
from sense_hat import SenseHat
#Dunction that returns a text with measurements of Temp, Pressure and Humidity
def GetMeasurements():
    #Initialize the SenseHat object
    sense = SenseHat()
    #Get the temperature
    # --> 
    #Convert the temperature to Fahrenheit
    t=(t*(9.0/5.0))+32.0
    #Round the temperature to two decimal points
    t=round(t,2)
    #Get the pressure
    # --> 
    #Round the pressure to two decimal points
    p=round(p,2)
    #Get the humidity
    # --> 
    #Round the humidity to two decimal points
    h=round(h,2)
    #Collectively create a text displaying Temp, Pressure and Humidity
    # --> 
    return msg
#Weather path of the server
@route('/Weather')
def index(name='Measurements'):
    measurementMsg = GetMeasurements()
    return template('<b>{{t}}</b>',t=measurementMsg)
#Running the host
run(host='0.0.0.0',port=80)
