"""
2000000 이하의 소수 모두 더한 값
"""

import math

def get(num):
    for i in range(2, int(math.sqrt(num))):
        if(num % i == 0):
            return False
    return True

numArray = []

num = 2
while num <= 2000000:
    if get(num):
        numArray.append(num)
    num += 1
    
print(sum(numArray))