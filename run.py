import problem
from copy import deepcopy

def inputVar(s):
	num = int(input("Enter number of variables: "))
	for i in range (num):
		print("\n****Variable "+str(i+1)+"****")
		s.inputStateVariable()

def inputRules(s):
	num = int(input("\nEnter number of rules: "))
	for i in range (num):
		print("\n****Rule "+str(i+1)+"****")
		s.inputTransitionRules()


def main():
	s = problem.State()
	inputVar(s)
	inputRules(s)
	print(s.d)
	print(s.variables)
	print(s.rules)
	s.inputStartState()
	
	g = deepcopy(s)
	g.inputGoalState()

	print(s.d)
	print(g.d)

if __name__=="__main__":
	main()
