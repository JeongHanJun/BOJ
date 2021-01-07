# 1546 평균
from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
m = max(nums)
for i in range(n):
    nums[i] = nums[i] * 100 / m
print(sum(nums) / n)