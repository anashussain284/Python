import random

# print("Hello world")

# a = "anas"
# A = "anas"

# print(a, id(a), type(a))
# print(A, id(A), type(A))

# a, b, c = "P", "Q", "R"
# a = b = c = "Z"
# print(a, b, c)

# no = [1, 2, 3]
# x, y , z = no
# print(x, y, z)

# a = 1
# b = "1"

# print(a, b)
# print(a + int(b))

# a = "AAA"

# print(a, "is super - 1", id(a))

# def myfun():
#     global a
#     a = "BBB"
#     print(a, "is super - 2", id(a))

# myfun()
# print(a, "is super - 3", id(a))

# x = 1j
# print(type(x))

# x = memoryview(bytes(0))

# x = 35e101
# x = 12E-4
# x = 87.17e5

# x = random.randrange(1, 3)

# print(x, type(x))

# x = "0123456789"
# # print(x[0])
# for i in x:
#     print(i)

# print(len(x))

# print("el" not in x)
# print(x[-6:-5])

# x = "A'n,a,s"
# print(x.split("'"))

# name = "Anas"
# salary = "5 lakhs"
# frame1 = "My name is {}, my salary is {} rupees"
# str1 = frame1.format(name, salary)
# # print(name, str1)
# print(str1)


# print()
# frame2 = "My name is {}. I'm coming from {}, I have {} brother and {} sister"
# place = "ernakulam"
# bro_count = 1
# sis_count = 1
# str2 = frame2.format(name, place, bro_count, sis_count)
# print(frame2)
# print(str2)

# txt = "Hello \fAnas\f"
# print(txt)

# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool({}))

# class myclass():
#     def __len__(self):
#         return 1
    
# myobj = myclass()
# print(bool(myobj))

# x = {'no':'20.0'}
# print(isinstance(x, dict))

# x = 10
# print(x)
# x%=7
# print(x)

# x = [1, 2]
# y = [1, 2]
# z = x
# print(x, id(x))
# print(y, id(y))
# print(z, id(z))

# print(x is y, x is not y)
# print(y is z, y is not z)
# print(x is z, x is not z)

# print(x == y)
# print(x == z)

# x = [1, 2.0, '3', True, ]

# print(10 not in x)
# print(len(x), type(x))

# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(x[2::2])
# print(x[5])
# print(x[-1])
# print(x[-4:-1]) # exp o/p = [3, 4, 5]
# print(x[-7:-1:2]) # exp o/p = [4, 6, 8]

# print(100 not in x)

# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("b4:", x, len(x))
# # x[9::] = [1, "a", "b", "c", 1]
# x[:4] = ["a"]
# print("a4:", x, len(x))

# x = [0, 1, 2, 3, 4]
# print("b4:", x, len(x))
# # x.insert(2, [1, 2])
# x.append((1, 2, 3))
# print("a4:", x, len(x))

# x = [1, 2, 3]
# y = ("a", "b", "c")
# print("x:", x)
# print("y:", y)
# print()

# x.extend(y)
# print("x:", x)
# print("y:", y)
# print()

# y.extend(x)
# print("x:", x)
# print("y:", y)
# print()

# x = [0, 1, 2, 0, 3, 4]
# print(len(x), "nos => b4:", x)
# x.remove(0)
# x.pop()
# del x[1]
# del x
# x.clear()
# print(len(x), "nos => a4:", x)

# x = [0, 1, 2, 0, 3, 4]
# x = ["a", "b", "c", "d"]
# print(len(x), "nos => b4:", x)
# print(len(x), "nos => a4:", x)

# for i in range(len(x)):
#     print(i, x[i])

# i = 0

# while i < len(x):
#     print(x[i])
#     i+=1

# [print(a, ":", x[a]) for a in range(len(x))]

# fruits = ["apple", "banana", "Apple", "orange", "cherry", "pineapple", "musambi", "mathalam", "watermelon", "grapes", "strawberry", "apple"]
# print(fruits)

# a = []

# for f in fruits:
#     # print(f)
#     if "b" in f:
#         a.append(f)

# print(a)
    
# b = [f for f in fruits if "w" in f]

# # print(b)


# c = [x for x in fruits if x == "apple"]
# print(c)

# a = [i for i in range(1, 11)]
# print(a)
# print(a[4::2])

# print odd no's upto 20
# a = [i for i in range(21) if i % 2 != 0]
# print(a)

# x = [f.capitalize() for f in fruits]
# x = [f*2 for f in fruits]
# print(fruits)
# x = [f if f!= "banana" else "mathanga" for f in fruits]
# x = [f if f != "apple" else "*" for f in fruits]
# print(x)

# def myfunction(n):
#     # return abs(n - 50)
#     a = abs(n - 10)
#     print(a)
#     return a

