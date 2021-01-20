# 1712 손익분기점
'''
a = 매년 고정비용
b = 물건 1개당 생산비용
c = 물건의 판매가

c * (판매갯수) > a + b * (판매갯수)
판매갯수 = t라고 하면   c*t > a + b*t  ->  t(c-b)  > a  ->  t > a / (c-b)
판매갯수를 구하는 문제
'''

from sys import stdin
a, b, c = map(int, stdin.readline().strip().split())
# 분모가 0이 되는 ZeroDivisionError를 생각해야 하는 부분
if c-b > 0:
    print( (a // (c-b) ) + 1)
else:
    print(-1)

'''
a, b, c = map(int, input().split())
if c-b > 0:
    print((a//(c-b)) + 1)
else:
    print(-1)
'''