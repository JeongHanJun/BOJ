# 10610 30

#nums = list(map(int, input()))# 이렇게 하면 num을 만들때 힘듬
nums = list(input())
nums = sorted(nums, reverse = True)
num = int(''.join(nums))
if num % 30 == 0:
    print(num)
else:
    print(-1)

'''
n = sorted(list(input()), reverse = True)
if n[-1] != 0 or sum(map(int, n)) % 3 != 0:
    print(-1)
else:
    print(''.join(n))
'''