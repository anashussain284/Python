# print(type(float(1)))

# print(type(float(1)))

# a = 1;
# A = "1";

# print(a, type(a), id(a))
# print(A, type(A), id(A))


# a = "Hello world";
# print(a[-11])

# for x in "Banana":
#     print(x)

# a = "Anas";
# print(a, type(a), len(a))


# txt = "The best things in life are free"
# key = "free"
# # print(txt)
# # print(key)
# # found = key in txt
# # print(found)

# if key not in txt:
#     # print("Yes", key, "is present in", txt)
#     print("No", key, "is not present in", txt)
# else:
#     # print("No", key, "is not present in", txt)
#     print("Yes", key, "is present in", txt)



# print()
# print()
# print()
# print()
# print()

# if "super" in "Anas is super":
#     print(True)
# else:
#     print(False)


# a = "Hello world"
# print(a)
# print(a[-5:-1])

# a = "He, ll, o W,hor,ld"
# b = a.split(",");
# print(a.upper())
# print(a.lower())
# print(a.strip())
# print(a.replace("h", "J"))
# print(a.replace("el", "**"))
# print(b, type(b), b[0])

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(a, type(a), len(a))
# print(b, type(b), len(b))
# print(c, type(c), len(c))

# age = 25
# name = "Anas {}"
# txt = name.format(age)
# print(age)
# print(name)
# print(txt)


# txt = "a-{2}, b-{1}, c-{0}"
# a = 1
# b = 2
# c = 3
# data = txt.format(a, b, c)
# print(data)

# a = "We are the so-called \"Vikings\" from the north."
# b = "We are the so-called \'Vikings\' from the north."
# c = "We are the so-called \\Vikings\\ from the north."
# d = "We are the so-called \/Vikings\/ from the north."
# e = "We are the so-called \nVikings\n from the north."
# f = "Hello\rWorld!"
# g = "We \tare the so-called \tVikings from the north."
# h = "We are the so-called Vik\b\bings from the north."
# i = "\110\145\154\154\157"
# j = "\x48\x65\x6c\x6c\x6f"
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print()
# print(f)
# print(g)
# print(h)
# print(i)
# print(j)

# print(1 > 2)
# print(1 < 2)
# print(1 == 2)

# a = 10
# b = 2

# if a > b:
#     print(a, "is greater than", b)
# else:
#     print(b, "is greater than", a)

# print(bool(""))
# print(bool(10))
# print(bool(["a", "b"]))
# print(bool([]))

# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(()))
# print(bool([]))
# print(bool({}))

# class myclass():
#     def __len__(self):
#         return 0
    
#     def __test__(test):
#         return 0
    
# myobj = myclass()
# print(bool(myobj))

# def myfun():
#     return False

# if myfun():
#     print("Yes")
# else:
#     print("No")

# x = 200
# print(isinstance(x, int))
# print(isinstance(x, float))
# print(isinstance(x, object))

# a = 3
# b = 2
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(b / a)
# print(b % a)
# print(b ** a)
# print(a // b)
# print(b // a)

# a = 5
# print(a)
# a += 1
# print(a)
# a -= 1
# print(a)
# a *= 5
# print(a)
# a /= 5
# print(a)
# a %= 1
# a /= 1
# a **= 3
# a >>= 3
# print(a)

# a = 1
# b = 2
# print(a == b)
# print(a != b)
# print(a > b)
# print(b > a)
# print( a >= b)
# print(b >= a)

# print(not(1 > 0 or 2 > 1))

# a = ["apple", "banana"]
# b = ["banana", "apple"]
# c = b
# print(a, type(a), id(a))
# print(b, type(b), id(b))
# print(c, type(c), id(c))
# print()
# print(a is c)
# print(b is c)
# print(a is a)
# print()
# print(a == b)

# a = ["apple", "orange", "banana"]
# b = {"apple", "orange", "banana"}
# c = ("apple", "orange", "banana")
# # print(a)
# print("orange" not in a)
# print("orange" in b)
# print("orange" in c)

# print(6 & 3)

# print((6 + 3) - (6 + 3))
# print((95 + 5) * 3)
# print(5 + 4 - 7 + 3)

# a = [1, 2, 3, 4, 5, 1, 2, 3]
# print(a)
# print(len(a))
# print()
# b = ["a", "b", "c"]
# print(b)
# print()
# c = [True, False, True, False]
# print(c)
# d = ["a", True, 1]
# print(d)
# print(type(d))

# print()
# e = list((1, 2, 3))
# print(e, type(e), len(e), id(e))

# a = ["a", "b", "c"]
# print(a)
# print(a[-5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist)
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist)
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist)
# print(thislist[-4:-1])

# a = ["a", "b", "c", "d", "e", "f"]
# print(a)
# # if "ab" in a:
# #     print("Yes")
# # else:
# #     print("No")
# # a[2] = "x"
# # print(a)
# a[2:3] = ["x", "y", 6]
# print(a)

