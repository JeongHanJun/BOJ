# k번째수
def solution(array, commands):
    answer = []
    for line in commands:
        answer.append( sorted(array[ line[0]-1 : line[1]])[line[2]-1] )
    return answer
'''
a1 = [1, 5, 2, 6, 3, 7, 4]
c1 = [ [2, 5, 3], [4, 4, 1], [1, 7, 3] ]
print(solution(a1, c1))
'''