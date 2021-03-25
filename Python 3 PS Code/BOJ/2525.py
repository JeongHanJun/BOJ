# 2525 오븐 시계
a, b = map(int, input().split())
c = int(input())
a += (c // 60)
b += (c % 60)
if b >= 60:
    a += (b//60)
    b -= (b // 60) * 60
if a >= 24:
    a -= 24
print(a, b)