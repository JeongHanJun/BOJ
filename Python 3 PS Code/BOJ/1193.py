# 1193 분수찾기
'''
1   1/1
2   1/2
3   2/1
4   3/1
5   2/2
6   1/3
x번째 분수를 구해라
분모 + 분자의 합 -> 2   3    4   5   6 ...
                   1   
시작점             1    2   4   7   11  16
                     1    2   3   4    5   -> 시작점 = (n*n +n)/2 + 1
끝점               1    3   6   10  15  21  
                     2    3   4   5   6    -> 끝점 = (n*n + 3n)/2 + 1
i line
0 1
1 3
2 4
3 5

'''
n = int(input())
for i in range(n):
    e = (i*i + 3*i)/2 + 1
    #if n == 1:
    #    print('1'+'/'+'1')
    #    break
    if n > e:
        continue
    else:
        s = (i*i + i)/2 + 1
        if i % 2 == 0:
            print(str(int(e-n+1))+'/'+str(int(n-s+1)))
            break
        else:
            print(str(int(n-s+1))+'/'+str(int(e-n+1)))
            #print(str(int(e-n+1))+'/'+str(int(n-s+1)))
            # 위의 코드는 지그재그긴 한데 문제 로직과 다른 지그재그
            break