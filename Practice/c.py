"""

# import random

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

# x = 9

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


import math
import d

x = math.sqrt(9)
# print(x)

y = random.randfloat(1, 10)
print(y)


class MyClass:
    x = 5

# print(MyClass)
m = MyClass
print(m.x)


class Person:
    def __init__(self, name, age, place):
        self.name = name
        self.age = age 
        self.place = place

    def __str__(self):
        return f"{self.name} from {self.place} is {self.age} years old"
    
    def intro(self):
        print("Hello my name is", self.name)

    def test(abc):
        print("Hello", abc.name)

P1 = Person("Anas", 26, "Cochi")
P2 = Person("Aisha", 22, "Cochin")
# print(P1.name, P1.age)
# print(P1)
P1.intro()
P1.test()
print()
del P1.name
del P1
P1.name = "ANAS222"

P1.intro()

# import d as test_module
# from d import P1
import d
import platform

print(d.P1['name'])



def intersection(nums1, nums2):
    result = []
    i = 0
    j = 0
    nums1.sort()
    nums2.sort()

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            if len(result) == 0:
                result.append(nums1[i])
            else:
                if result[-1] != nums1[i]:
                    result.append(nums1[i])
            i += 1
            j += 1
        else:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
    return result

# nums1 = [1, 2, 2, 1]; nums2 = [2, 2]
nums1 = [4, 9, 5]; nums2 = [9, 4, 9, 8, 4]
x = intersection(nums1, nums2)
# print(x)



# def my_own_join(l1):
#     str1 = ""
#     for i in range(0, len(l1)):
#         if (i != 0):
#             str1 = str1 + " " + l1[i]
#         else:
#             str1 = str1 + l1[i]
#     return str1

# x = my_own_join("the sky is blue".split())
# print(x)

# a = "Hello world"
# print(a)
# b = a.split(" ")
# print(b)

def reverse_word(string):
    l1 = string.split(" ")
    l1.reverse()
    s2 = " ".join(l1)
    return s2

x = reverse_word("the sky is blue")
print(x)

def first_(haystack, needle):
    # return haystack.find(needle)
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1

x = first_("anas anu", "u")
# print(x)

def a(h, n):
    for i in range(len(h) - len(n) + 1):
        # print(i)
        x = h[i:i+len(n)]
        if x == n:
            return i

x = a("anas anu", "u")
print(x)


greet = lambda : print("Hello world")

greet


class Person:
    def __init__(self, fname, lname):
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()

    def printname(self):
        print("Hello", self.fname, self.lname)

x = Person("anas", "hussain")
# x.printname()

class Student(Person):
    # pass
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print(f"welcome {self.fname} {self.lname} to the class of {self.graduation_year}")

y = Student("aisha", "hussain", 2018)
y.printname()
print(y.graduation_year)
y.welcome()


# x = (1, 2, 3, 4, 5)
x = "Hello world"
# print(x, type(x))
y = iter(x)
# print(y, type(y))

print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

# x = "hello"

# for y in x:
#     print(y)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)



class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x    
myclass =  MyNumber()
myiter = iter(myclass)   

print(next(myiter))
print(next(myiter))


class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass2 = MyNumber()
myiter2 = iter(myclass2)


# print(next(myiter2))
# print(next(myiter2))
# print(next(myiter2))

for i in range(16):
    print(next(myiter2))
print(next(myiter))

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 15:            
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
my_class = MyNumber()
myiter = iter(my_class)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
for i in range(20):
    print(next(myiter))

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Yamaha", "Speed boat")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail")

class Plane(Vehicle):
    def move(self):
        print("Fly")

car1 = Car("Ford", "Mustang")        
boat1 = Boat("Yamaha", "Speed boat")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

x = 1
print(x)

def abc():
    print(x)
    global y
    y = 2
    print(y)

abc()
print(y)



print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)
print()
print(x.strftime("%A"))
print()

y = datetime.datetime(2024, 1, 18, 10, 10, 10, 10)
# print(y)

import datetime

x = datetime.datetime.now()
print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%w"))
print(x.strftime("%b"))
print(x.strftime("%B"))

import math

x = min(-1, 1, 2, 3)
y = max(10, 9, 8)
z = abs(-1)
p = pow(2, 2)

print(x, y, z, p)
print(math.sqrt(9))
print(math.ceil(4.1))
print(math.floor(4.1))
print(math.pi)



import json

x = '{ "name":"John", "age":30, "city":"New York"}'

# print(type(x), x)
# y = json.loads(x)
# print(type(y), y)
# print()
# print(y["name"])

p = {'name': 'John', 'age': 30, 'city': 'New York'}
print(type(p), p)
q = json.dumps(p)
print(type(q), q)

x = {
    "name": "anas",
    "happy": True
}

print(type(x))
y = json.dumps(x)
print(type(y))



import json

print(json.dumps({"name": "anas", "happy": True}))
a = [1, 2, 3]
print(type(a), a)
b = json.dumps(a)
print(type(b), b)
print(json.dumps((1, 2, 3)))
print(json.dumps("Hello"))
print(json.dumps(1.1))
print(json.dumps(True))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, sort_keys=True))

import re

txt = "he rain in Spain"
x = re.search("^he.*Spain$", txt)
print(txt)
print(x)


# try:
#     # x = 1
#     print(x)
# except NameError:
#     print("Variable x in not defined")
# except:
#     print("Something else went wrong")
# else:
#     print("Everything is good")
# finally:
#     print("The try-except is finished")

try:
  f = open("demo.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")


x = -1

# if x < 0:
#     raise Exception("Thankyou")

print()
print()

x = "thankyou"

if not type(x) is int:
    raise TypeError("Only integers are allowed")


name = input("Enter ur name:")
print(f"Welcome to the world of happiness {name}.")


x = 1
y = "Hello world - {:.2f}"
z = y.format(x)
print(x)
print(y)
print(z)
print()
p = 1
q = 2
r = 3

txt = "I have a {carname}, it is a {model}"
print(txt)
print(txt.format(carname = "Ford", model="Mustang"))


def myfunction(n):
    return len(n)

x = map(myfunction, ('apple', 'cherry', 'ball'))
print(list(x))

def xyz(a, b):
    return a + b

x = map(xyz, ('apple', 'ball', 'cat'), ('1', '2', '3'))
print(list(x))


ages = [5, 12, 17, 18, 24, 32]

def myfunct(x):
    if x < 18:
        return False
    else:
        return True
    
adults = filter(myfunct, ages)
print(list(adults))

for x in adults:
    print(x)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def check_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
even_numbers = filter(check_even, nums)
print(list(even_numbers))

def check_odd(x):
    if x % 2 == 0:
        return False
    else:
        return True
    
odd_numbers = filter(check_odd, nums)
print(list(odd_numbers))


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

vowels = ['a', 'e', 'i', 'o', 'u']

def check_vowels(x):
    if x in vowels:
        return True
    else:
        return False
    
vowel_letter = filter(check_vowels, letters)
print(list(vowel_letter))

def check_consonatns(x):
    if not x in vowels:
        return True
    else:
        return False
    
consonent_letters = filter(check_consonatns, letters)
print()
print(list(consonent_letters))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odds = filter(lambda x : x % 2 != 0, nums)
# print(list(odds))
# evens = filter((lambda x : x % 2 == 0), nums)
# print(list(evens))
# multiple_of_3 = filter((lambda x : x % 3 == 0), nums)
# print(list(multiple_of_3))

square = list(filter((lambda x : x**2), nums))
print(square)

farenhite = list(map((lambda x : (9 / 5) * x + 32),nums))
print(farenhite)

words = ["hello", "world", "python", "map"]  
capitalize_words = list(map(lambda x : x.capitalize(), words))
print(capitalize_words)

add_5_inline = list(map((lambda x : x + 1), nums))
print(add_5_inline)

def add_5(x):
    return x + 1

add_5_outline = list(map(add_5, nums))
print(add_5_outline)

def modify_value(x):
    x = x + 10
    return x

num = 20
new_num = modify_value(num)
print(id(num), num)
print(id(new_num), new_num)

def modify_list(lst1):
    lst1.append(10)
    return lst1

list1 = [1, 2, 3]
new_list = modify_list(list1)

print(id(list1), list1)
print(id(new_list), new_list)

path = "/home/anashussain/Python/Practice/demo.txt"

f = open("demo.txt", "r")

# print(f.readline())

f2 = open("abc2.txt", "w")

for data in f:
    print(data)
    f2.write(data)

img1 = open("me_hamid.jpeg", "rb")
img2 = open("image_copy.jpeg", "wb")

for i in img1:
    img2.write(i)

f = open("demo.txt", "r")
print(f.read(11))

f = open("123.py", "x")


import os
os.remove("123.py")

f = open("123.py", "x")

if os.path.exists("123.py"):
    os.remove("123.py")
else:
    print("file doesnot exist")
os.rmdir("tst")
"""