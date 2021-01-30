# 2581 소수
from sys import stdin
from math import floor
'''
def IsPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, floor(n**0.5)+1):
            if n % i == 0:
                return False
        return True

m = int(stdin.readline().strip())
n = int(stdin.readline().strip())
nums = []
for i in range(m, n+1):
    if IsPrime(i):
        nums.append(i)
if len(nums) == 0:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))
'''
#리스트를 사용하지 않는다면, 단순한 변수로 한다면
def IsPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, floor(n**0.5)+1):
            if n % i == 0:
                return False
        return True
n = int(stdin.readline().strip())
m = int(stdin.readline().strip())
sum = 0
min = 0
for i in range(n, m+1):
    if IsPrime(i):
        sum += i
        if min == 0:
            min = i
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)