from time import sleep
import Adafruit_DHT

if __name__ == '__main__':
    print("Measuring Temperature and Humidity")
    #Create a Temperature and Humidity Sensor Object
    DHT_Sensor = Adafruit_DHT.DHT11
    DHT_Pin = 18
    while True:
        humidity, temperature = Adafruit_DHT.read(DHT_Sensor,DHT_Pin)
        if humidity is not None and temperature is not None:
            print("Temperature = {0:0.1f}C, Humidity = {1:0.1f}%".format(temperature,humidity))
        else:
            print("Sensor Failure")
        sleep(3)
        