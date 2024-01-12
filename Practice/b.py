# a = 1
# print(a, type(a), id(a))

# a = 1;
# print(type(a))
# print(type(int(a)))
# print(type(str(a)))
# print(type(float(a)))


# a = 1
# A = 2
# print(id(a))
# print(id(A))

# a, b, c = "A", "B", "C"

# print(a, b, c)


# a = b = c = "X"
# print(a, b, c)

# l = ["A", "B", "C"] 
# print(l)

# # a, b, c = l

# a, b, c = ["P", "Q", "R"]

# print(a, b, c)

# l = a, b, c
# print(l, type(l))

# x = "A"

# def myfunc():
#     global x
#     x = "B"
#     print("inside is", x)

# myfunc()

# print("outside is", x)

# a = 1j
# print(a, type(a))

# z1 = complex(2, 3)
# print(z1, type(z1))

# z2 = 3 + 4j
# print(z2, type(z2))

# print("real part", z1.real)
# print("imaginary", z1.imag)

# print()

# a = complex(1, 2)
# print(a)

# b = 1+2j
# print(b.real)
# print(b.imag)

# z3 = z1 + z2
# print(z3)
# print("real", z3.real)
# print("image", z3.imag)

# a = [1, 2, 3]
# print(a, type(a))

# b = (1, 2, 3)
# print(b, type(b))

# c = {1, 2, 3}
# print(c, type(c))

# d = range(6)
# print(d, type(d))

# e = {"a":1, "b":2, "c":3}
# print(e, type(e))

# f = frozenset({1, 2, 3})
# print(f, type(f))

# print()

# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)

# my_frozen_set = frozenset({2, 3, 4})
# my_frozen_set.add(5)
# print(my_frozen_set)

# g = True
# print(g, type(g))

# h = b"1Hello"
# # h = b"1"
# print(h, type(h), id(h))
# # print(h[0], h[1])
# index = h.find(b'H')
# print("index", index)

# my_string = "hello"
# my_bytes = bytes(my_string, 'utf-8')
# print("my_string", my_string, type(my_string))
# print("my_bytes", my_bytes, type(my_bytes))

# h = bytearray([1, 8, 7])
# h[2] = 3
# print(h, type(h))
# i = h.find(3)
# print(i)

# print()

# j = "abc"
# print(j, type(j))
# k = bytes(j, "utf-8")
# print(k, type(k))
# l = bytearray(j, "utf-8")
# print(l, type(l))

# print()

# data = bytes([1, 2, 3, 4, 5])
# print(data, type(data), id(data))

# my_view = memoryview(data)
# print(my_view, type(my_view), id(my_view))

# print()
# print(my_view[1])

# subset = my_view[::]
# print(subset, type(subset))

# a = '1'
# a = str(a)
# print(a, type(a), id(a))

# a = 1+2j
# a = 5j+10
# a = -5j
# print(a, type(a), id(a))

# print(a.real)
# print(a.imag)

# print()

# print(complex(11))

# import random

# print(random.randrange(100, 500))



# a = """ljkldf
# lkjsdadnasljfsl
# ;lkkasdfjl"""

# # print(a[0])
# # for x in a:
# #     print(x)

# # print(len(a))
# print("anas" not in a)

# print()

# if "anas" in a:
#     print("found")
# else:
#     print("! found")


# a = "0123456789"
# print(a)
# print(a[5:])
# print(a[-8:-2])
# print(a[-5:-2])
# print(a[2:6])
# print(a[-6:-2])

# a = "h,el,lo"
# print(a)
# print(a.upper())
# print(a.lower())
# print(a.strip())
# a = a.upper()
# print(a.replace("H", "j"))
# b = a.split("'")
# print(b)


# print("hello_" + "world_" + {1})

# name = "anas"
# age = 26

# print(name)

# str = name.

# str = "My name is ANAS, My earning is {}"
# o_str = str.format(1000)
# print(str)
# print(o_str)


# str = "I have {} pens"
# print(str)
# print(str.format(99))

# str = "apple={}, ball={}, cat={}"
# modified_str = str.format(10, 20, 30)
# print(str)
# print(modified_str)

# a = "Hello \"Anas\"";
# print(a)

# txt = "banana"
# x = txt.center(50, '-')
# print ("|", x, "|")


# a = "anas hussain"
# b = a.count('a')
# print(a)
# print(b)

# a = "My name is Ståle"
# b = a.encode()
# print(a)
# print(b)


# txt = "My name is Ståle"

# print(txt)
# print(txt.encode(encoding="ascii", errors="backslashreplace"))
# print(txt.encode(encoding="ascii", errors="ignore"))
# print(txt.encode(encoding="ascii", errors="namereplace"))
# # print(txt.encode(encoding="ascii", errors="strict"))
# print(txt.encode(encoding="ascii", errors="replace"))
# print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))

txt = "0123456789, welcome to my world."
x = txt.endswith("4", 2, 5)
print(txt)
print(x)