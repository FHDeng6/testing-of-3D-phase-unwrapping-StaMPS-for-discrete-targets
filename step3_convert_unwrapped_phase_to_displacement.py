import numpy as np

########### edit below  ###########
wave =  5.5465763*10 ### wavelength in mm
########## edit above ###########

######## do not edit below unless you have to 


### get index of the reference image
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

#print(b_time)
index_refe = day.index(0)


### load unwrapped phase
ph_uw = np.loadtxt("ph_uw.txt") #default data type is float

#print(ph_uw.shape)
#print(ph_uw.shape[0], ph_uw.shape[1])
disp = np.zeros((ph_uw.shape[0], ph_uw.shape[1]+1))

## create disp_sim.txt file, simulated displacment file
f = open('disp_observed.txt', 'w')

for i in range(ph_uw.shape[0]):
	for j in range(ph_uw.shape[1]+1):
		if j == index_refe:  ## at the reference image acquisition day
			disp[i][j] = 0
		elif j<index_refe:
			disp[i][j] = wave*ph_uw[i][j]/(4*np.pi) 
		else:
			disp[i][j] = wave*ph_uw[i][j-1]/(4*np.pi) 
		
		
		if j<len(day)-1:
			f.write("%.2f\t" % (disp[i][j]))  	
		else:
			f.write("%.2f\n" % (disp[i][j])) 	
		
f.close()		
				
		
		
		
		


