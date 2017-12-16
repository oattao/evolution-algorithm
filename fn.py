# need to be optimized function
def cost_function(x):
	import numpy as np
	# return np.sum(np.square(x))
	return np.sum(np.square(x)-10*np.cos(2*np.pi*x)+10)



