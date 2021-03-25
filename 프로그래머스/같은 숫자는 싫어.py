# 같은 숫자는 싫어
def solution(arr):
    n = len(arr)
    answer = []
    answer.append(arr[0])
    for i in range(1, n):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer

a1 = [1, 1, 3, 3, 0, 1, 1]
a2 = [4, 4, 4, 3, 3]
print(solution(a1))
print(solution(a2))
