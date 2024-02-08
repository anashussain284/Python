"""
The factorial of a number is the product of all the integers from 1 to that number.

For example, the factorial of 6 is 1*2*3*4*5*6 = 720. Factorial is not defined for negative numbers, and the factorial of zero is one, 0! = 1
"""

# number using loop
# num = 7
# factorial = 1

# if num < 0:
#     print("factorial doesn't exist -ve no")
# elif num == 0:
#     print("factorial = ", 1)
# else:
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"factorial of {num} = {factorial}")
    
# number using recursion
def factorial(x):
    if x == 1:
        print(f"x in `x == 1` = {x}")
        return 1
    else:
        print(f"x in `x != 1` = {x}")
        y = x * factorial(x - 1)
        print(f"y = {y}")
        return y

num = 3

result = factorial(num)
print("**************")
print(result)
print("**************")