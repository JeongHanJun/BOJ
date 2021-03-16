# 모의고사
'''

1   1 2 3 4 5   1 2 3 4 5   1 2 3 4 5   1 2 3 4 5       5단위

2   2 1 2 3 2 4 2 5     2 1 2 3 2 4 2 5     2 1 2 3     8단위

3   3 3 1 1 2 2 4 4 5 5   3 3 1 1 2 2 4 4 5 5           10단위


'''
def solution(answers):
    answer = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    results = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == a1[i % 5]:
            results[0] += 1
        if answers[i] == a2[i % 8]:
            results[1] += 1
        if answers[i] == a3[i % 10]:
            results[2] += 1
    for i in range(3):
        if results[i] == max(results):
            answer.append(i+1)
    return answer
    
'''
t1 = [1, 2, 3, 4, 5]#   1
t2 = [1, 3, 2, 4, 2]#   1   2   3
print(solution(t1))
print(solution(t2))
'''