# 11653 소인수 분해
from sys import stdin
from math import floor
# 1. 정석적인 풀이
'''
def IsPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, floor(n**0.5)+1):
            if n % i == 0:
                return False
        return True
n = int(stdin.readline().strip())
if n == 1:
    exit()
if IsPrime(n):
    print(n)
else:
    for i in range(2, n):
        while n % i == 0:
            n /= i
            print(i)
'''
# 2. 산뜻한 방법, 시공간 복잡도가 적음. 소수의 판별과 관계 없이 인수를 반복적으로 분해, 소수는 2를 제외하고 홀수인 점도 이용
n = int(input())
d = 2
while d*d <= n:
    if n % d == 0:
        print(d)
        n //= d
    else:
        d += 2 if d > 2 else 1# d = 2일때만 +1, 나머지 경우엔 +2
if n > 1:
    print(n)
