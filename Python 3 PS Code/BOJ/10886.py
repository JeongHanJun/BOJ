# 10886 0 = not cute / 1 = cute
c0, c1 = 0, 0
for _ in range(int(input())):
    if int(input()):
        c1 += 1
    else:
        c0 += 1
if c1 > c0:
    print("Junhee is cute!")
else:
    print('Junhee is not cute!')