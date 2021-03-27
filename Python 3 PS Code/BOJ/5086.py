# 5086 배수와 약수
# 1만 이하의 2개의 자연수, 둘이 같은경우는 없다.
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')
