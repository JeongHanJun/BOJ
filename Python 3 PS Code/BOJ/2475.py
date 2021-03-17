# 2475 검증수
nums = list(map(int, input().split()))
temp = 0
for i in nums:
    temp += (i*i)
print(temp % 10)
