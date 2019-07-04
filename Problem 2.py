import time
start = time.time()

num1 = 1
num2 = 2
sum = 0
while num1 < 4000001 :
    if num1 % 2 == 0 :
       sum += num1
    num1 = num1 + num2

    temp = num1
    num1 = num2
    num2 = temp

print(sum)
print(time.time() - start)