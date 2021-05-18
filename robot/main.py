#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
m = LargeMotor('outB')
m2 = LargeMotor('outС')
m3 = MediumMotor('outA')
gy = GyroSensor()
assert gy.connected
gy.mode='GYRO-ANG'
units = gy.units


while True:
    angle = gy.value()
    print(str(angle) + " " + units)
    if angle>90:
        m.run_to_rel_pos(position_sp=3560, speed_sp=900, stop_action="brake")


    sleep(0.5)

# m.run_to_rel_pos(position_sp=3560, speed_sp=900, stop_action="brake")
m3.run_to_rel_pos(position_sp=-90, speed_sp=900, stop_action="brake")
# m.run_timed(time_sp=1500, speed_sp=900, stop_action="brake")
# print("0" + str(m.speed_sp))
# sleep(1) # За секунду мотор успеет раскрутиться
# print(900 + int(m.speed))
# sleep(4)
# m2.run_timed(time_sp=5000, speed_sp=900, stop_action="brake")
# print(500 + str(m.speed_sp))
# sleep(4) # За секунду мотор успеет раскрутиться
# print(900 + str(m.speed))
# sleep(4)


# m3.run_to_rel_pos(position_sp=120, speed_sp=900, stop_action="brake")



sleep(1)