# 2960 에라토스테네스의 체
n, k = map(int, input().split())
nums = list(range(2, n+1))
print(nums)

cnt = 0
for i in range(2, n+1):
    for j in nums:
        if j % i == 0:
            cnt += 1
            if cnt == k:
                print(j)
                break
            nums.remove(j)
print(nums)
