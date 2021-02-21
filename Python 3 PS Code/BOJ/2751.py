# 수 정렬하기 2
'''
def MergeSort(X):
    if len(X) > 1:
        mid = len(X) // 2
        left_X, right_X = X[:mid], X[mid:]
        MergeSort(left_X)
        MergeSort(right_X)
        
        left_index, right_index, index = 0, 0, 0
        while left_index < len(left_X) and right_index < len(right_X):
            if left_X[left_index] < right_X[right_index]:
                X[index] = left_X[left_index]
                left_index += 1
            else:
                X[index] = right_X[right_index]
                right_index += 1
            index += 1
        X[index:] = left_X[left_index:] if left_index != len(left_X) else right_X[right_index:]
'''

from sys import stdin
n = int(stdin.readline())
nums = sorted(list(map(int, stdin.read().split())))
print('\n'.join(map(str, nums)))
