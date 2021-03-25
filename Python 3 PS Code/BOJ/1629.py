# 1629 곱셈

def mul(a, b):
    if b == 1:
        return a % c
    else:
        half = mul(a, b//2)
        if b % 2 == 0:
            return half * half % c
        else:
            return half * half * a % c

a, b, c = map(int, input().split())
print(mul(a, b))