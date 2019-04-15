# This is just a file of basic functions

# function decleration
def test_function():
	# iterator loops
	for x in range(0,5):
		# conditionals
		if x % 2 == 0:
			# print and casting
			print("Hello " + str(x))


# function with parameters
def test_function_params(testNum):
	print(str(testNum))

# calling a function
test_function()

# calling a function with parameters
test_function_params(2)
test_function_params(10000)

# array
testArray = [1, 2, 3, 4, 5]
# array iteration
for x in testArray:
	print(x)