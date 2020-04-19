"""
a+b+c=1000을 만족하고
a^2 + b^2 = c^2를 만족하는
axbxc 는?
"""

result = 0

for a in range(1, 999):
    for j in range(1, 997):
        b = j
        c = 1000 - b - a
        result = a * b * c
        if(a * a == b * b + c * c):
            break
    if(a * a == b * b + c * c):
        break
print(a)
print(b)
print(c)
        
print(result)
