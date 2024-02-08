import math

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b ** 2) - (4 * a * c)

# solution 1 
sol1 = (-b + math.sqrt(d) / 2 * a)
sol2 = (-b - math.sqrt(d) / 2 * a)

print(f"sol1 = {sol1}")
print(f"sol2 = {sol2}")