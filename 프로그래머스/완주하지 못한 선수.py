# 완주하지 못한 선수
# 효율성 검사 탈락 코드
"""
def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
    return participant[0]
"""
# 성공 코드 1. collections 의 Counter를 이용
'''
from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer)[0]
'''
# 성공 코드 2. zip으로 비교하면서 다른게 있으면 바로출력, 비교 다해도 없으면 마지막것이 다른것
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for a, b in zip(participant, completion):
        if a != b:
            return a
    return participant[-1]



'''
p1 = ["leo", "kiki", "eden"]
p2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
p3 = ["mislav", "stanko", "mislav", "ana"]

c1 = ["eden", "kiki"]
c2 = ["josipa", "filipa", "marina", "nikola"]
c3 = ["stanko", "ana", "mislav"]

print(solution(p1, c1))
print(solution(p2, c2))
print(solution(p3, c3))
