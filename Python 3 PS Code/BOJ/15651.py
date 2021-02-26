# 15651 N과 M (3)
# 1 ~ n 까지 중복허용한 m개의 수열 - Cardesioan product
from itertools import product
n, m = map(int, input().split())
nums = map(str, range(1, n+1))
'''
for i in list(map(' '.join, product(nums, repeat = m))):
    print(i)
'''
print('\n'.join(list(map(' '.join, product(nums, repeat = m)))))