num = 600851475143
count = 2
while num != 1:
    if num % count == 0:
        num = num/count
    count += 1
print(count-1)