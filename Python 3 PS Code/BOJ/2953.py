# 2953 나는 요리사다
nums = []
for _ in range(5):
    nums.append(sum(map(int, input().split())))
print(nums.index(max(nums))+1, max(nums))