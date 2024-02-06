"""
import random

def greet(name):
    print("Hello", name.capitalize())

x = random.randint(1, 10)
y = 10

P1 = {
    "name": "anas",
    "place": "ekm",
}

1. Bianry search

import math

list = [1, 2, 3, 4, 5, 6, 7, 8]
target = 1
start = 0
end = len(list) - 1

def binary_search(list, start, end, target):
    # print(list[start:end+1])
    mid = math.floor((start + end) / 2)    
    if start > end:
        return False
    elif target == list[mid]:
        return True
    elif target < list[mid]:
        return binary_search(list, start, mid - 1, target)
    else:
        return binary_search(list, mid + 1, end, target)
print(binary_search(list, start, end, target))

2. Merge sort

def merge_sort(list_1): # O(log n)
    if (len(list_1)) < 2:
        return list_1
    
    mid = len(list_1) // 2
    left_array = list_1[:mid]
    right_array = list_1[mid:]
    
    print(f"left_array -{left_array}")
    print(f"right_array-{right_array}")

    return merge(merge_sort(left_array), merge_sort(right_array))

def merge(left_array, right_array): # O(n)
    print("*")
    result_array = []
    left_index = 0
    right_index = 0

    while (left_index < len(left_array) and right_index < len(right_array)):
        if (left_array[left_index] < right_array[right_index]):
            result_array.append(left_array[left_index])
            left_index += 1
        else:
            result_array.append(right_array[right_index])
            right_index += 1
        print(f"result_array-{result_array}")

    result_array.extend(right_array[right_index:])
    result_array.extend(left_array[left_index:])  
    # print(result_array)  
    return result_array

list_1 = [12, 3, 16, 6, 5, 1]
print(f"original-{list_1}")
print(f"sorted  -{merge_sort(list_1)}") # total = O(n * log n) = O(n log n)

3. Fibonacci


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(10))

4. Factorial
"""

def f(n):
    if n == 0:
        print("***")
    
    for i in range(n):
        f(n - 1)

f(3)        