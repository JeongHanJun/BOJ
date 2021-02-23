# 10773 제로
# 무난한 성공 코드
from sys import stdin
stack = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))
