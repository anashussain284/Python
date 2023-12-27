"""
    xxx method
"""
# def test(l1, l2):
#     # print(l1)
#     # print(l2)
#     op = []
#     for i in l1:
#         if (i in l2 and i not in op):
#             op.append(i)
#     return op

"""
    xxx method
"""
# def test(l1, l2):
#     s1 = set(l1)
#     s2 = set(l2)
#     i_s = s1.intersection(s2)
#     return list(i_s)

"""
    xxx method
"""
# def test(l1, l2):
#     s_l1 = sorted(l1)
#     s_l2 = sorted(l2)

#     i = j = 0
#     i_s_l = []

#     while (i < len(s_l1) and j < len(s_l2)):
#         if (s_l1[i] < s_l2[j]):
#             i += 1
#         elif (s_l2[j] < s_l1[i]):
#             j += 1
#         else:
#             i_s_l.append(s_l1[i])
#             i += 1
#             j += 1
#     return i_s_l

"""
    xxx method
"""
def test(l1, l2):
    ans = []
    l1 = set(l1)
    for i in l2:
        if i in l1:
            ans.append(i)
            l1.remove(i)
    return ans


l1 = [1,2,2,1]; l2 = [2,2]
# l1 = [4,9,5]; l2 = [9,4,9,8,4]

a = test(l1, l2)
print(a)