# x = ["banana", "Orange", "Kiwi", "cherry"]
# print(x)
# print("b4:", x)
# x.sort(key=str.lower)
# x.reverse()
# x.sort()
# x.sort(key = str.lower)
# x.sort(reverse=True)
# x.sort(key = myfunction)
# print("a4:", x)

# x = [1, 2, 3]
# # y = x
# # y = x.copy()
# y = list(x)
# y[0] = 8
# print(id(x), x)
# print(id(y), y)

# x = [1, 2, 3]
# y = ["a", "b", "c"]
# z = x + y
# [x.append(i) for i in y]
# z = x

# print(x)
# x.extend(y)
# print(x)
# print(y)
# print(z)

# x = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(len(x), x)

# x = (1,)
# print(x, type(x))
# print()
# print(isinstance(x, tuple))

# print(x[-10])

# print(x[-4:-1]) # [6, 7, 8]
# print(100 not in x)
# x = (0, 1, 2, 3)
# print(x)
# x = list(x)
# x[0] = True
# x = tuple(x)
# print(x)

# x = (1, 2, 3)
# y = (7,)
# z = x + y

# print(x)
# del x
# print(x)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (a, b , *c, d, e, f) = fruits
# print(fruits)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# for f in fruits:
#     print(f)

# for i in range(len(fruits)):
#     print(i, ":", fruits[i])

# i = 0

# while i < len(fruits):
#     print(i, fruits[i])
#     i+=1

# print(fruits*2)
# x = {1, 2, 3}
# print(x)
# print(x*2)

# x = (1, 3, 7, 18, 7, 5, 4, 6, 8, 5)
# print(x.count(5))
# print(x.index(8))

# x = {0, 1, "a", True, False, 0, "a", 2, 3, 1}
# print(x, len(x))
# print(isinstance(x, set))
# for y in x:
#     print(y)

# for y in x:
#     print(y)

# print(20 in x)

# x = {1, 2, 3}
# print(x, id(x))
# x.add(99)
# print(x, id(x))
# y = (11, 22, 33)
# x.update(y)
# x.update(99)
# x.clear()
# del x
# print(x, id(x))     
# y = {"a", "b", "c", 1}
# x.update(y)

# z = x.symmetric_difference(y)
# x.symmetric_difference_update(y)

# print(x)
# print(y)
# print(z)

# x = {
#     "name": "Anas",
#     "place": "ekm",
#     "year": "2024",
#     "profession": "IT"
# }
# x["test"] = "Pqr"

# print(len(x), x)
# print()
# print(x["name"])
# print(x.get("name"))
# print(x.keys())
# print(x.values())
# print()
# print(x.items())
# print()
# print("Name" in x)
# print()

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# # thisdict.update({"year": 2020, "brand":"pqr"})
# thisdict.update(dict(("name""anas")))
# print()
# print(thisdict)
# x.pop("name")
# x.popitem()
# del x["abc"]
# del x
# x.clear()
# print(len(x), x)

# for y in x:
#     print(y, x[y])

# for y in x.keys():
#     print(y)

# for y in x.values():
#     print(y)

# for y, z in x.items():
#     print(y, z)

# x = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(id(x), x)
# # y = x
# # y = x.copy()
# y = dict(x)
# print(id(y), y)

# family = {
#     "child1": {
#         "name": "child1_name",
#         "place": "child1_place",
#         "age": "child1_age"
#     },
#     "child2": {
#         "name": "child2_name",
#         "place": "child2_place",
#         "age": "child2_age"
#     },
#     "child3": {
#         "name": "child3_name",
#         "place": "child3_place",
#         "age": "child3_age"
#     }
# }

# print(family)
# print()
# print(family["child1"]["name"])

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.setdefault("model2", "Bronco")

# print(x)

# x = ("key1", "key2", "key3")
# y = {1}
# z = dict.fromkeys(x, y)

# print(x)
# print(y)
# print(z)

# x = 0

# if x > 0:
#     print(x, "is +ve")
# elif x < 0:
#     print(x, "is -ve")
# else:
#     print(x, "is zero")

# if 11 > 2: print("T")

# print("T") if 11 > 12 else print("F")

# x = 4

# print(1) if x == 1 else print(2) if x == 2 else print(3) if x == 3 else print("None")

# if not 1 > 2:
#     print("T")

x = 9

# if x > 10:
#     print(x, "is bigger than 10")

#     if x > 20:
#         print(x, "is bigger than 20")

#         if x > 30:
#             print(x, "is greater than 30")
#         else:
#             print(x, "is less than 30")
#     else:
#         print(x, "is lower than 20")
# else:
#     print(x, "is lower than 10")

# if 1 < 2:
#     pass

