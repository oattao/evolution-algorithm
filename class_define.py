# define bee Class
import numpy as np
from fn import cost_function

class Bee():
	def __init__(self,VarMin=None,VarMax=None,nVar=None):
		if nVar != None:
			self.Position = np.random.uniform(low=VarMin,high=VarMax,size=nVar)
			self.Cost = cost_function(self.Position)
		else:
			self.Position = None
			self.Cost = None

	def update(self,bee_a,bee_b,phi):
		self.Position = bee_a.Position+phi*(bee_a.Position-bee_b.Position)
		self.Cost = cost_function(self.Position)

	def copy(self,bee):
		self.Position = bee.Position
		self.Cost = bee.Cost
