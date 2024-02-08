"""
Prime no: A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number. 2, 3, 5, 7 etc. are prime numbers as they do not have any other factors. But 6 is not prime (it is composite) since, 2 x 3 = 6
"""

num = 29

# using flag method
# flag = False

# if num == 1:
#     print(num, "is not a prime number")
# elif num >= 2:
#     for i in range(2, num):
#         if num % i == 0:
#             flag = True
#             break
#     if flag:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")

# using for else statement
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")