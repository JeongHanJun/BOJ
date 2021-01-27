# 2839 설탕 배달
'''
3kg짜리, 5kg짜리봉지에
입력받은 설탕의 양을 분배
nkg배달시 몇개의 봉지가 필요한가?
만약 담을수없다면 '-1'을 출력
n = 3a + 5b
'''

# 1번째 방법) while문 안에서 전체 돌리기
'''
#n = int(input())
from sys import stdin
n = int(stdin.readline().strip())
cnt = 0
while True:
    if n % 5 == 0:
        print(cnt + n//5)
        break
    else:
        n -= 3
        cnt += 1
        if n < 0:
            print(-1)
            break
'''
# 2번쨰 방법 while문 돌리고 밖에서 판별
from sys import stdin
n = int(stdin.readline().strip())
cnt = 0
while n % 5 != 0 and n >= 0:
    n -= 3
    cnt += 1
if n < 0:
    print(-1)
else:
    cnt += n//5
    print(cnt)