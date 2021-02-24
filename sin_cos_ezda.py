#!/usr/bin/env python3
start_pos = 0 # угол к Х изначально
pos = 0
radius = 1 #радиус колеса в метрах
from ev3dev.ev3 import *
from time import sleep
import math
D = 'outD'
C = 'outC'
B = 'outB'
A = 'outA'
A1 = 'in1'
B2 = 'in2'
C3 = 'in3'
D4 = 'in4'
# тут должен быть дальномер
import math
def motor_start (port1,port2): #инициализация моторов
    m_left = LargeMotor(port1)
    m_right = LargeMotor(port2)
    return m_left,m_right
def sensor_start (port,name): #гироскоп (вскоре другие датчики)
    if name == gyro:
        gyro = GyroSensor(port)
        gyro.mode = "GYRO-ANG"
        return gyro
    elif name == ultrasonic:
        us = UltrasonicSensor(port) 
        us.mode='US-DIST-CM'
        return us
def enc_to_meters(radius,encoder): #енкодерские единицы в метры
    # пи * r = 180 градусов

    return encoder * math.pi * radius / 180 
def motor_reset():#для энкодера
    m_left.reset()
    m_right.reset()
def find_angle (start_angle):#нахождение относительного угла
    global start_pos
    angle = gyro.value() #нахождение абсолютного угла
    angle -= start_angle #нахождение относительного угла (если робот находится на оси Х)
    angle += start_pos # нахождение относительного угла с учётом поправки на начальный угол к оси Х (пока вбивается вначале)
    
    while angle > 360:
        angle -= 360
    while angle < 0:
        angle += 360
    return angle
def right (speed,angle,start_angle_right,time_sleep):
    sleep(time_sleep)
    angle_0 = start_angle_right
    m_left.run_forever(speed_sp=-speed) #кручение моторами
    m_right.run_forever(speed_sp=speed) 
    if start_angle_right<angle:
        while angle_0>0 and angle_0<angle: 
            angle_0 = find_angle(start_angle)
            sleep(0.5)
        while angle_0>start_angle_right-angle+360:
            angle_0 = find_angle(start_angle)
            sleep(0.5)
    else:
        while angle_0>start_angle_right-angle:
            angle_0 = find_angle(start_angle)
            sleep(0.5)
def forward (speed,time,fin_x,fin_y,time_sleep):# основная функция (скорость, время движения, предполагаемые координаты, задержка перед запуском)
    global x, y # координаты

    sleep(time_sleep) # ожидание перед запуском

    
    motor_reset()
    m_left.run_forever(speed_sp=speed)#кручение моторами
    m_right.run_forever(speed_sp=speed)
    past_encoder = 0 # прошлое значение энкодера для вычисления расстояния
    for i in range (2*time):
        angle = math.radians(find_angle(start_angle)) #в радианы показания угла (библиотека math предполагает работу с радианами)
        
        
        encoder = enc_to_meters(radius, m_left.position + m_right.position) / 2 - past_encoder #вычисление пройденного расстояния
        x+=encoder*math.cos(angle)
        y+=encoder*math.sin(angle)
        print('angle: ',angle,'x and y',x,y)
       
        # тут должен быть дальномер

        sleep(0.5)
        past_encoder += encoder
    pos = find_angle(start_angle)
    print(x,y, pos)
    print(math.sqrt((fin_x - x) ** 2 + (fin_y - y) ** 2),math.degrees(math.atan((fin_y-y)/(fin_x-x))))
    
    # поворот на угол и езда до точки (планируется)
    m_left.stop(stop_action="hold")
    m_right.stop(stop_action="hold")
    
#старьё
def left (speed,angle,time_sleep):sleep(time_sleep)
    m_left.run_forever(speed_sp=speed)
    m_right.run_forever(speed_sp=-speed)

    
    m_left.stop(stop_action="hold")
    m_right.stop(stop_action="hold")
def back (speed,time,time_sleep):
    sleep(time_sleep)
    m_left.run_forever(speed_sp=-speed)
    m_right.run_forever(speed_sp=-speed)

    sleep(time)
    m_left.stop(stop_action="hold")
    m_right.stop(stop_action="hold")
x = 0.0
y = 0.0
pos = 0 #угол к горизонтали

m_left,m_right = motor_start(B,C)
gyro = sensor_start(C3,gyro)
start_angle = gyro.value()
angle = 0

    
    
forward (50,10,486,486*2,0.1)

    