# print()
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# a = ["a", "b", "c"]
# # a[1:2] = ["x"]
# print(a)
# a.insert(2, "x")
# print(a)

# a = ["a", "b", "c"]
# print(a)
# a.append("d")
# print(a)
# a.insert(15, "e")
# print(a)

# letters = ["a", "b", "c"]
# numbers = [1, 2, 3]
# numbers = (1, 2, 3)
# numbers = {1, 2, 3}
# print(letters)
# print(numbers)
# letters.extend(numbers)
# # numbers.extend(letters)
# print()
# print(letters)
# print(numbers)

# # a = ["a", "b", "c"]
# a = {"a", "b", "c"}
# print(a)
# # a.remove("a")
# # a.pop(0)
# # del a
# a.clear()
# print(a)

# a = ["a", "b", "c"]
# for x in a:
#     print(x)

# a = range(6)
# print(a)
# print(len(a))
# print()
# for x in a:
#     print(x)

# a = ["apple", "ball", "cat"]
# print(a, len(a))
# print()
# # for x in a:
# #     print(x)
# for i in range(len(a)):
#     print(a[i])

# i = 0
# while i <= 5:
#     print(i)
#     i += 1

# while i < len(a):
#     print(i, ":", a[i])
#     i += 1

# [print(x) for x in a]
# a = ["apple", "banana", "cherry", "kiwi", "mango"]
# b = []
# print(a, b)

# for x in a:
#     # print(x)
#     if "a" in x:
#         b.append(x)

# b = [x for x in a if "r" in x]
# b = [x for x in a if "r" in x]
# b = [x for x in a if "i" in x]
# print(a, b)

# newlist = [x for x in fruits]
# b = [x for x in a]
# print(a, b)

# a = [x for x in range(10) if x < 5]
# print(a)
# a = ["apple", "banana", "cherry", "kiwi", "mango"]
# b = [x.upper() for x in a]
# print(a)
# print(b)

# b = ["*****" for x in a]
# print(a)
# print(b)

# b = [x for x in a]
# b = [x.upper() for x in a]
# b = ["*" for x in a]
# b = [x if x != "banana" else 'orange' for x in a]
# print(a)
# print(b)

# a = ["orange", "mango", "kiwi", "pineapple", "banana"]
# a = ["banana", "Orange", "Kiwi", "cherry"]
# a = [100, 50, 65, 82, 23]
# print(a)
# a.sort()
# a.reverse()
# a.sort(key = str.lower)
# a.sort(reverse=True)
# print(a)

# def myfn(n):
#     return abs(n - 50)

# a = [100, 50, 65, 82, 23]
# print(a)
# a.sort(key = myfn)
# print(a)

# a = ["z", "a", "z", "b", "z", "c"]
# a = ["a", "b", "c"]
# print("b4 :", a)
# b = a.copy()
# b = list(a)
# a.append("d")
# print(a)
# print(b)
# b = ["p", "q", "r"]
# print("b :", b, "count:")
# c = a + b
# print(c)

# for x in b:
#     # print(x)
#     a.append(x)
# print(a)

# a.extend(b)
# print("a :", a)

# print(a.count(1))
# print(a.index("z"))
# a.insert(100, [1, 2, 3, 4])

# a.pop(1)
# a.pop(-1)
# a.remove("a")
# print("a4 :", a)

# a = (1, 2, 3, 4)
# b = (9)
# print(a, type(a), len(a), a[0])
# # print(b, type(b), len(b), b[0])
# print(b, type(b))

# a = (1, '2', 3)
# a = tuple((1, 2, 3))
# b = ("a", "b", "c")
# c = (True, False, True, False)
# d = (1, "a", True)

# print(a, type(a))
# b = a[-1]
# print(b, type(b))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(a)
# print(a[::-1])

# if '1' in a:
#     print("Yes")
# else:
#     print("No")

# a = (1, 2, 3)
# print("b4", a)

# # a[0] = 10
# # b = list(a)
# # b.remove(3)
# # a = tuple(b)
# # a += (10, 99)
# del a

# print("a4", a)

# fruits = ("apple", "banana", "cherry")
# fruits = ["apple", "banana", "cherry"]
# fruits = {"apple", "banana", "cherry"}
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry", "orange")
# print(fruits)
# print()

# (green, *yellow, red, rose) = fruits

# print(green)
# print(yellow)
# print(red)
# print(rose)

# for x in fruits:
#     print(x)

# for i in range(len(fruits)):
#     print(fruits[i])

# i = 0

# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# a = (1, 2, 3, 1, 1)
# b = ("a", "b", "c")
# c = a + b

# print(a)
# print(b)
# print(c)
# d = a * 3
# print(d)

# print(a.index(3))
# print(a.count(10))

# a = {"a", "b", "c"}
# b = {1, 2, 3}
# a = ("a", "b", "c", 1, 2, 3, 3, 3, 3, 3, 3)
# b = {True, False, 0}
# print(len(a), len(b))

