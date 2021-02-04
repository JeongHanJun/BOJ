# 4153 직각삼각형
# 1. 직관적 해석이 가능한 코드
'''
from sys import stdin
while True:
    lens = list(map(int, stdin.readline().strip().split()))
    if lens[0] == lens[1] == lens[2] == 0:
        break
    lens.sort()
    if lens[2]**2  == lens[1]**2 + lens[0]**2:
        print('right')
    else:
        print('wrong')
'''
# 2. 입력받으면서 비교
from sys import stdin
for line in stdin:
    a, b, c = map(int, line.split())
    if a**2 == b**2 + c**2 or b**2 == c**2 + a**2 or c**2 == a**2 + b**2:
        if a == b == c == 0:
            break
        print('right')
    else:
        print('wrong')