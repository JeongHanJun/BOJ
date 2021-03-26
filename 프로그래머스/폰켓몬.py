# 폰켓몬

'''
def solution(nums):
    temp = []
    l = len(nums)
    for i in nums:
        if i not in temp:
            temp.append(i)
        if len(temp) == l//2:
            break
    print(temp)
    return len(temp)
'''
# 감명깊은 한줄풀이
# nums 리스트를 set으로 하면, 중복이 제거되므로, 중복이 제거된 상태의 nums 리스트가 된다, 이것과 nums리스트의 길이의 반 둘중에 최소값이 답이 된다.
def solution(nums):
    return min( len(nums)//2 , len(set(nums)))

'''
n1 = [3, 1, 2, 3]#              2
n2 = [3, 3, 3, 2, 2, 4]#        3
n3 = [3, 3, 3, 2, 2, 2, ]#      2
print(solution(n1))
print(solution(n2))
print(solution(n3))
'''