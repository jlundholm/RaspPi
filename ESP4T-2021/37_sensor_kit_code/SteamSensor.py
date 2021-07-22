from gpiozero import MCP3008
from time import sleep

if __name__ == '__main__':
    Voltage = MCP3008(0)
    RawValue = 0
    MAX_RAWVALUE = 1023
    VRef = 3.3
    MeasuredVoltage = 0.0
    moisture = 0.0
    while True:
        RawValue = Voltage.raw_value
        MeasuredVoltage = (VRef/MAX_RAWVALUE)*RawValue
        moisture = (MeasuredVoltage/3.3)*100
        print("Moisture is = {0:f} percent." .format(moisture))
        sleep(1.0) 