# 1010 다리 놓기
from math import factorial
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(factorial(b) // ( factorial(a) * factorial(b-a)))
