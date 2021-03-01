# 1003 피보나치 함수
t = int(input())
nums = [ int(input()) for _ in range(t) ]
dp = [ [1, 0], [0, 1]]# 0, 1
for i in range(2, max(nums)+1):# 2부터 입력받은 최대수까지
    dp.append( [dp[i-2][0]+dp[i-1][0] , dp[i-2][1]+dp[i-1][1] ] )
for num in nums:
    print( dp[num][0], dp[num][1] )
    


