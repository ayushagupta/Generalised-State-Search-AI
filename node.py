from queue import Queue
from copy import deepcopy
import problem

class Node:
	def __init__(self, state, parent=None, move=""):
		self.state = state
		self.parent = parent
		self.cost = 0
		if parent is None:
			self.moves = str(move)
			self.cost = 0
		else:
			self.moves = parent.moves + " " + str(move)
			self.cost = self.parent.cost + self.state.evaluateRuleCost(move, parent.state)

	def goalState(self):
		return self.state.checkGoalState()

	def costHeuristic(self):
		return self.state.evaluateHeuristic()

	def childGen(self):
		children = Queue()
		print("Children:")
		for r in range(len(self.state.rules)):
			temp = deepcopy(self.state)
			check = temp.executeRule(r, self.state)			
			if check:
				print(temp.dt)
				children.put(Node(temp, self, r))
		return children

	def __str__(self):
		return "Moves list: "+str(self.moves)

