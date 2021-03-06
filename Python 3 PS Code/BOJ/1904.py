# 1904 01타일
'''
00과 1로 조합
n   조합
1   1                                           1
2   00  11                                      2
3   001 100    111                              3
4   0000    0011    1100    1111    1001        5
dp[n] = dp[n-1] + dp[n-2]
'''
n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[n])