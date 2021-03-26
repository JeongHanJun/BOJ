# 1977 완전제곱수
m = int(input())
n = int(input())
nums = []
for i in range(m, n+1):
    if (i ** 0.5) % 1 == 0:
        nums.append(i)
if nums:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)