# 2163 초콜릿 자르기
'''
1x1 0
2x1 1   2x2 3   2x3 5   2x4 7   2x5 9
3x1 2   3x2 5   3x3 8

nxm 이면 n<=m 이라 할때 (m-1) + (n-1)Xm
'''
n, m = map(int, input().split())
print( (m-1) + (n-1)*m)