
"""최고 큰건 99801 """
result = []
for i in range(900, 1000):
    for j in range(900, 1000):
        num = i*j
        if str(num) == str(num)[::-1]:
            result.append(num)
print(max(result))