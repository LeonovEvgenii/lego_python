#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
m = LargeMotor('outB')
# m2 = LargeMotor('outС')
# m3 = MediumMotor('outA')
# gy = GyroSensor()
us = UltrasonicSensor()
# assert gy.connected
# gy.mode='GYRO-ANG'
# units = gy.units
 
assert us.connected
us.mode='US-DIST-CM'
# units = us.units
status=1
while True:
    if status==1:
        # assert us.connected
        # us.mode='US-DIST-CM'
        distance = us.value()/10
        print(distance)
        if distance<20:
            status = 2
        continue

    if status==2:
        print(2)
        sleep(1000)
        # m.run_forever(speed_sp=900)

        status=3
        continue

    if status==3:
        # print(3)
        status=1
        continue

