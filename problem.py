class State:
	def __init__(self):
		self.d = {}
		self.variables = []
		self.rules = []

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

		self.d[name] = {'type':type, 'val':0, 'domain': domain, 'constraints': []}
		self.variables.append(name)


	def inputTransitionRules(self):
		print("Rules are input in the form: a = F(x1,x2,x3,...)")
		print("Example for using variable with name a in F: d['a']['val']")
		num_steps = int(input("Enter number of steps in the rule: "))
		temp_rule = []
		for i in range (num_steps):
			print("**Step "+str(i+1)+"**")
			lhs = input("Enter variable a: ")
			exp = input("Enter expression F: ")
			temp_rule.append((lhs, exp))
		self.rules.append(temp_rule)
		

	def inputIntegerValue(self, variable_name):
		return int(input("Enter integer value of "+variable_name+": "))

	def inputFloatValue(self, variable_name):
		return float(input("Enter float value of "+variable_name+": "))

	def inputStateValues(self):
		for i in range (len(self.variables)):
			if self.d[self.variables[i]]['type'][0] == 1:
				self.d[self.variables[i]]['val'] = self.inputIntegerValue(self.variables[i])
			elif self.d[self.variables[i]]['type'][0] == 2:
				self.d[self.variables[i]]['val'] = self.inputFloatValue(self.variables[i])
			else:
				for j in range (self.d[variables[i]]['type'][2]):
					if self.d[self.variables[i]]['type'][1] == 1: 
						self.d[self.variables[i]]['val'][j] = self.inputIntegerValue(self.variables[i])
					elif self.d[self.variables[i]]['type'][1] == 2:
						self.d[self.variables[i]]['val'][j] = self.inputFloatValue(self.variables[i])

	def inputStartState(self):
		print("\nEnter initial values of the state variables:")
		self.inputStateValues()

	def inputGoalState(self):
		print("\nEnter final values of the state variables:")
		self.inputStateValues()