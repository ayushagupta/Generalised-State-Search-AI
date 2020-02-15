import math
from copy import deepcopy

class State:
	def __init__(self):
		self.dt = {}
		self.variables = []
		self.rules = []
		self.rule_conditions = []
		self.rule_cost = []
		self.constraints = []
		self.heuristic = ""
		self.goal = {}
		self.forbidden = []

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
			val = 0
			
		elif type[0] == 2:
			domain = self.input_variable_float()
			val = 0.0

		else:
			list_properties = self.input_variable_list()
			type[1] = list_properties[0]
			type[2] = list_properties[1]
			domain = list_properties[2]
			val = []
			for i in range (type[2]):
				if type[1] == 1:
					val.append(0)
				else:
					val.append(0.0)

		self.dt[name] = {'type':type, 'val':val, 'domain': domain}
		self.variables.append(name)


	def inputRuleConditions(self):
		num_cond = int(input("Enter number of conditions to be fulfilled for this rule: "))
		temp_cond = []
		for i in range (num_cond):
			exp = input("Enter condition: ")
			exp = exp.replace("['", "self.dt['")
			exp = exp.replace("']", "']['val']")
			temp_cond.append(exp)
		self.rule_conditions.append(temp_cond)

	def inputRuleCost(self):
		temp_cost = input("Enter cost of using this rule: ")
		temp_cost = temp_cost.replace("['", "parent.dt['")
		temp_cost = temp_cost.replace("']", "']['val']")
		self.rule_cost.append(temp_cost)


	def inputTransitionRules(self):
		print("Rules are input in the form: a = F(x1,x2,x3,...)")
		print("Example for using variable with name a in F: ['a']")
		num_steps = int(input("Enter number of steps in the rule: "))
		temp_rule = []
		for i in range (num_steps):
			print("**Step "+str(i+1)+"**")
			lhs = input("Enter variable on LHS: ")
			if self.dt[lhs]['type'][0] == 3:
				ele = int(input("Enter element of the list: "))
			else:
				ele = -1
			exp = input("Enter expression on RHS: ")
			exp = exp.replace("['", "parent.dt['")
			exp = exp.replace("']", "']['val']")
			temp_rule.append((lhs, ele, exp))
		self.rules.append(temp_rule)
		self.inputRuleConditions()
		self.inputRuleCost()

	def inputConstraints(self):
		num_constraints = int(input("\nEnter number of constraints: "))
		for i in range(num_constraints):
			temp_constraint = input("Enter constraint "+str(i+1)+": ")
			temp_constraint = temp_constraint.replace("['", "self.dt['")
			temp_constraint = temp_constraint.replace("']", "']['val']")
			self.constraints.append(temp_constraint)
		

	def inputIntegerValue(self, variable_name):
		return int(input("Enter integer value of "+variable_name+": "))

	def inputFloatValue(self, variable_name):
		return float(input("Enter float value of "+variable_name+": "))

	def inputStateValues(self,dit):
		for i in range (len(self.variables)):
			if dit[self.variables[i]]['type'][0] == 1:
				dit[self.variables[i]]['val'] = self.inputIntegerValue(self.variables[i])
			elif dit[self.variables[i]]['type'][0] == 2:
				dit[self.variables[i]]['val'] = self.inputFloatValue(self.variables[i])
			else:
				for j in range (dit[self.variables[i]]['type'][2]):
					if dit[self.variables[i]]['type'][1] == 1: 
						dit[self.variables[i]]['val'][j] = self.inputIntegerValue(self.variables[i])
					elif dit[self.variables[i]]['type'][1] == 2:
						dit[self.variables[i]]['val'][j] = self.inputFloatValue(self.variables[i])

	def inputStartState(self):
		print("\nEnter initial values of the state variables:")
		self.inputStateValues(self.dt)

	def inputGoalState(self):
		self.goal = deepcopy(self.dt)
		print("\nEnter final values of the state variables:")
		self.inputStateValues(self.goal)

	def inputForbiddenState(self):
			temp_dt = deepcopy(self.dt)
			self.inputStateValues(temp_dt)
			self.forbidden.append(temp_dt)

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
		print("\nEnter heuristic function in terms of current and goal variables")
		h = input("Use {} for goal variables and [] for current variables: ")
		h = h.replace("['", "self.dt['")
		h = h.replace("{'", "self.goal['")
		h = h.replace("'}", "']")
		h = h.replace("']", "']['val']")
		self.heuristic = h

	def evaluateHeuristic(self):
		return eval(self.heuristic)

	def domainCheck(self):
		for i in range(len(self.variables)):
			if self.dt[self.variables[i]]['type'][0] == 3:
				for j in range(self.dt[self.variables[i]]['type'][2]):
					if self.dt[self.variables[i]]['val'][j]>self.dt[self.variables[i]]['domain'][1] or self.dt[self.variables[i]]['val'][j]<self.dt[self.variables[i]]['domain'][0]:
						return False

			else:
				if self.dt[self.variables[i]]['val']>self.dt[self.variables[i]]['domain'][1] or self.dt[self.variables[i]]['val']<self.dt[self.variables[i]]['domain'][0]:
					return False
		return True

	def constraintCheck(self):
		for i in range (len(self.constraints)):
			if not eval(self.constraints[i]):
				return False
		return True

	def forbiddenCheck(self):
		if self.dt in self.forbidden:
			return False
		return True


	def executeRule(self, r, parent):
		for i in range(len(self.rule_conditions[r])):
			if not eval(self.rule_conditions[r][i]):
				return False
		for i in range(len(self.rules[r])):
			if self.rules[r][i][1] == -1:
				self.dt[self.rules[r][i][0]]['val'] = eval(self.rules[r][i][2])
			else:
				self.dt[self.rules[r][i][0]]['val'][self.rules[r][i][1]] = eval(self.rules[r][i][2])
		return self.domainCheck() and self.constraintCheck() and self.forbiddenCheck()

	def evaluateRuleCost(self, r, parent):
		return eval(self.rule_cost[r])
