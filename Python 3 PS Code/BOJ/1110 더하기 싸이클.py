import sys
n = int(sys.stdin.readline())
temp = n
cnt = 0
while True:
    n1 = int(temp % 10)
    n10 = int(temp / 10)
    d = n1 + n10
    temp = n1 * 10 + d % 10
    cnt += 1
    if temp == n :
        break
print(cnt)