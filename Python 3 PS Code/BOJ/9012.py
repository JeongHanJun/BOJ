# 9012 괄호
'''
#1. 무난한 성공 코드
from sys import stdin
for _ in range(int(stdin.readline())):
    stack = []
    line = list(stdin.readline().rstrip())
    for i in line:
        if i == ')':
            if '(' in stack:
                stack.remove('(')
            else:
                stack.append(')')
                break
        else:
            stack.append(i)
    if stack:
        print('NO')
    else:
        print('YES')
'''
#2 다른 성공코드
from sys import stdin
for _ in range(int(stdin.readline())):
    c = 0
    l = stdin.readline().rstrip()
    for e in l:
        if e == '(':
            c += 1
        else:
            c -= 1
            if c < 0:
                break
    if c: print('NO')
    else: print('YES')
