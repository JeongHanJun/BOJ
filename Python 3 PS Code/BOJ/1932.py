# 1932 정수 삼각형
from sys import stdin
n = int(stdin.readline())
dp = []
for i in range(n):
    dp.append(list(map(int, stdin.readline().rstrip().split())))

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif j == len(dp[i])-1:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[n-1]))

""" 
from sys import stdin
n = int(stdin.readline())
nums = []
dp = []
for i in range(n):
    dp.append(list(range(i+1)))
    nums.append(list(map(int, stdin.readline().rstrip().split())))
print(dp)
print(nums)
dp[0] = nums[0]
temp = dp[0]
for i in range(1,n):
    for j in range(1, i+2):
        dp[i][j] += max(nums[i-1][j-1] + nums[i-1][j])
    print(dp)
"""
"""
# 새로운 리스트에 dp를 진행
from sys import stdin
n = int(stdin.readline())
nums = []
for _ in range(n):
    nums.append(list(map(int, stdin.readline().rstrip().split())))
dp = [ list(range(i+1)) for i in range(n) ]
dp[0] = nums[0]
for i in range(1,n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + nums[i][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] = dp[i-1][j-1] + nums[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + nums[i][j]
print(max(dp[n-1]))
"""
