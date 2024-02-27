"""
In the program below, we have used anonymous (lambda) function inside the filter() built-in function to find all the numbers divisible by d in the list.
"""
y = [12, 65, 54, 39, 102, 339, 221,]
d = 5

result = list(filter(lambda x : (x % d == 0), y))

print(result)