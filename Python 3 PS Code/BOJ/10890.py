# 10890 알파벳 찾기
# a b c d e  f g h i j  k l m n o  p q r s t  u v w x y  z
#
#  아래 코드는 각 알파벳 출력된 횟수, 처음에 문제 의도가 이것인줄로 잘못해석 ㅜ
""" 
from sys import stdin
word = stdin.readline().strip()
split_word = list(map(str, word))
answer = []
for i in range(26):
    alpha = chr(97+i)
    cnt = 0
    for j in split_word:
        if j == alpha:
            cnt += 1
    answer.append(cnt)
for i in answer:
    print(i, end=" ")
"""

from sys import stdin
word = stdin.readline().strip()
split_word = list(map(str, word))
answer = [-1] * 26
for i in split_word:
    # 이부분에 if answer[ord(i)-97] == -1: 을 써서 조건을 거는 방법도 있으나, 이미 기존에 값이 저장되면 다시 갱신되지 않으므로 상관없다.
    answer[ord(i)-97] = word.index(i)
for i in answer:
    print(i, end = " ")


# 감명깊은 짧고 굵은 코드
# 비교 및 검색의 관점을 바꾸는 코드
# 알파벳 문자열 변수를 따로 만들고, 입력된 문자열과 비교함, 이떄 리스트 내장함수 find를 사용하여서
# 자연적으로 입력된 문자열에 알파벳이 없는경우 -1을 return하도록(return False) 하는 것이 인상깊었던 코드
'''
str = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in alpha:
    print(str.find(i), end = " ")
'''
