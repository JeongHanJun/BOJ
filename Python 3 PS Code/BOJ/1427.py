# 1427 소트인사이드
'''
#1. 원래 코드
from sys import stdin
a = stdin.readline().strip()
b = sorted(map(int, a), reverse=True)
for i in b:
    print(i, end='')
'''
#2. 감명깊은 한줄 코드
print(''.join(sorted(input())[::-1]))