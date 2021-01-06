# 3052 나머지
# 방법1 입력받고 if문으로 나머지를 판별하여 리스트에 추가하기
''' 
from sys import stdin
answer = []
for i in range(10):
    a = int(stdin.readline())
    if a % 42 in answer:
        pass
    else:
        answer.append(a % 42)
#print(answer)
print(len(answer))
'''
# 방법 2 입력받음과 동시에 나머지연산을 수행하고 중복제거를 위해 set으로 변환해서 출력하는 법
from sys import stdin
answer = [ (int(stdin.readline()) % 42) for i in range(10) ]
print(len(set(answer)))