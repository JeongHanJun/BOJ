# 1193 분수찾기
'''
1   1/1
2   1/2
3   2/1
4   3/1
5   2/2
6   1/3
x번째 분수를 구해라
분모 + 분자의 합 -> 2   3    4   5   6 ...
                   1   
시작점             1    2   4   7   11  16
                     1    2   3   4    5   -> 시작점 = (n*n +n)/2 + 1
끝점               1    3   6   10  15  21  
                     2    3   4   5   6    -> 끝점 = (n*n + 3n)/2 + 1
i line
0 1
1 3
2 4
3 5

'''
n = int(input())
for i in range(n):
    e = (i*i + 3*i)/2 + 1
    if n > e:
        continue
    else:
        s = (i*i + i)/2 + 1
        if i % 2 == 0:
            print(str(int(e-n+1))+'/'+str(int(n-s+1)))
            break
        else:
            print(str(int(n-s+1))+'/'+str(int(e-n+1)))
            break



'''
# 대각선의 방향이 변하지 않고 아래에서 위로 ( 시계기준 7시에서 1시 방향으로 ) 진행될 경우의 코드
n = int(input())
for i in range(n):
    e = (i*i + 3*i)/2 + 1
    if n > e:
        continue
    else:
        s = (i*i + i)/2 + 1
        print(str(int(e-n+1))+'/'+str(int(n-s+1)))
        break
'''