# 체육복
'''
# testcase #11 실패 코드
def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n+2)
    for i in reserve:
        students[i] += 1
    for i in lost:
        students[i] -= 1
    for i in range(1, n+1):
        if students[i] == 2:
            if students[i-1] == 0:
                students[i] -= 1
                students[i-1] += 1
            if students[i+1] == 0:
                students[i] -= 1
                students[i+1] += 1
    
    answer = n - students.count(0)
    return answer
'''
'''
# 성공코드 1
def solution(n, lost, reserve):
    for i in reserve:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)# 여유분이 있는 학생이 체육복을 잃어버렸을 경우의 중복을 제외
    answer = n - len(lost)# answer 에는 중복없이 전체 학생중에 체육복을 잃어 버리지 않은 학생수가 저장되있음
    for i in lost:
        if i in reserve:
            answer += 1
            reserve.remove(i)
        elif i-1 in reserve:# 남는 학생이 자기 앞사람에게
            answer += 1
            reserve.remove(i-1)
        elif i+1 in reserve:# 남는 학생이 자기 뒷사람에게
            answer += 1
            reserve.remove(i+1)
    return answer
'''
# 성공코드 2 set을 활용한 빠른 코드 
# lost set에 대해 모든 원소들에 +0, +1, -1 을 순차적으로 계산하고, 차집합으로 중복을 버리는것을 반복
def solution(n, lost, reserve):
    reserve = set(reserve)
    for size in [0, 1, -2]:
        lost = set(map(lambda x: x+size, lost))
        reserve, lost = reserve - lost, lost - reserve
    return n - len(lost)

n1 = 5
l1 = [2, 4]
r1 = [1, 3, 5]
n2 = 5
l2 = [2, 4]
r2 = [3]
n3 = 3
l3 = [3]
r3 = [1]
print(solution(n1, l1, r1))
print(solution(n2, l2, r2))
print(solution(n3, l3, r3))