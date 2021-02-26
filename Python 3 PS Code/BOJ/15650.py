# 15650 N과 M (2)
# 1 ~ n 까지 중복없이 오름차순 m 개의 수열
from itertools import combinations
n, m = map(int, input().split())
nums = map(str, range(1, n+1))
'''
for i in list(map(' '.join, combinations(nums, m))):
    print(i)
'''
print('\n'.join(list(map(' '.join, combinations(nums, m)))))