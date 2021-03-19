# 1759 암호 만들기
'''
<조건>
1. C개의 알파벳중 L개를 조합하여 암호를 만든다. ( 1 <= L <= C <= 15 )
2. 알파벳에는 최소 1개의 모음(a, e, i, o, u)과 최소 2개의 자음이 사용된다.
3. 암호는 알파벳순으로 정렬되어있다.
4. 1,2,3을 만족하는 암호들을 모두 출력
'''
from itertools import combinations
L, C = map(int, input().split())
letters = sorted(input().split())

temp = list(combinations(letters, L))
for pw in temp:
    cnt_a = 0
    cnt_b = 0
    for k in pw:
        if k in 'aeiou':
            cnt_a += 1
        else:
            cnt_b += 1
    if cnt_a >= 1 and cnt_b >= 2:
        print(''.join(pw))