# 2231 분해합
# 1. 리스트 안에 생성자들을 넣고 그중의 최소값을 반환
'''
n = int(input())
temp = max(n - 9*(len(str(n))), 0)
answer = []
for num in range(temp, n+1):
    #if sum( [ int(i) for i in str(num)] ) + num == n:
    if num + sum(map(int, str(num))) == n:
        answer.append(num)
if len(answer) == 0:
    print(0)
else:
    print(min(answer))
'''
# 2. bool 변수를 통해 for문의 최소값에너 나온값을 바로 출력
n = input()
ni = int(n)
temp = max(ni - 9*(len(n)), 0)
find = True
for num in range(temp, ni+1):
    if num+sum(map(int, str(num))) == ni:
        print(num)
        find = False
        break
if find:
    print(0)

