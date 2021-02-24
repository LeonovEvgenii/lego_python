#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
from math import *
D = 'outD'
C = 'outC'
B = 'outB'
A = 'outA'
A1 = 'in1'
B2 = 'in2'
C3 = 'in3'
D4 = 'in4'
trigger = 0
m_left = LargeMotor(B)
m_right = LargeMotor(C)
mm = Motor(A)
mm1 = Motor(D)
m_right.reset()
m_left.reset()
from time import sleep
color = 'white'
from ev3dev.ev3 import *
cl = ColorSensor(B2) 
cl1 = ColorSensor(C3)
cl.mode='COL-REFLECT'
def find_color (x):
    if x>49:
        return "white"
    else:
        return "black"
#forward
motor_speed = 190 
motor_time = 3
time_sleep = 0.5
#right left
motor_time_1 = 2.21 
motor_speed_1 = 85
# kran
motor_time_kran = 10
motor_speed_kran = 200
#zaxvat
motor_time_zaxvat = 2
motor_speed_zaxvat = -200

# shtrix code
speed = 80
encL, encR = 0,0
n = 5 #высота
nn = 7 #длина

a = [0]*7
past_trigger = 7
center_y = n//2
st_x, st_y  = 0,center_y
fin_x,fin_y = nn - 2,center_y
def zaxvat (speed,time,time_sleep):
    sleep(time_sleep)
    mm.run_forever(speed_sp=speed)
    

    sleep(time)
    mm.stop(stop_action="hold")
def kran (speed,time,time_sleep):
    sleep(time_sleep)
    mm1.run_forever(speed_sp=-speed)
    

    sleep(time)
    mm1.stop(stop_action="hold")
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
def left (speed,time,time_sleep):
    sleep(time_sleep)
    m_left.run_forever(speed_sp=speed)
    m_right.run_forever(speed_sp=-speed)

    sleep(time)
    m_left.stop(stop_action="hold")
    m_right.stop(stop_action="hold")
def back (speed,time,time_sleep):
    sleep(time_sleep)
    m_left.run_forever(speed_sp=-speed)
    m_right.run_forever(speed_sp=-speed)

    sleep(time)
    m_left.stop(stop_action="hold")
    m_right.stop(stop_action="hold")


