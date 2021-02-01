# 4948 베르트랑 공준
'''
베르트랑 공준 = 임의의 자연수 n에 대하여 n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다.
'''
# 시간초과 코드 n ~ 2n 의 숫자들에 대해 소수인지 판별하고 카운트  -> 이를 해결하기 위해 #2 에서 미리 소수리스트를 만들고 시작
'''
def IsPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

from sys import stdin
while True:
    n = int(stdin.readline().strip())
    cnt = 0
    if n == 0:
        break
    else:
        for i in range(n+1, 2*n+1):
            if IsPrime(i):
                cnt += 1
    print(cnt)
'''
# 시간초과 코드 2, 미리 소수들의 집합인 리스트를 만들고 나서 그 안에서 탐색 -> 이를 해결하기 위해 소수확인을 더 빠르게, 탐색도 이분탐색으로
'''
from sys import stdin
def IsPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
Pnums = [ i for i in range(3,123456,2) if IsPrime(i)]
Pnums.append(2)
while True:
    n = int(stdin.readline().strip())
    cnt = 0
    if n == 0:
        break
    for i in range(n+1, 2*n+1):
        if i in Pnums:
            cnt += 1
    print(cnt)
'''
# 3. 빠른 소수탐색, 이분검색 활용
def PrimeList(n):
    if n < 2:
        return []
    else:
        n += 1
        save = [True] * (n//2)
        for i in range(3, int(n**0.5)+1, 2):
            if save[i//2]:
                k = i*i
                save[k//2::i] = [False] * ((n-k-1) // (2*i)+1)
    return [2] + [ (2*i+1) for i in range(1, n//2) if save[i] ]

def BiSearch(nums, n):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > n:
            right = mid -1
        else:
            left = mid + 1
    return left

Pnums = PrimeList(123456*2)
while True:
    n = int(input())
    if n == 0:
        break
    print(BiSearch(Pnums, 2*n) - BiSearch(Pnums, n))
