# 11051 이항 계수 2
from math import factorial
n, k = map(int, input().split())
print( (factorial(n) // (factorial(k) * factorial(n-k))) % 10007 )