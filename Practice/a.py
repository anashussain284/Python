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

a = ["a", "b", "c"]
# a[1:2] = ["x"]
print(a)
a.insert(2, "x")
print(a)

