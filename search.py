from queue import PriorityQueue
import problem
import node

class Search:
	def __init__(self, problem):
		self.start = node.Node(problem)

	def aSearch(self):
		current = self.start
		open_list = PriorityQueue()
		open_list.put(current.costHeuristic(), current)
		closed_list = []

		while True:
			if open_list.empty():
				return None
			current = open_list.get()[1]
			if current.goalState():
				return current
			elif current.state.dt not in closed_list:
				closed_list.append(current.state.dt)
				children = current.childGen()
				while not children.empty():
					child = children.get()
					open_list.put(child.costHeuristic()+child.cost, child)