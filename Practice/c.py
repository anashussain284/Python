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