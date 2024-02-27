"""
Program to insert a value to a specific location

def ins(nums, val, pos):
    print(nums)
    nums.insert(pos - 1, val)
    nums.pop()
    print(nums)


def ins(nums, val, pos):
    print(nums)
    nums.insert(pos - 1, val)


def ins(nums, val, pos):
    print(nums)
    print()
    prev = 0
    pos -= 1
    found = False
    i = 0
    while i < len(nums):
        pres = nums[i]
        print(f"pres: {pres}")
        if i == pos:
            print("**start:: i == pos **")
            found = True
            prev = nums[i] # future purpose [for next iteration]
            nums[i] = val
            print(f"found: {found}, prev: {prev}, num[i]: {nums[i]}")
            print("**end:: i == pos **")
        elif found == True:
            nums[i] = prev
            prev = pres
            print(f"nums[i]: {nums[i]}, prev: {prev}")
        i += 1
    print()        
    print(nums) 
    print(nums[:len(nums)-1])

def ins(nums, val, pos):
    print(nums)
    if pos == len(nums):
        nums[pos - 1] = val
        return nums
    for i in range(len(nums) - 2, -1, -1):
        # print(i)
        nums[i + 1] = nums[i]
        if i == pos - 1:
            nums[i] = val
            return nums        

nums = [2, 4, 5, 6, -1]
val = 3
pos = 2
print(ins(nums, val, pos))

"""
def ins(nums, val, pos):
    print(nums)
    for i in range(len(nums) - 2, pos - 2, -1):
        print(f"i = {i}, value: {nums[i]}")
        nums[i + 1] = nums[i]
    nums[pos - 1] = val
    print(nums)

nums = [2, 4, 5, 6, -1]
val = 8
pos = 4
ins(nums, val, pos)


# x = [2, 4, 5, 6, -1]
# print(x)
# print(x[::])