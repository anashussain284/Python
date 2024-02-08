# Display the powers of 2 using anonymous function

terms = 11

result = list(map(lambda x: 2 ** x, range(terms)))

# print(result)
print(f"The total terms are: {terms}")
print("*******************************")

for i in range(terms):
    # print(i, result[i])
    print(f"2 raised to power of {i} = {result[i]}")
