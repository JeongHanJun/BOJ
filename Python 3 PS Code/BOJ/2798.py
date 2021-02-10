# 2798 블랙잭
# 1. 첫번쨰 풀이 직접 다 합산해서 비교해봐야 함 Brute Force
'''
from sys import stdin
n,m = map(int, stdin.readline().strip().split())
cards = list(map(int, stdin.readline().strip().split()))
sum_cards = []
for i in range(n-2):
    for j in range(1,n-1):
        for k in range(2,n):
            if i >= j or j >= k:
                continue
            else:
                if cards[i] + cards[j] + cards[k] <= m:
                    sum_cards.append(cards[i]+cards[j]+cards[k])
print(max(sum_cards))

'''
# 2. 두번쨰 풀이 1번풀이보다 조금 더 빠름  max 내장함수 쓰지않고 변수에 최댓값 받음
from sys import stdin
n,m = map(int, stdin.readline().strip().split())
cards = list(map(int, stdin.readline().strip().split()))
sum_cards = []
max_sum = 0
for i in range(n-2):
    for j in range(1,n-1):
        for k in range(2,n):
            if i >= j or j >= k:
                continue
            else:
                temp = cards[i] + cards[j] + cards[k]
                if max_sum <= temp <= m :
                    max_sum = temp
print(max_sum)

