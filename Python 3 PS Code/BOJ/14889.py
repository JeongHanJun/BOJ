# 14889 스타트와 링크
from itertools import combinations #조합 함수

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
possible_team = []

#조합으로 가능한 팀 생성해주기
for team in list(combinations(members, N//2)):
    possible_team.append(team)

min_stat_gap = 10000 #갭이 가장 작은 값을 찾기 위하여
for i in range(len(possible_team)//2):
    #A 팀
    team = possible_team[i]
    stat_A = 0 #A팀 능력치
    for j in range(N//2):
        member = team[j] #멤버
        for k in team:
            stat_A += S[member][k] #멤버와 함께할 경우의 능력치들
            
    #A를 제외한 나머지 팀
    team = possible_team[-i-1]
    stat_B = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_B += S[member][k]
            
    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))
    
print(min_stat_gap)
'''
from itertools import combinations

N = int(input())
ability_board = []
for _ in range(N):
    ability_board.append(list(map(int, input().split())))

num_list = [i for i in range(N)]
res = float('inf')

def solve():
    global res
    
    # 조합을 이용하여 각 후보자를 생성함
    for cand in combinations(num_list, N // 2):
        # 선택된 후보와 나머지
        start_member = list(cand)
        link_member = list(set(num_list) - set(cand))
        
        # 점수 비교는 2명씩 이루어진다.
        start_comb = list(combinations(start_member, 2))
        link_comb = list(combinations(link_member, 2))
        
        # 점수 구하기
        start_sum = 0
        for x, y in start_comb:
            start_sum += (ability_board[x][y] + ability_board[y][x])
            
        link_sum = 0
        for x, y in link_comb:
            link_sum += (ability_board[x][y] + ability_board[y][x])
        
        # 차이를 구하는 것이므로 abs 사용
        if(res > abs(start_sum - link_sum)):
            res = abs(start_sum - link_sum)
            
solve()
print(res)
'''