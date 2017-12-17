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

class PSO():
	def __init__(self,pb):
		self.Pos = np.random.uniform(pb['VarMin'],pb['VarMax'],pb['nVar'])
		self.Vel = np.zeros(pb['nVar'])
		self.Cost = cost_function(self.Pos)
		self.BestPos = self.Pos
		self.BestCost = self.Cost

	def update(self,pb,pr,gb_pos):
		self.Vel = pr['w']*self.Vel+pr['c1']*np.multiply(np.random.rand(pb['nVar']),self.BestPos-self.Pos)+pr['c2']*np.multiply(np.random.rand(pb['nVar']),gb_pos-self.Pos)
		self.Vel = np.maximum(self.Vel,pb['VelMin'])
		self.Vel = np.minimum(self.Vel,pb['VelMax'])

		self.Pos = self.Pos + self.Vel
		self.Pos = np.maximum(self.Pos,pb['VarMin'])
		self.Pos = np.minimum(self.Pos,pb['VarMax'])

		self.Cost = cost_function(self.Pos)

		# update personal best
		if self.Cost < self.BestCost:
			self.BestCost = self.Cost
			self.BestPos = self.Pos



