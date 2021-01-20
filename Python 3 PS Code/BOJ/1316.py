# 1316 그룹 단어 체거

# 입력된 문자열을 쪼개서 리스트에 담아서 비교하는법
'''
from sys import stdin
n = int(stdin.readline().strip())
cnt = 0
for i in range(n):
    line = list(map(str, stdin.readline().strip()))
    check = True
    alphas = []
    for j in range(len(line)):
        if line[j] in alphas:
            if line[j-1] != line[j]:
                check = False
                break
        else:
            alphas.append(line[j])
    if check:
        cnt += 1
print(cnt)

'''
# 입력된 문자열을 비교하는 방법
from sys import stdin
n = int(stdin.readline().strip())
cnt = 0
for i in range(n):
    line = stdin.readline().strip()
    for j in range(len(line)-1):
        if line.find(line[j]) > line.find(line[j+1]):
            # 기본적으로 find함수는 찾을 문자열의 가장 앞에부분, index가 작은 부분을 반환하는데
            # 만약 같은 알파벳의 경우 find값은 같은 값을 리턴해야하고
            # 정상적인 그룹단어의 경우에는 index가 적은 부분이 먼저 나와야 하므로
            # 해당 if문의 조건처럼 index가 작은부분의 find값이 더 큰 경우는 같은 알파벳이 연속되지 않게 등장한경우이다.
            # ex) abcabc  에서 j = 2일때, c와 다시등장한 a를 비교하는데 이떄 2 > 0 이므로 그룹단어에 해당하지 않는다.
            cnt += 1
            break
print(n - cnt)