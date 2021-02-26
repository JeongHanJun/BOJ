# 9184 신나는 함수 실행
''' -50 <= a, b, c <= 50 이지만
문제의 조건
    1. if a <= 0 or b <= 0 or c <= 0 :
            w(a, b, c) = w(0, 0, 0) = 1 
    2. if a > 20 or b > 20 or c > 20:
            w(a, b, c) = w(20, 20, 20) 
'''
from sys import stdin
M = 21
dp = [[[0]*M for _ in range(M)] for _ in range(M)]
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

while True:
    a, b, c = map(int, stdin.readline().rstrip().split())
    if a == -1 and b == -1 and c == -1:
        break    
    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))
    #print('w(%d, %d, %d) = %d'%(a, b, c, w(a, b, c)))