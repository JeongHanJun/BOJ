# 10818 최소, 최대 방법1 최대값과 최소값을 초기설정한후 비교하면서 최대/최소값을 추적
'''
import sys
n = int(sys.stdin.readline())
min = 1000000
max = -1000000
for i in sys.stdin.readline().rstrip().split():
    i = int(i)
    if i >= max:
        max = i
    if i <= min:
        min = i
print(min, max)
'''
# 10818 최소, 최대 방법2 컨테이너 타입의 데이터 이용
import sys
n, *num = map(int, sys.stdin.read().split())
print(min(num), max(num))