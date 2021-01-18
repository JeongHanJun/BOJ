# 2908 상수
from sys import stdin
a, b = map(str, stdin.readline().split())
if int(a[::-1]) > int(b[::-1]):
    print(a[::-1])
else:
    print(b[::-1])