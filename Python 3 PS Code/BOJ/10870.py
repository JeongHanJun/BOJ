# 10870 피보나치 수 5
# 1. 재귀 함수를 통해 구현한다면
'''
from sys import stdin
def fib(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(stdin.readline().strip())
print(fib(n))
'''
# 2. 재귀함수 필요없이 빠른 코드를 원한다면
n = int(input())
fib = []
fib.append(0)
fib.append(1)
fib.append(1)
for i in range(3,n+1):
    fib.append(fib[i-1]+fib[i-2])
print(fib[n])