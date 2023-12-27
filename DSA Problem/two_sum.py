"""
    Brute force method
"""
# def test(l, t):
#     for i in range(len(l)):
#         # print(l[i])
#         for j in range(i + 1, len(l)):
#             if l[i] + l[j] == t:
#                 return [i, j]
#     return -1

"""
    xxx method
"""
# def test(l, t):
#     for i in range(len(l) - 1):
#         # print(i, l[i])
#         search = t - l[i]
#         if search == l[i+1]:
#             return [i, l.index(search)]
#     return -1

"""
    xxx method
"""
def test(l, t):
    left = 0
    right = len(l) - 1
    temp_sum = 0

    while (left < right):
        temp_sum = l[left] + l[right]
        if temp_sum == t:
            return [left, right]
        elif temp_sum > t:
            right -= 1
        elif temp_sum < t:
            left += 1
    return -1


l = [2, 7, 11, 15];    t = 18
# l = [2,7,11,15];     t = 9

a = test(l, t)
print(a)