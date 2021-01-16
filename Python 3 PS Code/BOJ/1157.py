""" # 1157 단어 공부
from sys import stdin
line = list(map(str, stdin.readline().strip().upper()))
#print(line)
alpha = [0] * 26
for i in range(len(line)):
    alpha[ord(line[i])-65] = line.count(line[i])
m = max(alpha)
ml = [i for i, j in enumerate(alpha) if j == m]
if len(ml) >= 2:
    print('?')
#if len[i for i, j in enumerate(alpha) if j == m] >= 2:
#   print('?')
else:
    print(chr(alpha.index(max(alpha))+65))
"""
# 아래 간단한 코드의 로직을 좀더 풀어쓴 정석적인 코드
'''
from sys import stdin
line = list(map(str, stdin.readline().strip().upper()))
alpha = [0] * 26
for i in range(len(line)):
    alpha[ord(line[i])-65] += 1
m = 0
answer = ''
for i in range(26):
    if alpha[i] > m:
        m = alpha[i]
        answer = chr(i+65)
    elif alpha[i] == m:
        answer = '?'
print(answer)
'''
# 가장 간단한 코드, 아스키 코드값을 answer 리스트의 index 와 결합하여 입력하고, 출력할때 비교를 통해 최댓값을 출력
from sys import stdin
line, answer = stdin.readline().strip().upper(), []
for i in range(65,91):
    answer.append(line.count(chr(i)))
print('?'if answer.count(max(answer))>1 else chr(answer.index(max(answer))+65))

# 알파벳 문자열을 만든후 하나하나 비교해보는법(하드코딩)
'''
n = input()
n = n.upper()
alpa='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []
for i in alpa:
  result.append(n.count(i))
if result.count(max(result)) > 1:
  print("?")
else:
  print(alpa[result.index(max(result))])
'''