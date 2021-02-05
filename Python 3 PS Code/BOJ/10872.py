# 10872 팩토리얼
from sys import stdin
def fact(n):
    if n <= 1:
        return 1
    return fact(n-1) * n

n = int(stdin.readline().strip())
print(fact(n))