# 9461 파도반 수열
t = int(input())
p = [1] * 101
for _ in range(t):
    n = int(input())
    for i in range(3, n+1):
        p[i] = p[i-2] + p[i-3]
    print(p[n-1])