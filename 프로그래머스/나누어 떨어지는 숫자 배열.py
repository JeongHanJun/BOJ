# 나누어 떨어지는 숫자 배열
'''
def solution(arr, divisor):
    answer = []
    for e in arr:
        if e % divisor == 0:
            answer.append(e)
    answer = sorted(answer)
    if len(answer) == 0:
        answer.append(-1)
    return answer
'''
# 간단한 한줄 풀이
def solution(arr, divisor):
    return sorted( [n for n in arr if n % divisor == 0]) or [-1]# 앞이 거짓이면 뒤가 호출
a1 = [5, 9, 7, 10]
d1 = 5
a2 = [2, 36, 1, 3]
d2 = 1
a3 = [3, 2, 6]
d3 = 10
print(solution(a1, d1))
print(solution(a2, d2))
print(solution(a3, d3))