# 2675 문자열 반복
""" 
from sys import stdin
t = int(stdin.readline().strip())
for i in range(t):
    testcase = list(stdin.readline().strip().split())
    split_word = list(map(str, testcase[1]))
    #print(testcase)
    #print(split_word)
    for j in range(len(split_word)):
        for k in range(int(testcase[0])):
            print(split_word[j], end = '')
    print()
"""
# 위의 코드를 리스트를 사용하지 않고 좀더 깔끔하게 작성한코드, 시공간복잡도는 동일함
from sys import stdin
t = int(stdin.readline().strip())
for i in range(t):
    n,line = stdin.readline().strip().split()
    for j in line:
        print(j * int(n), end = '')
    print()