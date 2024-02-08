"""
Print armstrong numbers b/w 2 no's
"""
start = 1
end = 1000

for num in range(start, end + 1):
    # print(num)
    temp = num
    sum = 0
    order = len(str(num))

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)