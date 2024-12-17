import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS

#import Adafruit_ADS1x15 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from django.db import connection


def hanger_update(hanger_id, in_closet):
    sql = """ UPDATE closet_info
            SET in_closet = %s
            WHERE id = %s"""

    conn = psycopg2.connect(dbname='webappdb',
        user='postgre',
        password='1q2w3e4R.',
        host='192.168.86.22',
        port='5432')

    try:
        with  conn.cursor() as cur:
            # execute the UPDATE statement
            cur.execute(sql, (hanger_id, in_closet))
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print("done") 






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

    if volt - 1.0 > 0.000001:
        if picked_up:
            picked_up = False
            print("hanger 1 is on the rack")
            #hanger_update(hanger_id = 1, in_closet = True)
    else:
        if not picked_up:
            picked_up = True
            print("hanger 1 has been picked up")
            #hanger_update(hanger_id = 1, in_closet = False)
    time.sleep(1)
