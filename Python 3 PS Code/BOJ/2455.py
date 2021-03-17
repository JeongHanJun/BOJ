# 2455 지능형 기차
'''
nums = []
for _ in range(4):
    nums.append(list(map(int, input().split())))
people = []
cnt = 0
for i in range(4):
    cnt -= nums[i][0]
    people.append(cnt)
    cnt += nums[i][1]
    people.append(cnt)
print(max(people))
'''
nums = []
c = 0
l = []
for _ in range(4):
    m, p = map(int, input().split())
    c += p-m
    l.append(c)
print(max(l))
