#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
m = LargeMotor('outB')
m2 = LargeMotor('outС')
m3 = MediumMotor('outA')
gy = GyroSensor()
us = UltrasonicSensor()
assert gy.connected
gy.mode='GYRO-ANG'
units = gy.units
 
assert us.connected
us.mode='US-DIST-CM'
units = us.units
status=1
while True:
    if status==1:
        assert us.connected
        us.mode='US-DIST-CM'
        distance = us.value()/10
        if distance>20:
            m.run_forever(speed_sp=900)
        else:
            status = 2
        continue

    if status==2:
        m.run_to_rel_pos(position_sp=45, speed_sp=900)
        if distance>20:
            while True:
            angle = gy.value()

            if gy=90
            
            sleep(0.5)
        else:
            
            status = 3
        continue

    if status==3:
        m.run_to_rel_pos(position_sp=90, speed_sp=900)
        if distance>20:
            while True:
            angle = gy.value()
            m2.run_to_rel_pos(position_sp=90, speed_sp=900)
            m3.run_forever(speed_sp=900)
            if gy=-90
            
            sleep(0.5)
        else:
            
            status = 1
        
        continue

