# Take in a number and returns the factorial of that number
# Author :Jerry Huang
#Using a while loop

#The function of calculate the factorial
def factorial(number):
        result = 1
        while number > 1:
                result *= number
                number -= 1
        return result


# Let the user to enter a number
num = int(input("Please enter a number larger that 1: "))

# Calling the function
fac = factorial(num)

#print out the result
print(fac)
