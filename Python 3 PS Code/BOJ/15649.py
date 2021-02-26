# 15649 N과 M (!)
'''
자연수 n,m이 주어졋을때 1~n까지 중복없이 m개를 고른 수열
'''

'''
    itertools 의 조합형 iterators 
    1. product('ABCD, repeat = 2) - Cartesian Product 
        AA, AB, AC, AD, BA, BB, BC, BD, CA, CB, CC, CD, DA, DB, DC, DD
    
    2. permutations('ABCD', 2) - r길이 튜플들, 가능한순서, 반복되는 요소x
        AB, AC, AD, BA, BC, BD, CA, CB, CD, DA, DB, DC
    
    3. combitations('ABCD', 2)  -   r길이 튜플들, 정렬된순서, 반복되는 요소x
        AB, AC, AD, BC, BD, CD

    4. combinations_with_replacement('ABCD', 2) -   r길이 튜플들, 정렬된순서, 반복되는 요소o
        AA, AB, AC, AD, BB, BC, BD, CC, CD, DD
'''

'''
# 1. itertools 에서 permutations 사용
from itertools import permutations
n, m = map(int, input().split())
nums = map(str, range(1, n+1))
print('\n'.join(list(map(' '.join, permutations(nums, m)))))
'''

from itertools import permutations
from sys import stdin
n, m = map(int, stdin.readline().rstrip().split())
nums = map(str, range(1, n+1))
for i in list(map(' '.join, permutations(nums, m))):
    print(i)

'''
#2. itertools 사용하지 않는 경우
def nnm(a, temp, result = []):
    if a == 1:
        for i in temp:
            result.append(i)
            print(' '.join(result))
            result.pop()
            if i == temp[-1] and result != []:
                result.pop()
    else:
        for i in temp:
            temp_copy = temp.copy()
            temp.copy.remove(i)
            result.append(i)
            temp_copy(a-1, temp_copy, result)
            if i == temp[-1] and result != []:
                result.pop()
n, m = map(int, input().split())
nums = [str(i) for i in range(1, n+1)]
nnm(m, nums)'''