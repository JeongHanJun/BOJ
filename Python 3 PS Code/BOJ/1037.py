# 1037 약수
cnt = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums[0] * nums[-1])