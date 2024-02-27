"""
Python Program to Shuffle Deck of Cards
@ref https://www.programiz.com/python-programming/examples/shuffle-card
"""

import itertools, random

deck = list(itertools.product(range(1, 14), ["Spade", "Heart", "Diamond", "Club"]))

# print(deck)
for i in range(len(deck)): 
    # print(deck[i])
    pass

d = list(itertools.product(range(1, 10), ["a", "b", "c", "d"]))
# print(d)
random.shuffle(d)
for i in range(5):
    pass
    # print(d[i])

a = list(itertools.product(range(1, 4), [1, 2, 3]))
random.shuffle(a)
for i in range(len(a)):
    # print(i)
    # print(a[i])
    pass


# b = list(itertools.product(["a", "b", "c"], [1, 2, 3]))    
# random.shuffle(b)
# for i in range(len(b)):
#     # print(i)
#     print(b[i])

c = [1, 2, 3, 4, 5]
random.shuffle(c)
for i in range(len(c)):
    print(c[i])