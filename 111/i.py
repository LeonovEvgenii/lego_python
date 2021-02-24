#!/usr/bin/env python3
D = 'outD'
C = 'outC'
B = 'outB'
A = 'outA'
A1 = 'in1'
B2 = 'in2'
C3 = 'in3'
D4 = 'in4'
speed = 20
encL, encR = 0,0
from time import sleep
color = 'white'
from ev3dev.ev3 import *
cl = ColorSensor(B2) 
cl1 = ColorSensor(D4)
cl.mode='COL-REFLECT'
def find_color (x):
    if x>49:
        return "white"
    else:
        return "black"
print(cl1.value())


'''
m_left = Motor(B)
m_left.run_forever(speed_sp=speed)
'''
m_left = LargeMotor(B)
m_right = LargeMotor(C)

def forward (speed,time,time_sleep):
    sleep(time_sleep)
    m_left.run_forever(speed_sp=speed)
    m_right.run_forever(speed_sp=speed)

    sleep(time)
    m_left.stop(stop_action="hold")
    m_right.stop(stop_action="hold")
while color == 'white':
    forward(2*speed,0.4,0)
    color = find_color(cl.value())
while color == 'black':
    Sound.speak(cl.value()).wait()
    print(cl.value(),end = ' ')
    color = find_color(cl.value())
    if color == 'black':
        forward(speed,0.4,0)
    print (color)

    encL = m_left.position
    encR = m_right.position

    print(encL,encR)

length_1 = (encL+encR)//2
print(length_1)

m_left.reset()
m_right.reset()

while color == 'white':
    Sound.speak(cl.value()).wait()
    print(cl.value(),end = ' ')
    if cl.value() <= 20:
        color = 'black'
    else:
        color = 'white'
        forward(speed,0.4,0)
    print (color)
    encL = m_left.position
    encR = m_right.position
    print(encL,encR)

length_2 = (encL+encR)//2
print (length_2)

length = (length_1+length_2)//2
print(length)

for i in range (7):
    forward(length,1,0)
    print(find_color(cl.value()))


    
