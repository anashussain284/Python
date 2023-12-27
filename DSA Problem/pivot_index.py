"""
    xxx method
"""
# def test(l):
#     all_sum = sum(l)
#     prefix = 0

#     for i, num in enumerate(l):
#         # print(i, num)
#         if (prefix == all_sum - prefix - num):
#             return i
#         prefix += num
#     return -1 

"""
    xxx method
"""
# def test(l):
#     for i in range(len(l)):
#         # print(i, l[i])
#         left = sum(l[j] for j in range(i))
#         right = sum(l[j] for in )
#         print(left)

"""
    xxx method
"""
# def test(l):
#     for k, v in enumerate(l):
#         left = sum(l[j] for j in range(k))
#         right = sum(l[j] for j in range(k + 1, len(l)))
#         if (left == right):
#             return k
#     return -1

"""
    xxx method
"""
# def test(l):
#     total = sum(l)
#     # print(total)
#     prefix = 0
#     for k, v in enumerate(l):
#         # print(k, v)
#         prefix += v
#         # print(prefix)
#         if prefix == (total + v) / 2:
#             return k
#     return -1

"""
    xxx method
"""
def test(l):
    for k, v in enumerate(l):
        # print(k, v)
        if sum(l[:k:]) == sum(l[k + 1:]):
            return k
    return -1

l = [1,7,3,6,5,6]
a = test(l)
print(a)
# print(l)
# print(l[:1:])