# i = 0

# while (i <= 5):
    
#     if (i == 3):
#         # break
#         continue

#     print(i)
#     i+=1

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
# else:
#   print("loop condition is false")

# for i in range(0, 10, 2)    :
#     print(i)
# else:
#     print("loop is finished")

# x = [1, 2, 3]
# y = ["a", "b", "c"]

# for a in x:
#     # for b in y:
#     #     print(a, b)
#     pass

# def print_name(*fname):
#     print(fname[0], "Hussain")

# # print_name("Anas")
# # print_name("Aisha")
    
# names = ["Anas", "Aisha", "Nazeer", "Muhammed"]

# for i in names:
#     print_name(i)

# def my_function(*kids):
#   print("The youngest child is " + kids[0])

# my_function("Emil", "Tobias", "Linus")

# print_name("A", "B", "C")

# def my_function(**abc):
#     print("selected:", abc["place"])
#     # print("selected:", abc[0])

# # pqr = ()
# my_function(name = "anas", place="cochin")
# # my_function("a", "b", "c")

# def test_fn(name = "Nil"):
#     print("Hello", name)

# test_fn("Anas")
# test_fn()

# def test_fn(letters):
#     for i in letters:
#         return i

# letters = ("A", "B", "C")        

# x = test_fn(letters)
# print(x)

# def my_fun(*, x):
#     print(x)

# my_fun(x = 5)

# def tri_recursion(k):
#     if (k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("Recursion example")
# tri_recursion(2)

# lambda arguments : expression
# x = lambda a : a + 10
# print(x(5))

# s = lambda a, b, c, d : a + b + c + d
# print(s(1, 2, 3, 4))

# def my_func(n):
#     return lambda a : a * n

# my_doubler = my_func(3)

# print(my_doubler(22))

# def my_func(n):
#     return lambda a : a * n

# my_doubler = my_func(2)
# my_trippler = my_func(3)

# print(my_doubler(11))
# print(my_trippler(11))

# class MyClass:
#     x = 5

# x = MyClass()
# print(x.x)

# name = input("Enter your name:")
# place = input("Where are you coming from?")

# print(name, "from", place)

# try:
#     num = float(input("Enter a no:"))
# except ValueError:
#     print("Invalid input. Please a valid number.")

# age = 111
# has_license = False

# if age >= 18 and has_license:
#     print("U R allowed to drive")
# elif age >= 18 and not has_license:
#     print("U need a license to drive")
# else:
#     print("U R Not old enough to drive")

# matrix = [
#     [7, 8, 9],
#     [1, 2, 3],
#     [4, 5, 6],
    
# ]

# # print(matrix)
# for row in matrix:
#     # print(row)
#     for col in row:
#         print(col)

# number = 64
# found_divisor = False

# for i in range(2, number):
#     # print(i)
#     if found_divisor:
#         break
#     for j in range(2, number):
#         # print(j)
#         # pass
#         if i * j == number:
#             print("the 1st occurrance for {number} are {i} and {j}")
#             found_divisor = True
#             break

# number = 64
# found_divisor = False

# for i in range(2, number):
#     if found_divisor:
#         break
#     for j in range(2, number):
#         if i * j == number:
#             print(f"The first pair of divisor for {number} are {i} and {j}.")
#             found_divisor = True
#             break

# def power(base, exponent = 2):
#     return base ** exponent

# print(power(3))
# print(power(4))

# def two_sum(nums, target):
#     for i in range(len(nums)):
#         num1 = nums[i]

#         for j in range(i + 1, len(nums)):
#             num2 = nums[j]

#             if num1 + num2 == target:
#                 return [i, j]
            
# list1 = [2, 10, 9, 20, 5, 7]            
# result = two_sum(list1, 11)
# if (result == None):
#     result = "Target not found"
# print(result)

# def contains_duplicate(nums):
#     n = len(nums)
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if nums[i] == nums[j]:
#                 return True
#     return False

# list1 = [1, 2, 3, 4]
# result = contains_duplicate(list1)
# print(result)

# def duplicate2(nums):
#     nums.sort()
#     n = len(nums)
#     for i in range(1, n):
#         # print(i, nums[i], nums[i - 1])
#         if nums[i] == nums[i - 1]:
#             return True
#     return False

# list2 = [1, 2, 3, 1]
# result = duplicate2(list2)
# print(result)

# def duplicate3(nums):
#     seen = set()
#     for num in nums:        
#         if num in seen:
#             return True
#         seen.add(num)    
#         print(seen)    
#     return False

# list3 = [1, 2, 3, 4]
# result = duplicate3(list3)
# print(result)

# str1 = "Hello world man"
# print(type(str1), str1)
# tuple1 = str1.partition("wo")
# print(type(tuple1), tuple1)

