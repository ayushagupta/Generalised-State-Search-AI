import problem

def inputVar(s):
	num = int(input("Enter number of variables: "))
	for i in range (num):
		print("\n****Variable "+str(i+1)+"****")
		s.inputVariable()


s = problem.State()
inputVar(s)
print(s.dictionary)
print(s.variables)