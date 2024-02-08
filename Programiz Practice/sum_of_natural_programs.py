"""
Mathematical equation method
n * (n + 1) / 2
"""
num = 2
sum = num * (num + 1) / 2
print(f"number = {num}, sum = {sum}")

"""
while loop
"""
# num = 2

if num <= 0:
    print("Enter a +ve no")
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1 
    print(f"sum = {sum}")

"""
Recursion method
"""
def sum_n(num):
    if num == 1:
        return 1
    return num + sum_n(num - 1)
print(sum_n(2))