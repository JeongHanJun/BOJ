# 2217 로프
'''
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()
temp = []

for i in range(n):
    temp.append(nums[i] * (n-i))
print(max(temp))
'''
n = int(input())
k = [0] * (n+1)
for _ in range(n):
    k[int(input())] += 1
m, res = 0, 0
for i in range(n+1, 0, -1):
    if k[i] == 0:
        continue
    m += k[i]
    res = max(res, i*m)
print(res)