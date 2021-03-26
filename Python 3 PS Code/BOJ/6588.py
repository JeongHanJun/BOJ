# 골드바흐의 추측
'''
4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
'''
# 6 <= n <= 1000000
# 반례 조심할것   999998 = 19 + 999979
'''
# 첫번쨰 시도 코드 , 시간초과
from sys import stdin
def IsPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

nums = []
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    nums.append(n)

prime_nums = [ i for i in range(2, max(nums)) if IsPrime(i)]

for a in range(len(nums)):
    check = False
    for i in prime_nums:
        if nums[a]-i in prime_nums:
            check = True
            break
    if check:
        print(str(nums[a])+" = "+str(i)+" + "+str(nums[a]-i))
        #print("%d = %d + %d"%(nums[a], i, nums[a]-i))
    else:
        print("Goldbach's conjecture is wrong.")
'''
# 2번째, 성공한 풀이
from sys import stdin
nums = []
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    nums.append(n)

m = max(nums)
checks = [ True for _ in range(m) ]

for i in range(2, int(m**0.5) + 1):
    if checks[i]:
        for j in range(i*i, m, i):
            checks[j] = False

for n in nums:
    if n == 0:
        break
    check = False

    for i in range(3, m):
        if checks[i] and checks[n-i]:
            check = True
            break
    if check:
        print("%d = %d + %d"%(n, i, n-i))
    else:
        print("Goldbach's conjecture is wrong.")