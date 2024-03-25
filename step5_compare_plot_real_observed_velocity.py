import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

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
vel_real = []
f = open('vel_real.txt','r')
while True:
	line = f.readline().strip()
	if line=='':
		#print ('break')
		break
	raw = line.split()
	vel_real.append(float(raw[0]))
f.close()

## shift the data, make the mean 0
## or you can reference the result to a point that does not have phase unwrapping error (usually an onland point)
vel_real_mean = sum(vel_real)/len(vel_real)
for i in range(len(vel_real)):
	vel_real[i] = vel_real[i] - vel_real_mean
print(vel_real_mean)

## read vel_observed.txt
vel_obs = []
f = open('vel_observed.txt','r')
while True:
	line = f.readline().strip()
	if line=='':
		#print ('break')
		break
	raw = line.split()
	vel_obs.append(float(raw[0]))
f.close()

## shift the data, make the mean 0
## or you can reference the result to the same reference point as used in the real rate result
vel_obs_mean = sum(vel_obs)/len(vel_obs)
for i in range(len(vel_obs)):
	vel_obs[i] = vel_obs[i] - vel_obs_mean
print(vel_obs_mean)

## residual of velocity
vel_res = [0]*len(vel_obs)
for i in range(len(vel_obs)):
	vel_res[i] = vel_real[i] - vel_obs[i]

## write to file
f = open('vel_residual.txt','w') 
for i in range(len(vel_res)):
	f.write("%.2f\n" % (vel_res[i]))  
f.close()

#### plot results
fig = plt.figure(figsize=(10,10))
gs = gridspec.GridSpec(2,2)
gs.update(wspace=0.2, hspace=0.2)

cm = plt.cm.get_cmap('jet') #RdYlBu
v_min = -10
v_max = 10

ax = fig.add_subplot(gs[0])
sc = ax.scatter(x, y, c=vel_real, marker='o',  edgecolors='none', s=10, cmap=cm, vmin=v_min, vmax=v_max) 
ax.title.set_text('Real')

ax = fig.add_subplot(gs[1])
sc = ax.scatter(x, y, c=vel_obs, marker='o',  edgecolors='none', s=10, cmap=cm, vmin=v_min, vmax=v_max) 
ax.title.set_text('Observed')

ax = fig.add_subplot(gs[2])
sc = ax.scatter(x, y, c=vel_res, marker='o',  edgecolors='none', s=10, cmap=cm, vmin=v_min, vmax=v_max) 
ax.title.set_text('Residual') 
 
## add color bar 
cbaxes=fig.add_axes([0.25,0.01,0.5,0.015])
c_bar=plt.colorbar(sc, cax=cbaxes, orientation='horizontal', extend='both') #, ticks=[-50,-25,0,25,50]
c_bar.set_label('Rate (mm/year)', labelpad = 6)


fig.savefig('rates_real_observed_residual.png',dpi = 300, bbox_inches='tight')

