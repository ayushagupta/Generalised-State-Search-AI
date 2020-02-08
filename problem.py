class State:
	def __init__(self):
		self.dictionary = {}
		self.variables = []

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
		print("3. char")
		print("4. bool")
		print("5. list")
		type = [int(input("Enter data type: ")), 0, 0]
		if type[0] == 1:
			domain = self.input_variable_int()
			
		elif type[0] == 2:
			domain = self.input_variable_float()

		elif type[0] == 5:
			list_properties = self.input_variable_list()
			type[1] = list_properties[0]
			type[2] = list_properties[1]
			domain = list_properties[2]

		else: 
			domain = 0

		
		self.dictionary[name] = [type, 0, domain, [], []]
		self.variables.append(name)

		

