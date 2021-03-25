# 1676 팩토리얼 0의 개수
from math import factorial
n = int(input())
nums = list(str(factorial(n)))
cnt = 0
for i in reversed(nums):
    if int(i) != 0:
        break
    else:
        cnt += 1
print(cnt)