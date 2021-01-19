# 5622 다이얼
'''
1               2s
2   A, B, C     3s
3   D, E, F     4s
4   G, H, I     5s
5   J, K, L     6s
6   M, N, O     7s
7   P, Q, R, S  8s
8   T, U, V     9s
9   W, X, Y, Z  10s
0
숫자를 누르면 다이얼이 처음으로 돌아간다.
1을 걸려면 2초가 필요하고
1보다 큰수는 1초씩 더 걸린다.

EX) UNUCIC == 숫자 ( 8, 6, 8, 2, 4, 2) -> 9s + 7s + 9s + 3s + 5s + 3s == 36s

문제 풀이 방법 해당 알파벳들을 if문으로 해서 합산
'''
from sys import stdin
line = list(map(str, stdin.readline().strip()))
answer = 0
for i in line:
    if i == 'A' or i == 'B' or i == 'C':
        answer += 3
    elif i == 'D' or i == 'E' or i == 'F':
        answer += 4
    elif i == 'G' or i == 'H' or i == 'I':
        answer += 5
    elif i == 'J' or i == 'K' or i == 'L':
        answer += 6
    elif i == 'M' or i == 'N' or i == 'O':
        answer += 7
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        answer += 8
    elif i == 'T' or i == 'U' or i == 'V':
        answer += 9
    else:
        answer += 10
print(answer)