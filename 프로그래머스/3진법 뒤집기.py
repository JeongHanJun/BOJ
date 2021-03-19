# 3진법 뒤집기
'''
# 정석 풀이 3진수로 변환후 다시 10진수로 변환
def solution(n):
    temp = ''
    while n > 0:
        #temp = str(n%3) + temp
        temp += str(n%3)
        n //= 3
    m = 0
    for idx, val in enumerate(temp[::-1]):
        m += (3 ** idx) * int(val)
    return m
'''
# 더 좋은 풀이 int함수의 활용
def solution(n):
    temp = ''
    while n:
        temp += str(n%3)
        n //= 3
    answer = int(temp, 3)
    return answer
n1 = 45
n2 = 125
print(solution(n1))
print(solution(n2))
