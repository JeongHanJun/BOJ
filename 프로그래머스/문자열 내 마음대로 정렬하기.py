# 문자열 내 마음대로 정렬하기
# 제목부터 sorted, key, lambda 가 떠오른다.
def solution(strings, n):
    answer = sorted(strings, key = lambda x : (x[n], x))
    return answer

s1 = ["sun", "bed", "car"]
n1 = 1
s2 = ["abce", "abcd", "cdx"]
n2 = 2
print(solution(s1, n1))
print(solution(s2, n2))