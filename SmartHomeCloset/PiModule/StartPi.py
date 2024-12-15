import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS

#import Adafruit_ADS1x15 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADS object and specify the gain
ads = ADS.ADS1115(i2c)
ads.gain = 1 
chan = AnalogIn(ads, ADS.P0)

# Continuously print the values

picked_up = False

while True:
    volt = chan.voltage
    #print(type(volt))
    #tmp = abs(volt) - 3.0
    #print(type(tmp))
    #print(tmp)
    #tmpp = tmp > 0.0000001
    #print(type(tmpp))
    #print(tmpp)
    
    print(f"MQ-135 Voltage: {volt}V")

    if volt - 3.0 > 0.000001:
        if picked_up:
            picked_up = False
            print("item is on the rack")
    else:
        if not picked_up:
            picked_up = True
            print("item has been picked up")

    time.sleep(1)
