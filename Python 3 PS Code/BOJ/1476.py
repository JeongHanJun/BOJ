# 1476 날짜 계산
'''

1 2 3 5266 = 15 * 351 + 1  /  28 * 188 + 2  /  19 * 277 + 3 

15 28 19    7980  15 * 532  /   28 * 285   /  19 * 420  
'''
from math import lcm
e, s, m = map(int, input().split())
n = 1
while True:
    if (n-e) % 15 == 0 and (n-s) % 28 == 0 and (n-m) % 19 == 0:
        print(n)
        break
    n += 1