# x = "    banana     "
# y = x.strip()

# print(x)
# print(y)
# print("of all fruits", y, "is my favorite")

# def find_left_sum(nums, i):
#     sum = 0
#     for j in range(0, i):
#         sum += nums[j]
#     return sum


# def find_right_sum(nums, i):
#     sum = 0
#     for j in range(i + 1, len(nums)):
#         sum += nums[j]
#     return sum

# def pivot_index(nums):
#     for i in range(0, len(nums)):
#         left_sum = find_left_sum(nums, i)
#         right_sum = find_right_sum(nums, i)

#         if left_sum == right_sum:
#             return i
#     return -1

# list1 = [1, 7, 3, 6, 5, 6]
# # list1 = [1, 2, 3]
# # list1 = [2, 1, -1]
# result = pivot_index(list1)
# # print(result)

# def pivot_index_2(nums):
#     s = sum(nums)
#     left_sum = 0    
    
#     for i, x in enumerate(nums):        
#         calc = s - left_sum - x
#         print("left_sum:", left_sum, ", sum:", s, ", calc:", calc)
#         if left_sum == calc:
#             return i
#         left_sum += x
#     return -1

# result = pivot_index_2(list1)
# print(result)

def intersection_1(nums1, nums2):
    ans = []
    for i in nums1:
        if (i in nums2):
            if (not i in ans):
                ans.append(i)
    return ans

# nums1 = [1, 2, 2, 1]; nums2 = [2, 2]
nums1 = [4, 9, 5]; nums2 = [9, 4, 9, 8, 4]
# result = intersection_1(nums1, nums2)
# print(result)

def intersection_2(nums1, nums2):
    result = list()
    unique_nums1 = list()

    for i in nums1:
        if not i in unique_nums1:
            unique_nums1.append(i)

    unique_nums2 = list()

    for j in nums2:
        if not j in unique_nums2:
            unique_nums2.append(j)

    for k in unique_nums1:
        if k in unique_nums2:
            result.append(k)

    return result

# result = intersection_2(nums1, nums2)
# print(result)

# def intersection_3(nums1, nums2):
#     result = []
#     i = 0
#     j = 0
#     nums1.sort()
#     nums2.sort()

#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] == nums2[j]:
#             if len(result) == 0:
#                 result.append(nums1[i])
#             else:
#                 if result[-1] != nums1[i]:
#                     result.append(nums1[i])
#             i += 1
#             j += 1
#         else:
#             if nums1[i] < nums2[j]:
#                 i += 1
#             else:
#                 j += 1
#     return result

# result = intersection_3(nums1, nums2)
# print(result)

# def divide(a, b):
#     quotient = a // b
#     reminder = a % b
#     return (quotient, type(quotient), reminder, type(reminder))

# result = divide(10, 3)
# print(result)
# from sys import getsizeof

# x = [1, 2, 1, 3, 2]
# print(len(x), type(x), x, id(x), getsizeof(x))
# y = set(x)
# print(len(y), type(y), y, id(y), getsizeof(y))
# z = list(y)
# print(len(z), type(z), z, id(y), getsizeof(y))

# def contains_duplicate(nums):
    # seen = set()
    # for num in nums:
    #     if num in seen:
    #         return True
    #     seen.add(num)
    # return False
    # x = len(nums)
    # y = len(set(nums))
    # if x != y:
    #     return True
    # else:
    #     return False

# list1 = [1, 2, 3, 4, 5]
# result = contains_duplicate(list1)
# print(result)

# def intersection(nums1, nums2):
#     s1 = set(nums1)
#     s2 = set(nums2)

#     return [x for x in s1 if x in s2]

# nums1 = [1, 2, 3, 4]
# nums2 = [5, 6, 7, 8]
# result = intersection(nums1, nums2)
# print(result)

# numbers = [1, 2, 3, 1, 2, 3, 4, 5, 1, 3, 1, 2, 3, 7, 1, 9, 10]
# counts = {}

# for n in numbers:
#     # print(n)
#     if n in counts:
#         counts[n] += 1
#     else:
#         counts[n] = 1

# print(counts)

# def two_sum(nums, target):
#     a = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if (nums[i] + nums[j] == target):
#                 a.append(i)
#                 a.append(j)
#                 break
#     return a

# # nums = [2, 7, 11, 15]; target = 9
# nums = [3, 2, 4]; target = 6

# result = two_sum(nums, target)
# print(result)
"""
def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num

        count += (1 if num == candidate else -1)
    
    return candidate

nums = [3, 2, 3]
result = majority_element(nums)
print(result)
"""

import math
import d

x = math.sqrt(9)
# print(x)

y = random.randfloat(1, 10)
print(y)
