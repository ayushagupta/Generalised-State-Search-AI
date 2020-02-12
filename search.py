from queue import PriorityQueue
import problem
import node

class Search:
	def __init__(self, problem):
		self.start = node.Node(problem)

	def aSearch(self):
		current = self.start
		node_count = 1
		open_list = PriorityQueue()
		open_list.put((current.costHeuristic(), node_count, current))
		closed_list = []
		

		while True:
			if open_list.empty():
				return None
			current = open_list.get()[2]
			print("Top of open: " + str(current.state.dt))
			print("Current Cost: " + str(current.cost))
			if current.goalState():
				print("\nGoal reahced with cost: "+str(current.cost))
				print("Number of nodes explored: "+str(node_count))
				return current
			elif current.state.dt not in closed_list:
				closed_list.append(current.state.dt)
				children = current.childGen()
				while not children.empty():
					node_count += 1
					child = children.get()
					open_list.put((child.costHeuristic()+child.cost, node_count, child))
					