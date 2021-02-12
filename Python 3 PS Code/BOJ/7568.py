# 7568 덩치
# 1. 오리지널 풀이
'''
from sys import stdin
height = []
weight = []
n = int(stdin.readline().strip())
for _ in range(n):
    a, b = map(int, stdin.readline().strip().split())
    height.append(a)
    weight.append(b)
rank = [1] * n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if height[i] > height[j] and weight[i] > weight[j]:
            rank[j] += 1
for i in rank:
    print(i)
'''
# 2. 위의 풀이를 좀더 간소화
from sys import stdin
n = int(stdin.readline().strip())
dc = []
for _ in range(n):
    dc.append(list(map(int, stdin.readline().strip().split())))
for i in dc:
    rank = 1
    for j in dc:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')