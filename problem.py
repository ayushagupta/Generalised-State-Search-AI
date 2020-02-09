import math
from copy import deepcopy

class State:
	def __init__(self):
		self.dt = {}
		self.variables = []
		self.rules = []
		self.rule_conditions = []
		self.rule_cost = []
		self.heuristic = ""
		self.goal = {}

	def input_variable_int(self):
		lower_bound = int(input("Enter lower bound of the integer variable: "))
		upper_bound = lower_bound-1;
		while upper_bound < lower_bound:
			upper_bound = int(input("Enter upper bound of the integer variable: "))
		domain = (lower_bound, upper_bound)
		return domain

	def input_variable_float(self):
		lower_bound = float(input("Enter lower bound of the float variable: "))
		upper_bound = lower_bound-1;
		while upper_bound < lower_bound:
			upper_bound = float(input("Enter upper bound of the integer variable: "))
		domain = (lower_bound, upper_bound)         
		return domain

	def input_variable_list(self):
		temp_type = int(input("Enter data type of list elemets: "))
		if temp_type == 1:
			domain = self.input_variable_int()
		elif temp_type == 2:
			domain = self.input_variable_float()

		size = int(input("Enter number of elements in the list: "))
		return (temp_type, size, domain)


	def inputStateVariable(self):
		name = input("Enter name of variable: ")
		print("1. int")
		print("2. float")
		print("3. list")
		type = [int(input("Enter data type: ")), 0, 0]
		if type[0] == 1:
			domain = self.input_variable_int()
			
		elif type[0] == 2:
			domain = self.input_variable_float()

		else:
			list_properties = self.input_variable_list()
			type[1] = list_properties[0]
			type[2] = list_properties[1]
			domain = list_properties[2]

		self.dt[name] = {'type':type, 'val':0, 'domain': domain, 'constraints': []}
		self.variables.append(name)


	def inputRuleConditions(self):
		num_cond = int(input("Enter number of conditions to be fulfilled for this rule: "))
		temp_cond = []
		for i in range (num_cond):
			exp = input("Enter condition: ")
			exp = exp.replace("dt[", "self.dt[")
			temp_cond.append(exp)
		self.rule_conditions.append(temp_cond)

	def inputRuleCost(self):
		temp_cost = float(input("Enter cost of using this rule: "))
		self.rule_cost.append(temp_cost)


	def inputTransitionRules(self):
		print("Rules are input in the form: a = F(x1,x2,x3,...)")
		print("Example for using variable with name a in F: dt['a']['val']")
		num_steps = int(input("Enter number of steps in the rule: "))
		temp_rule = []
		for i in range (num_steps):
			print("**Step "+str(i+1)+"**")
			lhs = input("Enter variable a: ")
			exp = input("Enter expression F: ")
			exp = exp.replace("dt[", "parent.dt[")
			temp_rule.append((lhs, exp))
		self.rules.append(temp_rule)
		self.inputRuleConditions()
		self.inputRuleCost()
		

	def inputIntegerValue(self, variable_name):
		return int(input("Enter integer value of "+variable_name+": "))

	def inputFloatValue(self, variable_name):
		return float(input("Enter float value of "+variable_name+": "))

	def inputStateValues(self,dt):
		for i in range (len(self.variables)):
			if dt[self.variables[i]]['type'][0] == 1:
				dt[self.variables[i]]['val'] = self.inputIntegerValue(self.variables[i])
			elif dt[self.variables[i]]['type'][0] == 2:
				dt[self.variables[i]]['val'] = self.inputFloatValue(self.variables[i])
			else:
				for j in range (dt[variables[i]]['type'][2]):
					if dt[self.variables[i]]['type'][1] == 1: 
						dt[self.variables[i]]['val'][j] = self.inputIntegerValue(self.variables[i])
					elif dt[self.variables[i]]['type'][1] == 2:
						dt[self.variables[i]]['val'][j] = self.inputFloatValue(self.variables[i])

	def inputStartState(self):
		print("\nEnter initial values of the state variables:")
		self.inputStateValues(self.dt)

	def inputGoalState(self):
		self.goal = deepcopy(self.dt)
		print("\nEnter final values of the state variables:")
		self.inputStateValues(self.goal)

	def checkGoalState(self):
		for i in range (len(self.variables)):
			if self.dt[self.variables[i]]['type'][0] == 1:
				if self.dt[self.variables[i]]['val'] != self.goal[self.variables[i]]['val']:
					return False
			
			elif self.dt[self.variables[i]]['type'][0] == 2:
				if not math.isclose(self.dt[self.variables[i]]['val'], self.goal[self.variables[i]]['val'], abs_tol=0.000001):
					return False

			else:
				for j in range (self.dt[self.variables[i]]['type'][2]):
					if self.dt[self.variables[i]]['type'][1] == 1:
						if self.dt[self.variables[i]]['val'][j] != self.goal[self.variables[i]]['val'][j]:
							return False

					elif self.dt[self.variables[i]]['type'][1] == 2:
						if not math.isclose(self.dt[self.variables[i]]['val'][j], self.goal[self.variables[i]]['val'][j], abs_tol=0.000001):
							return False

		return True

	def inputHeuristic(self):
		h = input("\nEnter heuristic function in terms of current and goal variables: ")
		h = h.replace("goal[", "self.goal[")
		h = h.replace("dt[", "self.dt[")
		self.heuristic = h

	def evaluateHeuristic(self):
		return eval(self.heuristic)

	def domainCheck(self):
		for i in range(len(self.variables)):
			if i == 3:
				for j in range(self.dt[self.variables[i]]['type'][2]):
					if self.dt[self.variables[i]]['val'][j]>self.dt[self.variables[i]]['domain'][1] or self.dt[self.variables[i]]['val'][j]<self.dt[self.variables[i]]['domain'][0]:
						return False

			else:
				if self.dt[self.variables[i]]['val']>self.dt[self.variables[i]]['domain'][1] or self.dt[self.variables[i]]['val']<self.dt[self.variables[i]]['domain'][0]:
					return False


	def executeRule(self, r, parent):
		for i in range(len(self.rule_conditions[r])):
			if not eval(self.rule_conditions[r][i]):
				return False

		for i in range(len(rules[r])):
			self.dt[rules[r][0]]['val'] = eval(self.rules[r][1])
		
		if not self.domainCheck():
			return False

		return True

