# 3009 네 번째 점
'''
3 점이 주어질떄 이들과 함꼐 축과 평행한 직사각형을 이루는 점의 위치를 출력하라
'''
# 모든 경우의수
'''
from sys import stdin
points = []
for _ in range(3):
    x, y = map(int, stdin.readline().strip().split())
    points.append(x)
    points.append(y)
if points[0] == points[2]:
    #x = points[4]
    if points[1] == points[3]:
        print(points[4], points[5])
    elif points[1] == points[5]:
        print(points[4], points[3])
    else:
        print(points[4], points[1])
elif points[0] == points[4]:
    #x = points[2]
    if points[1] == points[3]:
        print(points[2], points[5])
    elif points[1] == points[5]:
        print(points[2], points[3])
    else:
        print(points[2], points[1])
else:#points[2] == points[4]
    #x = points[0]
    if points[1] == points[3]:
        print(points[0], points[5])
    elif points[1] == points[5]:
        print(points[0], points[3])
    else:
        print(points[0], points[1])
'''

# 2. 입력받으면서 검사
from sys import stdin
xs= []
ys = []
for _ in range(3):
    x, y = map(int, stdin.readline().strip().split())
    if x in xs:
        xs.remove(x)
    else:
        xs.append(x)
    if y in ys:
        ys.remove(y)
    else:
        ys.append(y)
print(*xs, *ys)