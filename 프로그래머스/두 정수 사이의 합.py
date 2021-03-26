# 두 정수 사이의 합
'''
def solution(a, b):
    if a == b:
        return a
    else:
        m = min(a, b)
        M = max(a, b)
        answer = 0
        for i in range(m, M+1):
            answer += i
        return answer
'''
# 간단한 풀이 1
'''
def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b+1))
'''
def solution(a, b):
    return ( abs(a-b) + 1) * (a+b) // 2