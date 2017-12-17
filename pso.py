# particle swarm optimization
import numpy as np 
import matplotlib.pyplot as plt
from class_define import PSO
from utils import *
from fn import cost_function

# define hyper-parameter
# define problem
min_pos = -10
max_pos = 10
max_vel = 0.2*(max_pos-min_pos)

kappa = 1
phi1 = 2.05
phi2 = 2.05
phi = phi1+phi2
chi = 2*kappa/np.abs(2-phi-np.sqrt(phi*phi-4*phi))
w = chi
c1 = chi*phi1
c2 = chi*phi2

# Parameters of cost function
pb = {'nVar':5,'VarMin':min_pos,'VarMax':max_pos,'VelMin':-max_vel,'VelMax':max_vel}

# Parameters of update rule
pr = {'w':w,'c1':c1,'c2':c2}

nPop = 100
MaxIt = 500

# Init population
best = {'Pos': None, 'Cost': np.inf}			# save the best solution ever found
his = np.zeros(MaxIt) 					# save the best cost of each iteration
pop = list()
for i in range(nPop):
	pso = PSO(pb)
	pop.append(pso)
	if pso.Cost < best['Cost']:
		best['Pos'] = pso.Pos
		best['Cost'] = pso.Cost

# start timer
tic()

# start loop
for it in range(MaxIt):
	for i in range(nPop):
		pop[i].update(pb,pr,best['Pos'])

		if pop[i].BestCost < best['Cost']:
			best['Pos'] = pop[i].BestPos
			best['Cost'] = pop[i].BestCost


	his[it] = best['Cost']
	print("Iteration: %d Best Cost = %s" %(it+1,his[it]))

# stop timer
toc()

# plot graph
plt.plot(his)
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.show()