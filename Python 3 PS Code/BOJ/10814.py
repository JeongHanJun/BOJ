# 10814 나이순 정렬
'''
#1. 실패 코드
from sys import stdin
nums = {}
for _ in range(int(stdin.readline())):
    age, name = stdin.readline().split()# 여기서 age 는 int로 name은 str로 되야하는데 이 부분이 안됨
    nums[name] = age

for i, j in sorted(nums.items(), key = lambda x: x[1]):
    print(j, i)
'''
#2. 감명받은 코드
from sys import stdin
nums = sorted( [ stdin.readline() for _ in range(int(stdin.readline())) ], key= lambda x: int(x.split()[0]))
print(''.join(nums))