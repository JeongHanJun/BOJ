# 11729 하노이 탑 이동 순서
'''
 < 로직 > 
# src = source(출발지) = start , mid = 중간지점, dst = destination = end = 마지막 및 도착점

 src        mid         dst  이렇게 3개의 막대가 있고

 n개의 원반이 src에 있다고 하면
 1.  n-1개의 원반을 mid로 옮긴다. (n==1인 경우 제외이므로 이것이 종료조건) , 이 때 경유해야할 막대 dst
 2. 제일큰 원반(남은 1개의 원반)을 dst로 옮긴다.
 3. mid에 있는 n-1개의 원반을 dst로 옮긴다. 이때 경유해야할 막대는 src


'''


'''
def hanoi(n, src, mid, dst):
    if n == 1:
        print(src, dst)
    else:
        hanoi(n-1, src, dst, mid)
        print(src, dst)
        hanoi(n-1, mid, src, dst)
n = int(input())
hanoi(n, 1, 2, 3)
'''
# 성공코드, 시간이 복잡함( 재귀라서 )
'''
def hanoi(n, start, mid, end):
    answer[0] += 1
    if n == 1:
        answer.append(start)
        answer.append(end)
    else:
        hanoi(n-1, start, end, mid)
        answer.append(start)
        answer.append(end)
        hanoi(n-1, mid, start, end)
n = int(input())
answer = []
answer.append(0)
hanoi(n, 1, 2, 3)
print(answer[0])
for i in range(2,len(answer), 2):
    print(answer[i-1], answer[i])
'''

# 흥미로운 코드
n = int(input())
str_0 = '1 3\n'
for i in range(n-1):#2의 n-1승 이 이동횟수이므로
     str_1 = str_0.replace('3', '4').replace('2', '3').replace('4', '2')
     str_2 = '1 3\n'
     str_3 = str_0.replace('1', '4').replace('2', '1').replace('4', '2')
     str_0 = str_1+str_2+str_3
print(2**n-1)
print(str_0)

