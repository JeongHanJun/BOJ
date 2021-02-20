# 2750 수 정렬하기


# 1. 일반적 코드
from sys import stdin
n = int(stdin.readline().strip())
nums = []
for _ in range(n):
    nums.append(int(stdin.readline().strip()))
nums.sort()
for i in nums:
    print(i)

'''
# 2. stdout 이용
from sys import stdin, stdout
n = int(stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(stdin.readline()))
nums.sort()
stdout.write('\n'.join(map(str, nums)))
'''