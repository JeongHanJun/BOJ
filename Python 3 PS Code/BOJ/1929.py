# 1929 소수 구하기
# 1. 소수인지 판별하고 소수면 출력
'''
from sys import stdin
m,n = map(int, stdin.readline().strip().split())
def IsPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

for i in range(m, n+1):
    if IsPrime(i):
        print(i)
'''
# 2. bisect 모듈사용
def IsPrime(n):
    if n < 2:
        return []
    else:
        n += 1
        save = [True] * (n//2)
        for i in range(3, int(n**0.5)+1, 2):# 3부터 2간격으로 루트n까지, 2는 마지막에 출력할때 포함
            if save[i//2]:
                k = i * i
                save[k//2::i] = [False] * ( (n-k-1) // (2*i)+1 )
    return [2] + [2*i+1 for i in range(1, n//2) if save[i]] 

from bisect import bisect_left as bl
m, n = map(int, input().split())
s = IsPrime(n)
print(*s[bl(s, m):])

'''
ex1) n = 16 -> 17
save = [True] * 8
for문 i = 3
save[3] == True -> k = 9, save[4::3] = [False] * ( 1 ) -> 5, 8번쨰는 False
save =  [T, T, T, T, F, T, T, F]
출력i=1부터
return   x, 3, 5, 7, x, 11, 13, x  결국  2, 3, 5, 7, 11, 13 출력됨
2를 제외한 소수들은 홀수라는 점을 이용
또한 n까지의 소수들은 n//2 개 이하라는 점을 이용( save = [True] * n//2) 

ex2) n = 30 -> 31
save = [True] * 15
fori = 3 ~ 5
1) i = 3 -> k = 9, save[4::3] = save[4, 7, 10, 13] = [False] * 1 
    save = [T, T, T, T, F, T, T, F, T, T, F, T, T, F, T, T]

2) i = 5 -> k = 25, save[12::5] = save[12] = [False] * 0
    save = [T, T, T, T, F, T, T, F, T, T, F, T, x, F, T, T]
            x, 3, 5, 7, 9, 11,13,15,17,19,21,23,25,27,29,31
    print(2,   3, 5, 7,    11,13,   17,19,   23,      29)
'''