# 2108 통계학
# 1. 시간초과 코드
'''
from sys import stdin
n = int(stdin.readline())
nums = sorted(list(map(int, stdin.read().split())))
s = sum(nums)
l = len(nums)
print(round(s/l))#산술평균
print(nums[l//2])#중앙값
#최빈값
num_dict = {}
for i in range(l):
    num_dict[nums[i]] = nums.count(nums[i])
max_keys = [ k for k, v in num_dict.items() if max(num_dict.values()) == v]
max_values = [ v for k, v in num_dict.items() if max(num_dict.values()) == v]
if len(max_values) == 1:
    print(max_keys[0])
else:
    print(max_keys[1])

print( nums[-1] - nums[0])#범위
'''

#2. 런타임 오류 코드
'''
from sys import stdin
from collections import Counter
n = int(stdin.readline())
nums = sorted(list(map(int, stdin.read().split())))
s = sum(nums)
l = len(nums)
print(round(s/l))#산술평균
print(nums[l//2])#중앙값

#num_dict = Counter(nums)

for num in nums:
    if num not in num_dict:
        num_dict[num] = 0
    num_dict[num] += 1
# 지금 단체주석된 이 사전으로 카운팅하는 부분이 위으 num_dict = Counter(nums) 한 줄과 같은 코드이다.

c = Counter(nums).most_common(2)
if c[0][1] == c[1][1]:
    print(c[1][0])
else:
    print(c[0][0])
print(c[1][0] if c[0][1] == c[1][1] else c[0][0])
print( nums[-1] - nums[0])#범위
'''

# 3. 
from sys import stdin
from collections import Counter
n = int(stdin.readline())
nums = sorted(list(map(int, stdin.read().split())))

print(round(sum(nums)/n))

if n == 1:
    print(nums[0])
    print(nums[0])
else:
    print( nums[n//2] if n % 2 != 0 else round( (nums[n//2]+nums[n//2 +1])/2 ) )
    c = Counter(nums).most_common(2)
    print(c[1][0] if c[0][1] == c[1][1] else c[0][0])
print(nums[-1] - nums[0])

