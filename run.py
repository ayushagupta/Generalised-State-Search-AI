import problem
import search
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
	s.inputHeuristic()
	
	print("\nDictionary: "+str(s.dt))
	print("Variables: "+str(s.variables))
	print("Rules: "+str(s.rules))
	print("Rule Conditions: "+str(s.rule_conditions))
	print("Rule costs: "+str(s.rule_cost))
	print("Heuristic function: "+str(s.heuristic))
	
	s.inputStartState()
	s.inputGoalState()

	print("\nStart: "+str(s.dt))
	print("Goal: "+str(s.goal))
	print()

	f = search.Search(s)
	print(f.aSearch())

if __name__=="__main__":
	main()
