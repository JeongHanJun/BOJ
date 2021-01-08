# 8958 OX퀴즈
from sys import stdin
n = int(stdin.readline())
for i in range(n):
    #line = list(stdin.readline().rstrip())
    line = list(stdin.readline().strip().split('X'))
    print(line)
    cnt = 0
    score = 0
    for e in line:
        cnt = e.count('O')
        score += cnt * (cnt+1) / 2
    print(int(score))