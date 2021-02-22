# 11651 좌표 정렬하기 2
'''
# 1. 처음 코드 이렇게 하면 y값이 같을때 먼저 입력된순서로 출력됨 반례) 1 -2   1 -1   3 3   2 3   0 4
from sys import stdin
n = int(stdin.readline())
points = []
for i in range(n):
    points.append(list(map(int, stdin.readline().split())))
points.sort(key= lambda x: x[1])
for i in points:
    print(*i)
'''
'''
# 2. x,y를 바꿔서 정렬하고 출력시 반대로
from sys import stdin
nums = []
for _ in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())
    nums.append([y,x])
for i,j in sorted(nums):
    print(j, i)
'''

#3. key에 y좌표우선, 그다음 x좌표까지 sorted, key, lambda, 2개의 key
from sys import stdin
nums = [stdin.readline() for _ in range(int(stdin.readline()))]
nums = sorted(nums, key = lambda x: (int(x.split()[1]), int(x.split()[0])))
print(''.join(nums))
# 3, 4번쨰줄을 아래와 같이 변경해도 되나, 위의 방법이 더 빠름
'''
for i in sorted(nums, key = lambda x: (int(x.split()[1]), int(x.split()[0]))):
    print(i, end='')
'''
