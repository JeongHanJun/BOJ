''' 

< n = 3 > 3x3 board
***
* *                 # 당연하게 이 부분은 1,1 즉 x와 y를 나눈 나머지가 1
***
< n = 9 > 9x9 board
*********
* ** ** *           # 당연하게 이 부분은 1,1 즉 x와 y를 나눈 나머지가 1
*********
***   ***           # 여기랑
* *   * *           # 여기랑
***   ***           # 여기를 가진 큰 정사각형 이 부분이 힘들었는데 x를 3으로 나눈 몫 = y를 3으로나눈 몫 = 1 
*********
* ** ** *           # 당연하게 이 부분은 1,1 즉 x와 y를 나눈 나머지가 1
*********
        < n = 27 >  27x27 board 
***************************
* ** ** ** ** ** ** ** ** *     # 당연하게 이 부분은 1,1 즉 x와 y를 나눈 나머지가 1
***************************
***   ******   ******   ***
* *   * ** *   * ** *   * *     # 여기도 3으로 나눈 몫이 1 
***   ******   ******   ***
***************************
* ** ** ** ** ** ** ** ** *
***************************
*********         *********
* ** ** *         * ** ** *
*********         *********
***   ***         ***   ***
* *   * *         * *   * *
***   ***         ***   ***
*********         *********
* ** ** *         * ** ** *
*********         *********
***************************
* ** ** ** ** ** ** ** ** *
***************************
***   ******   ******   ***
* *   * ** *   * ** *   * *
***   ******   ******   ***
***************************
* ** ** ** ** ** ** ** ** *
***************************
'''
# 시간초과 코드
'''
ans = []
n = int(input())
for y in range(n):
    for x in range(n):
        flag = True
        temp_y = y
        temp_x = x
        while temp_y != 0:
            if temp_y % 3 == 1 and temp_x % 3 == 1:
                flag = False
                ans.append(' ')
                break
            temp_x = temp_x//3
            temp_y = temp_y//3
        if flag:
            ans.append('*')
    ans.append('\n')
result = ''.join(ans)
print(result)
'''
# gap 이라는 이 문제의 특징상 3배로 늘어나는 점을 이용한 코드
'''
def star(x, y, n):
    if n == 1:
        board[x][y] = '*'
        return
    gap = n//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            star(x+gap*i, y+gap*j, gap)

n = int(input())
board = [ [' ' for i in range(n)] for j in range(n) ]
star(0, 0, n)
for i in range(n):
    print(''.join(board[i]))
'''
# 빠른 코드
def merge(a, b):
    return [ ''.join(x) for x in zip(a, b, a) ]

def star(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star(n)
    x1 = merge(x, x)
    x2 = merge(x, [' '*n]*n)
    return x1 + x2 + x1

print('\n'.join(star(int(input()))))
