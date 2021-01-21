# 10250 ACM호텔
'''
h = 호텔의 높이
w = 호텔의 방 수
n = 몇번째 손님
'''

# 아래 코드는 n과 h가 배수 및 약수 관계일때 즉 n % h == 0일때 오류가 남
'''
from sys import stdin
t = int(stdin.readline().strip())
for i in range(t):
    h, w, n = map(int, stdin.readline().strip().split())
    room_floor =  n % h
    room_num = n // h + 1
    print(room_floor * 100 + room_num)
'''
# 내 첫 풀이
'''
from sys import stdin
t = int(stdin.readline().strip())
for i in range(t):
    h, w, n = map(int, stdin.readline().strip().split())
    if n % h == 0:# n이 h의 배수이면 호텔의 최고층에 해당하는 방이다. 이경우 room_floor 를 n%h로 잡으면 0이나므로 오류가 난다.
        room_floor = h
        room_num = n // h
        print(room_floor * 100 + room_num)
    else:
        room_floor = n % h
        room_num = n // h + 1
        print(room_floor * 100 + room_num)
'''

# 짧은 코드 구현을 위한 로직
'''
room_floot = (n-1) % h + 1
room_num = n//h + 1


6 12 10 -> 402
6 12 12 -> 602
'''

# stdin.readline()을 이용한 짧은 코드
'''
from sys import stdin
t = int(stdin.readline().strip())
for i in range(t):
    h, w, n = map(int, stdin.readline().strip().split())
    print(((n-1)%h+1)*100 + (n-1)//h+1)
'''

# input()을 통한 짧은 코드
t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    print(((n-1)%h+1)*100 + (n-1)//h+1)