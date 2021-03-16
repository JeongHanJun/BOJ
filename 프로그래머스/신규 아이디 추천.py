# 신규 아이디 추천
'''
id 조건
3 ~ 15글자 , 알파벳소문자/숫자/-/_/. 만 사용가능, . 는 처음과 끝, 연속으로 사용 불가        - = 45   . = 46  _ 95
1. lower()
2. 위의 문자를 제외한 모든 문자 제거
3. 마침표가 2번이상 반복되면 1개로 치환
4. 마침표가 처음이나 끝에 위치하면 제거
5. 빈문자열이라면 a 를 대입
6. 16자 이상이면 첫 15개를 제외한 나머지 문자 제거, 제거후 15번째가 . 이면 그 . 를 제거
7. 2자 이하라면 길이가 3이 될때까지 반복해서 끝에 붙임
'''
def solution(new_id):
    answer = ''
    letters = list(new_id.lower())# 1번
    for e in new_id.lower():
        if e.isalnum() or e in '-_.':
            answer += e
    # 이상 2번
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 이상 3번
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    # 이상 4번
    if answer == '':
        answer = 'a'
    # 이상 5번
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 이상 6번
    if len(answer) < 3 and len(answer) > 0:
        answer += answer[-1] * (3-len(answer))
    # 이상 7번
    return answer

'''
n1 = "...!@BaT#*..y.abcdefghijklm"                  #       "bat.y.abcdefghi"

n2 = "z-+.^."                                       #       "z--"

n3 = "=.="                                          #       "aaa"

n4 = "123_.def"                                     #       "123_.def"

n5 = "abcdefghijklmn.p"                             #       "abcdefghijklmn"
print(solution(n1))
print(solution(n2))
print(solution(n3))
print(solution(n4))
print(solution(n5))
'''