num1 = 20
num2 = 24

"""
for loop method
"""
# if num1 > num2:
#     smaller = num2
# else:
#     smaller = num1
# for i in range(1, smaller + 1):
#     # print(i)
#     if (num1 % i == 0) and (num2 % i == 0):
#         hcf = i
# print(hcf)
"""
Euclidean Algorithm
"""
def compute_hcf(x, y):
    print(f"x = {x}, y = {y}")
    while(y):        
        x, y = y, x % y
        print(f"x = {x}, y = {y}")
    return x

print(compute_hcf(54, 24))