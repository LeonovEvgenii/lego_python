#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

m = LargeMotor('outB', stop_action="hold")
m.run_to_rel_pos(position_sp=360, speed_sp=900)
sleep(5)
Suond.beep() 