def marshroot (x,y,b,c, past_trigger):



	while x!=b or y!=c:
		trigger = 0
		propusk_up = 1
		propusk_left = 1
		propusk_down = 1
		propusk_right = 1
		#up
		if a[y-1][x]>3:
			jj = a[y-1][x]
			
			while jj!=0 and propusk_up == 1:
				if jj%10==4:

					propusk_up = 0 
				jj=jj//10
		#left
		if a[y][x-1]>3:
			jj = a[y][x-1]
			while jj!=0 and propusk_left == 1:
				if jj%10==5:
					
					propusk_left = 0
					
				jj=jj//10
		#down
		if a[y+1][x]>3:
			jj = a[y+1][x]
			while jj!=0 and propusk_down == 1:
				if jj%10==6:
					propusk_down = 0 
				jj=jj//10
		#right
		if a[y][x+1]>3:
			jj = a[y][x+1]
			while jj!=0 and propusk_right == 1:
				if jj%10==7:
					propusk_right = 0 
				jj=jj//10
		if abs(y-c)>=abs(x-b):
			
			if y-c>0:
				if a[y-1][x] != 2  and propusk_up == 1:
					print('up')
					trigger = 4
				
				elif x-b>=0:
					
					if a[y][x-1] != 2 and propusk_left == 1:
						print('left')
						trigger = 5
					elif a[y][x+1] != 2 and propusk_right == 1:
						print('right')
						trigger = 7
				elif x-b<0:
					if a[y][x+1] != 2 and propusk_right == 1:
						print('right')
						trigger = 7
					elif a[y][x-1] != 2 and propusk_left == 1:
						print('left')
						trigger = 5
				elif a[y+1][x]  != 2  and propusk_down == 1:
					print('down')
					trigger = 6
			else:
				if a[y+1][x]  != 2  and propusk_down == 1:
					print('down')
					trigger = 6
				
				elif x-b>=0:
					if a[y][x-1] != 2 and propusk_left == 1:
						print('left')
						trigger = 5
					elif a[y][x+1] != 2 and propusk_right == 1:
						print('right')
						trigger = 7
				elif x-b<0:
					if a[y][x+1] != 2 and propusk_right == 1:
						print('right')
						trigger = 7
					elif a[y][x-1] != 2 and propusk_left == 1:
						print('left')
						trigger = 5
				
				elif a[y-1][x] != 2 and propusk_up == 1:
					print('up')
					trigger = 4
		else:
			if x-b>0:
				if a[y][x-1] != 2 and propusk_left == 1:
						print('left')
						trigger = 5
				elif y-c>=0:
					if a[y-1][x] != 2 and propusk_up == 1:
						print('up')
						trigger = 4
					elif a[y+1][x]  != 2  and propusk_down == 1:
						print('down')
						trigger = 6
				elif y-c<0:
					if a[y+1][x]  != 2  and propusk_down == 1:
						print('down')
						trigger = 6
					elif a[y-1][x] != 2 and propusk_up == 1:
						print('up')
						trigger = 4


				elif a[y][x+1] != 2 and propusk_right == 1:
					print('right')
					trigger = 7
			else:
				if a[y][x+1] != 2 and propusk_right == 1:
					print('right')
					trigger = 7
				elif y-c>=0:
					if a[y-1][x] != 2 and propusk_up == 1:
						print('up')
						trigger = 4
					elif a[y+1][x]  != 2  and propusk_down == 1:
						print('down')
						trigger = 6
				elif y-c<0:
					if a[y+1][x]  != 2  and propusk_down == 1:
						print('down')
						trigger = 6
					elif a[y-1][x] != 2 and propusk_up == 1:
						print('up')
						trigger = 4

				elif a[y][x-1] != 2 and propusk_left == 1:
					print('left')
					trigger = 5


		# повороты робота
		if trigger-past_trigger == 1:
			print('left 90 (first)')
			left(motor_speed_1,motor_time_1,time_sleep)
		elif past_trigger-trigger == 1:
			print('right 90 (first)')
			right(motor_speed_1,motor_time_1,time_sleep)
		elif abs(trigger-past_trigger) == 2:
			print('rasvorot 180 (first)')
			right(motor_speed_1,2*motor_time_1,time_sleep)
		#езда робота
		if trigger == 4:
			a[y][x] = 0
			y=y-1
			a[y][x] = '^'

		if trigger == 5:
			a[y][x] = 0
			x=x-1
			a[y][x] = '<'

		if trigger == 6:
			a[y][x] = 0
			y=y+1
			a[y][x] = 'v'

		if trigger == 7:
			a[y][x] = 0
			x=x+1
			a[y][x] = '>'
		forward(motor_speed,motor_time,time_sleep)
		for i in range (n):
			print(a[i])
		past_trigger = trigger

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
    print(find_color(cl.value()),find_color(cl1.value()))		
for i in range (n):
	if i==0 or i == n-1:
		a[i] = [2]*nn
	elif i==st_y:
		a[i] = [0]*nn
		a[i][0] = 2
		a[i][nn-1] = 2
		a[st_y][st_x]='>'

	else:
		a[i] = [0]*nn
		a[i][0] = 2
		a[i][nn-1] = 2
	print(a[i])




for i in range (2):
	marshroot(st_x,st_y,fin_x,fin_y, past_trigger)
	
	print ('zagruzka balls ')
	kran(motor_time_kran,motor_speed_kran,time_sleep)
	zaxvat(motor_speed_zaxvat,motor_time_zaxvat,time_sleep)
	kran(motor_time_kran,motor_speed_kran,time_sleep)
	#если надо то робот подъедет
	#print('координаты тела')

	st_x_1, st_y_1 = fin_x, fin_y
	fin_x_1, fin_y_1 = 2,1  #считывается с штрих кода
	marshroot(st_x_1,st_y_1,fin_x_1,fin_y_1, past_trigger)
	past_trigger = trigger
	#костыли
	if fin_y_1 == 3:

		trigger = 6 
		a[fin_y_1][fin_x_1] = 'v'
		print ('left 90 ')
		left(motor_speed_1,motor_time_1,time_sleep)
	else:
		trigger = 4
		a[fin_y_1][fin_x_1] = '^'
		print ('right 90')
		right(motor_speed_1,motor_time_1,time_sleep)
	kran(motor_time_kran,motor_speed_kran,time_sleep)
	zaxvat(-motor_speed_zaxvat,motor_time_zaxvat,time_sleep)
	kran(motor_time_kran,motor_speed_kran,time_sleep)
	for i in range (n):
			print(a[i])
	if fin_y_1 == 3:
		print ('left 90 ')
		left(motor_speed_1,motor_time_1,time_sleep)
	else:
		print ('right 90 ')
		right(motor_speed_1,motor_time_1,time_sleep)
    
    
	
	st_x,st_y = fin_x_1, fin_y_1

marshroot(st_x,st_y,0,center_y,past_trigger)