# a = {1, 2, 3}
# b = {"a", "b", "c"}
# c = {True, False}
# d = {1, "2", False}

# print("a:", a, type(a))
# print("b:", b, type(b))
# print("c:", c, type(c))
# print("d:", d, type(d))

# a = list(("a", "b", "c"))
# b = tuple(("a", "b", "c"))
# c = set(("a", "b", "c"))

# print("a:", a, type(a))
# print("b:", b, type(b))
# print("c:", c, type(c))

# for x in a:
#     print(x)

# print("ab" in a)
# print(a)

# for x in a:
#     print(x)
# b = 1
# a.add(b)
# print(a)
# print(a, "id:", id(a))
# a.update(b)
# print(b)
# print(a, "id:", id(a))


# a = {"a", "b", "c", True}
# b = {"p", "q", "r", "a", "b", "c", 1}
# b = {1}
# b = [1]
# b = (1,)
# print("before")
# print("a:",a, "id:", id(a))
# print("b:",b, "id:", id(b))
# a.add("1")
# a.update(b)
# b.update(a)
# a.intersection_update(b)
# a.union(b)
# b.union(a)
# a.remove('a')
# a.discard(1)
# a.clear()
# del a
# print()
# print("after")
# print("a:",a, "id:", id(a))
# print("b:",b, "id:", id(b))

# print()
# print("Union")
# print(a.union(b))

# print()
# print("Intersection")
# print(a.intersection(b))
# print()
# print("Symmetric difference")
# print(a.symmetric_difference(b))

# a = {1, 2, 3}
# print(a)
# a.add("a")
# print(a)
# a.clear()

# a = {
#     "Name": "Anas",
#     "Place": "cochi",
#     "Year": 2024
# }

# a = dict(name = "Anas", place = "Cochi", name = "Anas")

# print(a, type(a), id(a), len(a))
# b = a.get("Name")
# print(b, type(b), id(b), len(b))
# k = a.keys()
# print(k)
# v = a.values()
# print(v)

# for x in a.values():
#     print(x)

# a["Laptop"] = "HP"
# print(a, type(a), id(a), len(a))
# a.update({"Laptop": "HP2"})
# a.update({"Name": 2024})
# a.update({"a": "b"})
# a.pop("Name")
# a.popitem()
# del a["Name"]
# del a
# a.clear()
# print(a, type(a), id(a), len(a))

# c = a.items()
# print(c, type(c), id(c), len(c))

# for x in a.items():
#     print(x[0], ":", x[1])

# if "name" in a:
#     print("Yes")
# else:
#     print("No")

# a = {
#     "Name": "Anas",
#     "Place": "Cochi",
#     "Year": 2024
# }
# print(a, id(a))
# b = a
# b = a.copy()
# b = dict(a)
# a["Name"] = 1
# print(b, id(b))

# for x in a:
#     # print(x)
#     print(a[x])

# for x in a.values():
    # print(x)
# for x in a.keys():
#     print(x)

# for key, value in a.items():
#     print(key, ":", value)

# a = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# print(a, len(a["child1"]))

# a = {
#     "A": "A"
# }
# b = {
#     "B": "B"
# }
# c = {
#     "C": "Anas"
# }
# z = {
#     "a": a,
#     "b": b,
#     "c": c,
# }

# print(z, len(z))
# print(z["c"]["C"])

# if "Anas" in z["c"]["C"]:
#     print(True)
# else:
#     print(False)

# a = {
#     "Name": "Anas",
#     "Place": "Cochi",
#     "Year": 2024
# }

# print(a, id(a))
# a.clear()
# b = a.copy()
# print(a, id(a))
# print(b, id(b))

# a = ("a", "b", "c")
# c = a
# print(a, type(a), id(a))
# b = dict.fromkeys(a, c)
# # b = dict.fromkeys(a, c)
# print(b, type(b), id(b))

# print(a.get("Year"))

# a = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(a, type(a))

# b = a.setdefault("model2")

# print(b, type(b))
# print(a)

a = 5
# if a > 0:
#   print("+ve")
# elif a < 0:
#   print("-ve")
# else:
#   print("0")

# print("T") if 1 > 2 else print("F")


# print("+ve") if a > 0 else print("-ve")

# print("+ve") if a > 0 else print("-ve") if a < 0 else print("0")

# print("1") if a == 1 else print("2") if a == 2 else print("3") if a == 3 else print(4) if a == 4 else print("! in the list")

# if 1 > 0 and 2 > 0:
#     print("Both R T")

# if 1 > 0 or 2 > 0:
#     print("both / one is T")

# if not 1 > 2:
#     print("T")
# else:
#     print("F")

a = 10

# if (a > 5):
#   print("above 5")
#   if (a > 10):
#     print("above 10")
#   else:
#     print("blow 10")
# else:
#   print("below 5")

if 10 > 2:
    # print("T")
    pass
