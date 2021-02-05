# 2749 피보나치 수 3
'''
문제의 포인트 = 재귀 or 반복문을 사용하지 않고 행렬의 곱셈으로 피보나치를 해결 -> O(logn)
* 만약 2^64을 계산하려면 2를 64번곱할것인가?
위보다 빠른 방법중 하나로 2를 제곱한것을 제곱한것을 제곱한것을....제곱하는 것이다.
2^ (2 -> 4 -> 8 -> 16 -> 32-> 64) log2 (64) =  6    6번만에 가능하다. 64번 vs 6번

행렬의 곱셈의 개념으로는 모든 자연수는 2의 제곱수의 합으로 표현이 가능하다는 점도 이용한다.
(2의 제곱수에는 1과 2, 2의 제곱수들이므로, 이들의 합으로 모든 자연수를 표현할수 있다.)


[ 1 1 ]^n = [ F(n+1) Fn    ]
[ 1 0 ]   = [ F(n)   F(n-1)]  을 이용한다.

[ F(n)  ] = [ 1 1 ] [ F(n-1) ]    -->   [ F(n)  ] = [ 1 1 ]^(n-1) [ F(1) ]
[ F(n-1)] = [ 1 0 ] [ F(n-2) ]    -->   [ F(n-1)] = [ 1 0 ]       [ F(0) ]

'''
# 1. 위의 내용을 코드로
''' 
from sys import stdin
p = 1000000

def dot(mat1, mat2):
    N = len(mat1)
    M = len(mat2)
    K = len(mat1[0])
    ansmat = [[0 for _ in range(K)] for _ in range(N)]
    for i in range(N):
        for j in range(K):
            temp = 0
            for k in range(M):
                temp += mat1[i][k] * mat2[k][j] % p
            ansmat[i][j] = temp % p
    return ansmat

def power(mat, b):
    # 행렬의 제곱은 무조건 N * N꼴이다.
    N = len(mat)
    ret = [[0 for _ in range(N)] for _ in range(N)]
    # ret = 단위행렬
    for i in range(N):
        ret[i][i] = 1

    while b>0 :
        if b%2 :
            ret = dot(mat, ret)
        mat = dot(mat, mat)
        b //= 2
    return ret

n = int(stdin.readline().strip())
mat = [[1, 1], [1, 0]]
if n == 1:
    print(1)
else:
    fibmat = power(mat, n-1)
    ans = fibmat[0][0]
    print(ans)
'''
# 1번보다 좀 더  이해가 쉬운 코드
def mul(a, b):
    x1 = (a[0]*b[0] + a[1]*b[2]) % 1000000
    x2 = (a[0]*b[1] + a[1]*b[3]) % 1000000
    x3 = (a[2]*b[0] + a[3]*b[2]) % 1000000
    x4 = (a[2]*b[1] + a[3]*b[3]) % 1000000
    return x1,x2,x3,x4

def fib(n):
    a, b = (1,0,0,1), (1,1,1,0)
    while n > 0:
        if n & 1:
            a = mul(a, b)
        b = mul(b, b)
        n >>= 1
    return a[2]

print(fib(int(input())))


# 추가적으로, 피보나치의 일반항 구현이다.
'''
def fib(n):
    s = 5 ** (1/2)
    ans = 1 / s * ( ((1+s)/2)**n - ((1-s)/2)**n )
    return int(ans)
n = int(input())
print(fib(n))
'''