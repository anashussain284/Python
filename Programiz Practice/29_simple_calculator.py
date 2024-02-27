def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print("Select operation.")
print("1. Addition")
print("2. Subtract")
print("3. Multiplication")
print("4. Division")

while True:
    choice  = int(input("Enter choice(1/2/3/4): "))

    if choice in [1, 2, 3, 4]:
        try:
            num1 = float(input("Enter first no: "))
            num2 = float(input("Enter second no: "))
        except ValueError:
            print("Invalid input. Please enter a no.")

        if choice == 1:
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == 2:
            print(f"{num1} - {num2} = {sub(num1, num2)}")
        elif choice == 3:
            print(f"{num1} * {num2} = {mul(num1, num2)}")
        elif choice == 4:
            print(f"{num1} / {num2} = {div(num1, num2)}")
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid input")