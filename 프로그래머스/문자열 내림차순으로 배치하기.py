# 문자열 내림차순으로 배치하기
'''
def solution(s):
    ls = list(s)
    temp = sorted(ls, key = lambda x : ord(x), reverse=True)
    return ''.join(temp)
'''
#위를 좀더 간결히
# 포인트는 sorted 함수를 문자열에 쓰면 자동으로 정렬된 리스트가 된다는 점
def solution(s):
    return ''.join(sorted(s, reverse = True))

'''
s = "Zbcdefg"
print(solution(s))
'''