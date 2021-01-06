#2562 최댓값
'''
import sys
num_list = []
max = 0
idx = 0
num_list = sys.stdin.read().split()
for i in range(9):
    if int(num_list[i]) >= max:
        max = int(num_list[i])
        idx = i
print(max)
print(idx+1)
'''

# 2562 최댓값 다른방법
from sys import stdin
num_list = [int(stdin.readline()) for i in range(9)]
print(max(num_list))
print(num_list.index(max(num_list))+1)
