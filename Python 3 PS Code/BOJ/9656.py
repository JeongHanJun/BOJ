# 9656 돌 게임 2
''' 상근이가 먼저시작
n                                       상근 결과
1       1                                    패
2       1       1                           승
3       3-0     1-1-1                       패
4       3-1     1-1-1-1                     승
5       3-1-1   1-1-1-1-1                   패
6       3-3     3-1-1-1     1-1-1-1-1-1     승
7       3-1-1-1-1   3-3-1   1-1-1-1-1-1-1   패
'''
# 성공코드 1. 
'''
n = int(input())
if n % 2:
    print('CY')
else:
    print('SK')
'''
# 성공코드 2. 한줄코드
print( 'CY' if int(input())%2  else 'SK' )