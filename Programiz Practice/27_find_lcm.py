x = 54; y = 24

# if x > y:
#     greater = x
# else:
#     greater = y

# while (True):
#     if (greater % x == 0) and (greater % y == 0):
#         lcm = greater
#         break
#     greater += 1
# print(lcm)

"""
GCD method
equation is num1 * num2 = LCM * GCD
"""
def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
# gcd = find_gcd(x, y)

# product_of_no = x * y
# lcm = product_of_no // gcd
# print(f"GCD = {gcd}, LCM  = {lcm}")

def find_lcm(x, y):
    return (x * y) // find_gcd(x, y)

print(find_lcm(x, y))