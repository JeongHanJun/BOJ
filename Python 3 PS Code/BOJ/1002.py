# 1002 터렛
'''
조씨와 백씨는 터렛에 근무 각각 좌표(x1,y1), (x2, y2) - 마린까지의 거리 r1, r2
마린이 존재할 수 있는 좌표의 갯수를 출력
두 원과 한점
1. 1점 - 접한다 - 내접, 외접
2. 2점 - 겹친다
3. 0점 - 안만난다.
'''
from sys import stdin
for _ in range(int(stdin.readline().strip())):
    x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().strip().split())
    point_dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
    r_dist = r1+r2
    if x1 == x2 and y1 == y2:#동심원
        if r1 == r2:#같은원, 무한개의 접점
            print(-1)
        else:# 동심원이지만 안만남
            print(0)
    elif point_dist > r_dist:#안만남
        print(0)
    elif point_dist == r_dist:# 접점 1개존재
        print(1)
    elif point_dist == abs(r1-r2):#내접
        print(1)
    elif point_dist < abs(r1-r2):#큰원안에 작은원 포함
        print(0)
    else:
        print(2)

    