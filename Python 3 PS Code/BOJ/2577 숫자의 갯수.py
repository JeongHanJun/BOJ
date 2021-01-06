# 2577 숫자의 갯수
# 정석적인 풀이
''' 
from sys import stdin
a = int(stdin.readline())
b = int(stdin.readline())
c = int(stdin.readline())
num = a * b * c
for i in range(10):
    num_cnt = list(str(num)).count(str(i))
    print(num_cnt)
'''

from sys import stdin
a = int(stdin.readline())
b = int(stdin.readline())
c = int(stdin.readline())
# 방법 1 int형으로 비교
'''
n = list( map( int, str(a*b*c) ) )
for i in range(10):
    print(n.count(i))
'''
# 방법2 str형으로 비교 2가지 방법 모두 메모리와 시간은 같게 나옴
n = list(str(a*b*c))
for i in range(10):
    print(n.count(str(i)))