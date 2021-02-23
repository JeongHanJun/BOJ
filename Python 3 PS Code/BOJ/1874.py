# 1874 스택 수열
'''  예시로 43687521이 \n을 기준으로 주어졌을떄
43687521 아래줄은 스택, 그 아래줄은 출력할 문자열
1   12  123 1234    123 12  125 1256    125 1257    12578   1257    125     12          1           
                    4   43              436                 4368    43687   436875      4368752     43687521
'''
'''
# 실패 코드
from sys import stdin
n = int(stdin.readline())
nums, stack, answer = [], [], []
cnt = 0
for _ in range(n):
    nums.append(int(stdin.readline()))
for i in range(1, n+1):
    if len(stack) == 0 or nums[cnt] != i:
        stack.append(i)
        answer.append('+')
    else:# 스택이 차있고, nums[cnt] == i인 경우
        stack.append(i)
        answer.append('+')
        stack.pop()
        del nums[cnt]
        cnt += 1
        answer.append('-')
print(stack)
print(nums)
print(answer)
'''
'''
# 2. 성공코드 1
from sys import stdin
stack, answer = [], []
cnt = 1
check = True
n = int(stdin.readline())
for i in range(n):
    num = int(stdin.readline())
    while cnt <= num:
        stack.append(cnt)
        answer.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        check = False
if check == False:
    print('NO')
else:
    for i in answer:
        print(i)
'''
# 3. 성공코드 2
from sys import stdin
def solution():
    stack, result, cnt = [], [], 1
    for n in nums:
        while cnt <= n:
            stack.append(cnt)
            result.append('+')
            cnt += 1
        if stack.pop() != n:
            return 'NO'
        else:
            result.append('-')
    return '\n'.join(result)


t = int(stdin.readline())
nums = map(lambda x: int(x.rstrip()), stdin.readlines())
print(solution())
