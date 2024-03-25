import numpy as np
import random

### ---------- edit below --------- #####
wave =  5.5465763*10 ### radar wavelength in mm
noise_level = 0.3  ## percent of half of wavelength
### ---------- edit above -------- #####

##### do not edit below unless you have to 
## read xy.txt
x = []
y = []
f = open('xy.txt','r')
while True:
	line = f.readline().strip()
	if line=='':
		#print ('break')
		break
	raw = line.split()
	x.append(int(raw[1]))
	y.append(int(raw[2]))
f.close()

## read vel_real.txt
vel = []
f = open('vel_real.txt','r')
while True:
	line = f.readline().strip()
	if line=='':
		#print ('break')
		break
	raw = line.split()
	vel.append(float(raw[0])) ## unit: mm/year	
f.close()

### read day.txt file
day = []
f = open('day.txt','r')
while True:
	line = f.readline().strip()
	if line=='':
		#print ('break')
		break
	raw = line.split()
	day.append(int(raw[0])) ## unit: day	
f.close()

b_time = []
for i in range(len(day)):
	if day[i] != 0:
		b_time.append(day[i])
#print(b_time)
index_refe = day.index(0)

#print (index_refe)

## create ph.txt file
f = open('ph.txt', 'w')

## create displacment file
f_disp = open('disp_real.txt', 'w')

noise_rms = noise_level * wave/2 
rng = np.random.default_rng()

for i in range(len(x)):
	## generate noise, Gaussian distribution		
	noise = rng.normal(size=len(b_time))*noise_rms	
		
	for j in range(len(b_time)):
		disp_tmp = vel[i]*b_time[j]/365 + noise[j]		
				
		ph_unwrap_tmp = disp_tmp*4*np.pi/wave ## unwarpped phase
		frac = ph_unwrap_tmp/(2*np.pi)
		decimal = frac - int(frac) ## decimal part 
		## wrap phase, range -pi to pi
		if decimal>=0.5:
			ph_tmp = (decimal-1)*2*np.pi
		elif decimal<=-0.5:
			ph_tmp = (decimal+1)*2*np.pi
		else:
			ph_tmp = decimal*2*np.pi
		if j<len(b_time)-1:
			f.write("%.2f\t" % (ph_tmp))  		
				
		else:
			f.write("%.2f\n" % (ph_tmp)) 		
			
		
		if j < index_refe:
			f_disp.write("%.2f\t" % (disp_tmp)) 
		if j == index_refe:
			f_disp.write("%.2f\t" % (0))
		if j>=index_refe and j< len(b_time)-1:
			f_disp.write("%.2f\t" % (disp_tmp)) 
		if j == len(b_time)-1:
			f_disp.write("%.2f\n" % (disp_tmp)) 
		
		
f.close()		
f_disp.close()
		
		
		
		
		
		


