"""
a = 1
print(a, type(a))
b = str(a)
print(b, type(b))
c = float(a)
print(c, type(c))

a = 'a'
A = 'a'
print(a, type(a), id(a))
print(A, type(A), id(A))

a, b, c = "A", "B", "C"

print(a, type(a), id(a))
print(b, type(b), id(b))
print(c, type(c), id(c))

a = b = c = "A"
print(a, type(a), id(a))
print(b, type(b), id(b))
print(c, type(c), id(c))

no = [1, 2, 3]
a, b, c = no
print(a, type(a), id(a))
print(b, type(b), id(b))
print(c, type(c), id(c))
print()
a = str(a)
b = str(b)
print(a + ", " + b)

print("hello world")

a = 4
b = "apples"

print(a, b)

a = 3
b = int(a)
c = float(a)
d = str(c)
print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)

x, y, z = "Apple", "Orange", "Banana"
x = y = z = "Apple"
print(x, y, z)

fruits = ["Apple", "Banana", "Orange"]
x, y, z = fruits

print(x, y, z)

x = "awesome"

def myfun():
    global x
    x = "fantastic"
    print("Python is", x)

myfun()
print(x)


# x = "Hello world"
# x = {"Apple", "Banana", "Orange"}
# x = ["Apple", "Banana", "Orange"]
# x = ("Apple", "Banana", "Orange")
# x = {"Apple", "Banana", "Orange"}
# x = range(5)
# x = {"name": "Anas", "age": "26"}
# x = True
x = None
print(type(x), x)

x = "Hello world"
print(x[-1])
for i in x:
    print(i)
print(len(x))
print("h" not in x)

x = [0, 1, 2, 3, 4, 5]
print(x[:-2]) # 0, 1, 2, 3
print(x[-2:])
print(x[::-1]) # 5, 4, 3, 2, 1, 0
print(x[:3]) # 0, 1, 2
print(x[3::])

x = " Hello"
print(x)
print(x.strip())
y = x.replace("H", "h")
z = y.replace(" ", "~")
print(x)
print(y)
print(z)

a = "Hello, world"
b = a.split(",")
print(a, type(a))
print(b, type(b))

age = 10
txt = "My name is John and I'm {}"
# print(txt.format(age))
# print(f"My name is John and I'm {age} years old")

a = 10
b = 20
c = 30
string = "Hello {2}, how are you {1}, nice to meet you {0}"
string2 = string.format(a, b, c)
print(string)
print(string2)

a = "Hello Raju"
b = "Hello \"Raju\""
print(a)
print(b)

print(bool(False))
print(bool(None), type(None))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

def myfun():
    return False

if myfun():
    print("Yes")
else:
    print("No")

a = 10.0
print(isinstance(a, float))
print(isinstance((1,), tuple))

print(f"10/3 = {10/3}")
print(f"10%3 = {10%3}")
print(f"10//3 = {10//3}")
print()
print(f"10/4 = {10/4}")
print(f"10%4 = {10%4}")
print(f"10//4 = {10//4}")

print(1 > 2 or 2 > 1)
print(not(1 < 2 and 2 > 1))

x = [1, 2, 3, [1, 2]]
y = [1, 2, 3]
z = x

print(id(x), x)
print(id(y), y)
print(id(z), z)
print()
print(x is z)
print(z is x)
print(x == z)
print()
print(x is y)
print(x == y)

print([1, 2] in x)

a = list((1, 2, 3))
print(type(a), a)

x = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(x)
print()
print(x[-4:-1:-1]) # "kiwi", "melon", "mango"

a = [0, 1, 2, 3, 4, 5, 6]
print(f"before {a}")
a[1:4] = [1, 2, 3, 4, 5, 6]
print(f"after  {a}")
a.insert(2, "test")
print(a)

a = [1, 2, 3]
print(f"before {a}")
a.append((1, 2, 3))
print(f"after  {a}")

print("Before")
a = ["a", "b", "c"]
p = ["p", "q", "r"]
print(f"a = {a}")
print(f"p = {p}")
a.extend(p)
p.extend([1, 2, 3])
print("After")
print(f"a = {a}")
print(f"p = {p}")

print(a)
a.remove("a")
print(a)

print(a)
a.pop()
print(a)

a = ["a", "b", "c"]
print(a)
del a
print(a)


a = ["apple", "banana", "cherry"]

# for i in range(len(a)):
#     print(a[i])

[print(x) for x in a]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

a = []
for i in fruits:
    if "w" in i:
        a.append(i)
    
# print(a)
# b = [x for x in fruits if "a" in x]
b = [y for y in fruits if "a" in y]
c = [x for x in fruits if "w" in x]
# print(c)

even = [x for x in range(10) if x % 2 == 0]
# print(even)
odd = [x for x in range(10) if x % 2 != 0]
# print(odd)

nos = [1, -1, 2, -2, 3, -3, 4, -4, 0, 0]
zero = [x for x in nos if x == 0]
# print(zero)
positive = [x for x in nos if x > 0]
# print(positive)
negative = [x for x in nos if x < 0]
# print(negative)

non_apple = [x for x in fruits if x != "apple"]
# print(fruits)
# print(non_apple)

print([x for x in range(11)])
print([x for x in range(11) if x < 5])
print([x for x in range(11) if x > 5])
a = ["hi" for x in range(11)]
# print(a)
# b = [x for x in fruits if "w" in x]
# b = [x if x != "banana" else "orange" for x in fruits]
# print(fruits)
b = [x if x != "banana" else "orange" for x in fruits]
# c = [x for x in fruits if "w" in x]
c = [x if "w" in x else "h" for x in fruits]
print()
print(c)


# fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
# print(fruits)
# fruits.sort()
# print(fruits)

a = [100, 50, 65, 82, 23]
print(a)
a.sort(reverse=True)
print(a)
print()

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(fruits)
fruits.sort(reverse=True)
print(fruits)

# a = ["#8", "#15", "#42", "#23", "#4", "#16"]
a = [ "#53", "#7", "#3356", "#19", "#09", "#17185"]
print(a)
# a.sort()
b = sorted(a)
print(b)
c = sorted(a, key = len)
print(c)

def orders_sorting(string):
    return int(string[1:])

print()
print(a)
d = sorted(a, key=orders_sorting)
print(d)

list_of_pokemon = [
    {
        "name": "Sq",
        "pokedox": 7,
        "type": "water"
    },
    {
        "name": "Bu",
        "pokedox": 1,
        "type": "grass"
    },
    {
        "name": "Ch",
        "pokedox": 4,
        "type": "fire"
    },
]

# print(list_of_pokemon)
for i in list_of_pokemon:
    print(i)

def sort_1(pokemon):
    return pokemon['pokedox']

x = sorted(list_of_pokemon, key=sort_1)
# print(x)

print()

for i in x:
    print(i)



def my_fun(n):
    x = abs(n - 50)
    print(x)
    return x

a = [100, 50, 65, 82, 23]
print(a)

a.sort(key=my_fun)
print(a)

a = ["banana", "Orange", "Kiwi", "cherry"]
print(a)
# a.sort(key = str.upper)
a.reverse()
print(a)

a = ["apple", "banana", "cherry"]
print(id(a), a)
b = list(a)
b[0] = "test"
print(id(b), b)


list1 = ["a", "b", "c", "aa"]
list2 = [1, 2, 3]

list3 = list2 + list1

print(list3.index("a"))
print(list1)
print(list2)
print(list3)

# a = (1, 2, 3, 4, 1, 2, 3, 4)
a = (1, )
print(type(a), a)
print()
print(isinstance(a, tuple))
print()
b = tuple((1, 2, 3))
print(type(b))
a = tuple(range(6))
print(a)
print(a[0])
print(a[-1])
print()
print(a[4:])

a = tuple(range(11))
print(a)
b = list(a)
print(b)
b[5] = 5.1
c = tuple(b)
print(c)

a = list(range(11))
# print(a)
b = list(range(11))
# c = a

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
# print(id(c))

a = ("apple", "banana", "cherry")
print(a)
b = ("orange", "grapes")
print(b)
a += b
print(a)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(*green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

a = ("a", "b", "c")
b = (1, 2, 3)
c = b * 3
print(a)
print(b)
print(c)
print()
print(c.count(3))

a = set(range(5))
b = {0, 1, 2, 3, 4}
c = {0, 1, 2, 3, 4}
d = {0, 1, 2, 3, 4}
print(id(a), a)
print(id(b), b)
print(id(c), c)
print(id(d), d)

a = {"apple", "banana", "cherry", "apple"}
a.add("coconut")
print(a)
print("a2pple" in a)

a = {1, 2, 3}
b = {"a", "b", "c"}
print(a)
print(b)
print()
a.update(b)
print(a)
print(b)

a = {"a", "b", "c", "a"}
print(a)
a.remove("a")
print(a)

a = {"a", "b", "c", "a"}
print(a)
a.discard("ab")
print(a)

a = {"a", "b", "c"}
print(a)
a.clear()
print(a)

set1 = {1, 2, 3, 4}
set2 = {6, 7, 8, 9}
# set3 = set1.union(set2)

print(set1)
print(set2)
# print(set3)
set1.update(set2)
print()
print(set1)
print(set2)

set1 = {1, 2, 3}
set2 = {7, 8, 9, 1}
# set3 = set1.intersection(set2)
print(f"set1 = {set1}")
print(f"set2 = {set2}")
# print(f"set3 = {set3}")
# set1.intersection_update(set2)
set2.intersection_update(set1)
print()
print(f"set1 = {set1}")
print(f"set2 = {set2}")

set1 = {1, 2, 3}
set2 = {7, 8, 9}
# set3 = set1.symmetric_difference(set2)
print(f"set1 = {set1}")
print(f"set2 = {set2}")
# print(f"set3 = {set3}")
set1.symmetric_difference_update(set2)
print()
print(f"set1 = {set1}")
print(f"set2 = {set2}")

a = {1, 2, 3}
# a.add(5)
# a.clear()
b = a.copy()
print(a)
print(b)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(f"set1 = {set1}")
print(f"set2 = {set2}")
print(f"set3 = {set3}")

a = {
    "name": "HP",
    "class": 10,
    "place": "abc",
    "name":"lenovo",
    "name2":"lenovo"
}

# b = {
#     "name": "Lenovo",
#     "class": 10,
#     "place": "abc"
# }
print(a)
print(a["name"])
print(len(a))
print(type(a))
print(id(a))
b = dict(name="abc", age = 32, country = "India")
print(id(b), type(b), b)
print()
print(b.get("name"))

keys = b.keys()
print(type(keys), keys)

values = b.values()
print(type(values), values)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

keys = car.keys()
print(type(keys), keys)

values = car.values()
print(type(values), values)

items = car.items()
print(type(items), items)

print()

for x in car.items():
    print(x[0], " = ", x[1])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

print(car["year"])

car["year"] = 2004

print(car["year"])

# car.update({"year":2024})
car.update(dict(year=2024))

print(car["year"])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

print(car)
car.popitem()
del car["model"]
del car
car.clear()
print(car)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

for i in car:
    print(i)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

a = myfamily.copy()

myfamily.clear()

print(myfamily)
print(a)

for i in myfamily.values():
    for j in i.values():
        print(j)

print()
print(myfamily["child1"]["name"])

x = ("key1", "key2", "key3")
y = "test"
z = dict.fromkeys(x, y)

print(f"x = {x}, type = {type(x)}")
print(f"y = {y}, type = {type(y)}")
print(f"z = {z}, type = {type(z)}")
print()
# z.pop("key1")
z.popitem()
print(z.get("key1"))
print(f"z = {z}, type = {type(z)}")


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car)

car.update({"color":"black"})
print(car)
"""
