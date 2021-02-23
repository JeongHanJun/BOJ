# 10828 스택
from sys import stdin

# 1. 일반적인 성공코드
temp = []
for _ in range(int(stdin.readline())):
    line = stdin.readline().strip()
    if line == 'top':
        if len(temp) == 0:
            print(-1)
        else:
            print(temp[-1])
    elif line == 'empty':
        if len(temp) == 0:
            print(1)
        else:
            print(0)
    elif line =='size':
        print(len(temp))
    elif line == 'pop':
        if len(temp) == 0:
            print(-1)
        else:
            print(temp.pop())
    else:
        a, b = line.split()
        temp.append(int(b))
'''
# 2. 1과 다른점은 비교할시 if 리스트명: 으로 했다는것
from sys import stdin
stack = []
for _ in range(int(stdin.readline())):
    line = stdin.readline().split()
    if line[0] == 'push':
        stack.append(line[1])
    elif line[0] == 'pop':
        if stack: print(stack.pop())
        else: print(-1)
    elif line[0] == 'size':
        print(len(stack))
    elif line[0] == 'empty':
        if stack: print(0)
        else: print(1)
    else:
        if stack: print(stack[-1])
        else: print(-1)
'''
