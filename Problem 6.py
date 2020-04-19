num1 = 0
num2 = 0

for i in range(1, 101):
    num1 += i*i

for i in range(1, 101):
    num2 += i

print(num2*num2 - num1)