# Take in a number and returns the factorial of that number
# Author :Jerry Huang
#Using a for loop

#The function of calculate the factorial
def factorial(number):
	result = 1
        
	for i in range(1, number+1):
		result *= i
	
	return result

# Let the user to enter a number
num = int(input("Please enter a number larger that 1: "))

# Calling the function
fac = factorial(num)

# print the result
print(fac)
