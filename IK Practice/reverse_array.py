nums = [3, 1, 0, -1, 7, 10, 2]
"""
def reverse(num):
    result = []
    for i in range(len(nums)-1, -1, -1):
        result.append(nums[i])

    print(result)

print(nums)
reverse(nums)


def reverse(nums):
    print(nums)
    nums.reverse()
    print(nums)

reverse(nums)

def reverse(nums):
    print(nums)
    nums2 = nums.copy()
    for i in range(0, len(nums2) // 2):
        nums2[i], nums2[-1-i] = nums2[-1-i], nums2[i]
    print(nums2)

reverse(nums)

def reverse(nums):
    print(nums)
    rev = nums[::-1]
    print(rev)

reverse(nums)

def reverse(nums):
    print(nums)
    rev = []
    for i in range(len(nums)):
        index = (len(nums) - i - 1)
        # print(i, index)
        rev.append(nums[index])
    print(rev)

reverse(nums)     

def reverse(nums):
    print(nums)
    l = 0
    r = len(nums) - 1
    while l < r:
        tmp = nums[r]
        nums[r] = nums[l]
        nums[l] = tmp
        l += 1
        r -= 1
    print(nums)

reverse(nums)
"""