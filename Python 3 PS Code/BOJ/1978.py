# 1978 소수 찾기
from sys import stdin
from math import floor
# 소수판단 함수를 만들어서, 입력된숫자를 함수에서 소수판단
def IsPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, floor(n**0.5)+1):
            if n % i == 0:
                return False
        return True

n = int(stdin.readline().strip())
nums = list(map(int, stdin.readline().strip().split()))
cnt = 0
for num in nums:
    if IsPrime(num):
        cnt += 1
print(cnt)

        