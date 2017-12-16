import numpy as np
import matplotlib.pyplot as plt
from bee import Bee
from fn import cost_function
from utils import *

# define problem of cost function
nVar = 5
VarMin = -10
VarMax = 10

# ABC setting
MaxIt = 500				# Maximum number of iterations
nPop = 100					# Population size
L = round(0.6*nVar*nPop);	# abandonment limit parameter (trial limit)
a = 1						# acceleration coefficient upper bount

# Initialize population
history = np.zeros(MaxIt)				# save the best cost of each iteration
best_bee = Bee(VarMin,VarMax,nVar)		# save the best bee
c = np.zeros(nPop)						# abandonment counter 
new_bee = Bee()

pop = list()
for i in range(nPop):
	b = Bee(VarMin,VarMax,nVar)
	pop.append(b)
	if pop[i].Cost < best_bee.Cost:
		best_bee = pop[i]

# start timer
tic()

# strat loop
for it in range(MaxIt):
	# Recruited Bees
	for i in range(nPop):
		# choose k randomly, not equal to i
		K = np.concatenate((np.arange(i),np.arange(i+1,nPop)),0)
		k = K[np.random.randint(0,nPop-1)]

		# define acceleration coeff
		phi = a*np.random.uniform(-1,1,nVar)

		# update  new_bee
		new_bee.update(pop[i],pop[k],phi)

		# comparison
		if new_bee.Cost < pop[i].Cost:
			pop[i].copy(new_bee)
		else:
			c[i] += 1

	# calculate fitness values and selection probabilities
	f = np.zeros(nPop)
	mean_cost = 0
	for p in pop:
		mean_cost += p.Cost
	mean_cost /= nPop
	for i in range(nPop):
		f[i] = np.exp(-pop[i].Cost/mean_cost)
	p = f/np.sum(f);

	# Onlooker bees
	for j in range(nPop):
		i = roulette_wheel_selection(p)

		# choose k randomly, not equal to i
		K = np.concatenate((np.arange(i),np.arange(i+1,nPop)),0)
		k = K[np.random.randint(0,nPop-1)]

		# define acceleration coeff
		phi = a*np.random.uniform(-1,1,nVar)

		# update  new_bee
		new_bee.update(pop[i],pop[k],phi)

		# comparison
		if new_bee.Cost < pop[i].Cost:
			pop[i].copy(new_bee)
		else:
			c[i] += 1

	# scout bees
	for i in range(2):
		if c[i] >= L:
			pop[i] = Bee(VarMin,VarMax,nVar)
			c[i] = 0

	# update best solution ever found
	for i in range(nPop):
		if pop[i].Cost < best_bee.Cost:
			best_bee = pop[i]

	# update history
	history[it] = best_bee.Cost

	# Display iteration information
	print("Iteration: %d Best Cost = %s" %(it+1,history[it]))
	# end loop

# stop timer
toc()

# plot graph
plt.plot(history)
plt.ylabel('Cost')
plt.xlabel('Iteration')
plt.grid(color='red',linestyle='--',linewidth='0.5')
plt.show()













