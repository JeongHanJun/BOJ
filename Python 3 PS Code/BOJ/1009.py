# 1009 분산처리
'''
    0   0
    1   1
    2   2   4   6   8   0
    3   3   9   7   1
    4   4   6
    5   5
    6   6
    7   7   9   3   1
    8   8   4   2   6
    9   9   1

'''
t = int(input())
nums = [ [2, 4, 8, 6], [3, 9, 7, 1], [7, 9, 3, 1], [8, 4, 2, 6] ]
for _ in range(t):
    c, b = map(int, input().split())
    c %= 10
    if c == 1 or c == 5 or c == 6:
        print(c)
        continue
    elif c == 2:
        print(nums[0][b%4-1])
        continue
    elif c == 3:
        print(nums[1][b%4-1])
        continue
    elif c == 4:
        if b % 2 == 0:
            print(6)
        else:
            print(4)
        continue
    elif c == 7:
        print(nums[2][b%4-1])
        continue
    elif c == 8:
        print(nums[3][b%4-1])
        continue
    elif c == 9:
        if b % 2 == 0:
            print(1)
        else:
            print(9)
        continue
    else:#c == 10
        print(10)

'''
    elif c == 5:
        print(5)
        continue
    elif c == 6:
        print(6)
        continue
'''