# 15652 N과 M (4)
# 1 ~ n까지 m개를 고른 수열, 같은수를 중복해서 골라도 되고, 비내림차순, 
from itertools import combinations_with_replacement
n, m = map(int, input().split())
nums = map(str, range(1, n+1))
for i in list(map(' '.join, combinations_with_replacement(nums, m))):
    print(i)