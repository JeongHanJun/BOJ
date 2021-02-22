# 1181 단어 정렬
# 리스트로 하면 중복시 중복출력된다.
# 1. 직관적인 코드
'''
from sys import stdin
words = {}
for i in range(int(stdin.readline())):
    words[stdin.readline().strip()] = i
words_list = sorted(words.keys(), key= lambda x: (len(x), x ) )
for i in words_list:
    print(i)
'''
# 2. 빠른 코드
from sys import stdin
nums = []
for i in range(int(stdin.readline())):
    nums.append(stdin.readline())
print(''.join(list(sorted(sorted(set(nums)), key = lambda s: len(s)))))