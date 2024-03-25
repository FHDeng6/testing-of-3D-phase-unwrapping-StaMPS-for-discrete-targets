import numpy as np
from numpy.polynomial.polynomial import polyfit

### read day.txt file, convert day to decimal year
time = []
f = open('day.txt','r')
while True:
	line = f.readline().strip()
	if line=='':
		#print ('break')
		break
	raw = line.split()
	time.append(int(raw[0])/365.0) ## unit: day	
f.close()

print (len(time))
#print (time)

### load displacment
disp = np.loadtxt("disp_observed.txt") #default data type is float

print(disp.shape)


f = open('vel_observed.txt', 'w')
vel = [0]*disp.shape[0]
for i in range(disp.shape[0]):
	los = []
	for j in range(disp.shape[1]):
		los.append(disp[i][j])
	### get linear rate
	b, slope = polyfit(time, los, 1)
	vel[i] = slope
	
	f.write("%.2f\n" % (vel[i])) 	
		
f.close()		
				
		
		
		
		


