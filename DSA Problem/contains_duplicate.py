"""
    xxx method
"""
# def test(a):
#     for i in range(len(a)):
#         # print(i)
#         for j in range(i + 1, len(a)):
#             # print(i, j)
#             if a[i] == a[j]:
#                 return True;
#     return False;

"""
    xxx method
"""
# def test(a):
#     # print(a)
#     a.sort()
#     print(a)
#     for i in range(len(a) - 1):
#         # print(i)
#         if a[i] == a[i + 1]:
#             return True
#     return False

"""
    xxx method
"""
# def test(a):
#     has_set = set()
#     for i in a:
#         # print(i)
#         if i in has_set:
#             return True
#         else:
#             has_set.add(i)
#     return False

"""
    xxx method
"""
def test(a):
    d = {}
    for i in a:
        if i in d:
            return True
        else:
            d[i] = 1

    # return d
    return False

# a = [4, 2, 5, 3, 1, 2]
a = [1, 2, 3]
b = test(a)
print(b)

# print(range(5))
