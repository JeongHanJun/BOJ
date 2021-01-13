# 11654 아스키 코드
#print(ord(input()))
# 위의 방법도 괜찮으나 아래 방법이 익숙해지는것이 좋고, strip으로 개행문자를 없애야 원활한 출력이 가능하다.
from sys import stdin
print(ord(stdin.readline().strip()))