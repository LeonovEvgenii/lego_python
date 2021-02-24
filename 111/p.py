#!/usr/bin/env python3

from time import sleep

from ev3dev.ev3 import *
D = 'outD'
C = 'outC'
B = 'outB'
A = 'outA'
m_left = LargeMotor(B)
m_right = LargeMotor(C)
mm = Motor(A)
mm1 = Motor(D)

def forward (speed,time,time_sleep):
    sleep(time_sleep)
    m_left.run_forever(speed_sp=speed)
    m_right.run_forever(speed_sp=speed)

    sleep(time)
    m_left.stop(stop_action="hold")
    m_right.stop(stop_action="hold")
def right (speed,time,time_sleep):
    sleep(time_sleep)
    m_left.run_forever(speed_sp=-speed)
    m_right.run_forever(speed_sp=speed)

    sleep(time)
    m_left.stop(stop_action="hold")
    m_right.stop(stop_action="hold")
def zaxvat (speed,time,time_sleep):
    sleep(time_sleep)
    mm.run_forever(speed_sp=speed)
    

    sleep(time)
    mm.stop(stop_action="hold")
def kran (speed,time,time_sleep):
    sleep(time_sleep)
    mm1.run_forever(speed_sp=speed)
    

    sleep(time)
    mm1.stop(stop_action="hold")
   
kran (200,10,0.5)
zaxvat (-100,2,0.5)
right (85,2.2,0.5)




