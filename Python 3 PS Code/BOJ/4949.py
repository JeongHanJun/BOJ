# 4949 균형잡힌 세상
'''
from sys import stdin
while True:
    line = list(stdin.readline().rstrip())
    if line == '.':
        break
    stack = []
    check = True
    for e in line:
        if e == '(' or e == '[':
            stack.append(e)
        elif e == ')':
            if not stack and stack[-1] == '(':
                stack.pop()
            else:
                check = False
                break
        elif e == ']':
            if not stack and stack[-1] == '[':
                stack.pop()
            else:
                check = False
                break
    if check and not stack:
        print('yes')
    else:
        print('no')
'''
#2. 빠른 풀이
from sys import stdin, stdout

def isvalid(s):
    stack = []
    for c in s:
        if c in '([':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                return False
        elif c == ']':
            if not stack or stack.pop() != '[':
                return False
    return not stack

strings = stdin.readlines()
strings.pop()
for string in strings:
    stdout.write("yes\n" if isvalid(string) else "no\n")