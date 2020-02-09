from queue import Queue
from copy import deepcopy
import problem

class Node:
	def __init__(self, state, parent=None, move=None):
		self.state = state
		self.parent = parent
		self.cost = 0
		self.moves = []
		if parent is not None:
			self.moves.append(move)
			self.cost = parent.cost + state.rule_cost[move]

	def goalState(self):
		return self.state.checkGoalState()

	def costHeuristic(self):
		return self.state.evaluateHeuristic()

	def childGen(self):
		children = Queue()
		for r in range(len(self.state.rules)):
			temp = deepcopy(self.state)
			check = temp.executeRule(r, self.state)
			if check:
				children.put(Node(temp, self, r))
			return children

	def __str__(self):
		return str(self.moves)

