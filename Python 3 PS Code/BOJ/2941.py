# 2941 크로아티아 알파벳
'''
크로아티아 알파벳 종류
c=
c-
dz=
d-
lj
nj
s=
z=

위 목록에 없는 알파벳은 1글자로 인식
lj 와 nj같은경우는 조심해야하는게
l j 와  n j 로 인식하면 안된다는게 문제의 포인트

입력된 문자열에 대해 크로아티아알파벳의 갯수를 출력

ex) ljes=njak -> lj, e, s=, nj, a, k 6개
ddz=z= -> d, dz=, z= 3개
nljj = n, lj, j 3개
c=c= -> c=, c= 2개
'''

from sys import stdin
line = stdin.readline().strip()
cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
letters = 0
for i in range(8):
    if line.count(cro_list[i]) > 0:
        cnt = line.count(cro_list[i])
        for j in range(cnt):
            #line.replace( line[ line.find(cro_list[i]) : line.find(cro_list[i])+len(cro_list[i]) ] , '')#코드 실행전후결과가 다른게 없는데 뭐가 이상한건지 모르겠다.
            #line = line[0:line.find(cro_list[i])] + line[line.find(cro_list[i])+len(cro_list[i]):]# 이렇게 하면 nljj 와 같이 크로아티아 알파벳이 중첩되있을때 실패하는 코드
            line = line[0:line.find(cro_list[i])] +' '+ line[line.find(cro_list[i])+len(cro_list[i]):]
            #letters += 1
            #print(line, letters)
    else:
        pass
letters += len(line)
print(letters)


# 감명깊은 한줄코드
# 전체길이에서 크로아티아 알파벳은 제외하고 출력하는 로직, 상당히 인상깊었다.
'''
line = input()
print(len(line) - sum(map(line.count, ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] )))
'''
