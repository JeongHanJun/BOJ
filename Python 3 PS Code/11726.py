# 11726 2xn 타일링
from sys import stdin
n = int(stdin.readline())
dp = [1] * (n+1)
dp[1] = 1
dp[2] = 2
if n < 3:
    print(dp[n])
else:
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])

