
num = int(input("Enter a no: "))

sum = 0
temp = num
n = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if num == sum:
    print(True)
else:
    print(False)






