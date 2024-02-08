start = 1
end = 21

print(f"prime no.s b/w {start} to {end}")

for num in range(start, end + 1):
    # print(i)
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)