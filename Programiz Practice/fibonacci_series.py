x = int(input("Enter no. of fibonacci series: "))

n1, n2 = 0, 1
count = 0

if x <= 0:
    print(f"Please try with a +ve no")
elif x == 1:
    print(n1)
else:
    while (count < x):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(3))