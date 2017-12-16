def tic():
	import time
	global startTime_for_tictoc
	startTime_for_tictoc = time.time()

def toc():
	import time
	import math
	if 'startTime_for_tictoc' in globals():
		dt = math.floor(100*(time.time()-startTime_for_tictoc))/100
		print('Elapsed time is {} second(s)'.format(dt))

def roulette_wheel_selection(p):
	import numpy as np
	r = np.random.uniform(0.0,1.0)
	c = np.cumsum(p)
	wh = np.where(r <= c)
	return wh[0][0]
