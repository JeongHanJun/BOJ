# 11727 2xn 타일링 2
'''
1   1
2   3
3   5
4   11
'''
# 리스트를 쓴다면?
'''
from sys import stdin
n = int(stdin.readline())
dp = [1, 1, 3]

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    for i in range(3, n+1):
        dp.append(dp[i-1] + 2 * dp[i-2])
    print(dp[n] % 10007)
'''
# 리스트를 안쓴다면?

from sys import stdin
n = int(stdin.readline())
ans = 3
a, b = 1, 3
if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    for i in range(3, n+1):
        ans = 2*a + b
        a = b
        b = ans
    print(ans % 10007)
# 위 까지는 성공코드, 아래는 실패 코드
# 오류 코드 ( 런타임 에러 - IndexError )
'''
from sys import stdin
n = int(stdin.readline())
dp = [1] * (n+1)
dp[2] = 3
if n < 3:
    print(dp[n])
else:
    for i in range(3, n+1):
        dp[i] = (2 * dp[i-2] + dp[i-1]) % 10007
    print(dp[n])
'''