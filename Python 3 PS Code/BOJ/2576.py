# 2576 홀수
'''
nums = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        nums.append(num)
if len(nums) == 0:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))
'''
# filter , lambda 함수를 이용해 입력받을때 걸러서 입력받기
nums = list( filter( lambda x : x%2 == 1, [ int(input()) for _ in range(7) ] ) )
if nums:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)