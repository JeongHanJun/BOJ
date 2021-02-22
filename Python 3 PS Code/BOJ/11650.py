# 11650 좌표 정렬하기
from sys import stdin
points = []
n = int(stdin.readline())
for _ in range(n):
    points.append(list(map(int, stdin.readline().split())))
points.sort()
for i in points:
    print(*i)
'''
for i in sorted(points):
    print(*i)
'''
