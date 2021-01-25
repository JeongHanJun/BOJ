# 2775 부녀회장이 될테야
'''
a층의 b호에 살려면 a-1층의 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다.
양의정수 k와 n이 입력
k층의 n호에는 몇명이 사는가
아파트는 0층부터 존재
0층의 i호에는 i명이 산다.

ex) k = 3, n - 3 - >  0층 1호에 1, 2호에 2, 3호에 3
                      1층 1호에 1, 2호에 3(1+2), 3호에 6(3+3)
                      2층 1호에 1, 2호에 4(1+3), 3호에 10(4+6)
                      3층 1호에 1, 2호에 5(1+4), 3호에 15(5+10)
            
            rule) Dynamic Programming,  k층, n호라고 할떄 apart[k, n] = apart[k, n-1] + apart[k-1, n]
'''

'''
t = int(input())
for a in range(t):
    k = int(input())# k층
    n = int(input())# n호
    apart = [ i for i in range(1, n+1) ]# 0층(1 ~ n)
    for b in range(k):# k층
        for j in range(1, n):
            apart[j] += apart[j-1]
    print(apart[-1])
'''

# 2차원 리스트를 쓰는 방법
t = int(input())
for a in range(t):
    k = int(input())# k층
    n = int(input())# n호
    apart = [ [0 for i in range(n)] for j in range(k+1)]# k+1인 이유는 0층부터 k층까지이므로, 즉 0층이 없다면 range(1, k+1)이 맞는것
    # 0으로 공간을 만들고 해당 칸들을 채워야한다. 이부분에서 2차원 리스트가 비효율적이다

    for b in range(1, n+1):# 0층부터 먼저 채우기
        apart[0][b-1] = b
    
    for f in range(1, k+1):# 1층부터 k층까지 층수 floor의 f
        for r in range(n):# 0호부터 n-1호까지rooms의 r
            if r == 0:
                apart[f][r] = 1
            else:
                apart[f][r] = apart[f][r-1] + apart[f-1][r]
        #print(apart)    
    print(apart[k][n-1])# 0층이 있는 k, 0칸이 없는 n


