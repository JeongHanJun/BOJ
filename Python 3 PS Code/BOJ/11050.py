# 11050 이항 계수 1
# math 모듈의 factorial 이용하는 방법
'''
from math import factorial
n, k = map(int, input().split())
print( factorial(n) // (factorial(k) * factorial(n-k)) )
'''
# math module 사용하지 않고 dp로 이항계수 값을 구하는 방법
def com(n, k):
    if k == 0 or k == n:
        return 1
    if dp[n][k] != 0:
        return dp[n][k]
    return com(n-1, k-1) + com(n-1, k)

n, k = map(int, input().split())
dp = [ [0 for i in range(k+1)] for j in range(n+1)]
print(com(n, k))