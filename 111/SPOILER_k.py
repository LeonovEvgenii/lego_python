trigger = 0
from math import *
luck = 0
n = 5
nn = 7 
a = [0]*7
past_trigger = 7
center_y = n//2
st_x, st_y  = 0,center_y
fin_x,fin_y = nn - 2,center_y
		
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


		
		if trigger-past_trigger == 1:
			print('поворот на', 90 * (trigger - past_trigger), 'градусов влево')
		elif past_trigger-trigger == 1:
			print('поворот на', 90 * (- trigger + past_trigger), 'градусов вправо')
		elif abs(trigger-past_trigger) == 2:
			print ('разворот на 180 градусов')
		

		luck = int(input('успех'))

		if luck == 0:

			if trigger == 4:
				a[y-1][x] *= 10
				a[y-1][x] += trigger

			if trigger == 5:
				a[y][x-1] *= 10
				a[y][x-1] += trigger

			if trigger == 6:
				a[y+1][x] *= 10
				a[y+1][x] += trigger

			if trigger == 7:
				a[y][x+1] *= 10
				a[y][x+1] += trigger
		else:
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
		for i in range (n):
			print(a[i])
		past_trigger = trigger
for i in range (2):
	marshroot(st_x,st_y,fin_x,fin_y, past_trigger)
	

	print ('загрузка шариков ')
	#если надо то робот подъедет
	print('координаты тела')

	st_x_1, st_y_1 = fin_x, fin_y
	fin_x_1, fin_y_1 = map(int,input().split())
	marshroot(st_x_1,st_y_1,fin_x_1,fin_y_1, past_trigger)
	past_trigger = trigger
	if fin_y_1 == 3:

		trigger = 6 
		a[fin_y_1][fin_x_1] = 'v'
		print ('поворот на 90 градусов влево')
	else:
		trigger = 4
		a[fin_y_1][fin_x_1] = '^'
		print ('поворот на 90 градусов вправо')
	
	for i in range (n):
			print(a[i])

	print ('выгрузка шариков')
	st_x,st_y = fin_x_1, fin_y_1

marshroot(st_x,st_y,0,center_y,past_trigger)




