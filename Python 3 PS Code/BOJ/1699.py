# 1699 제곱수의 합
'''
1   1
2   1 + 1
3   1 + 1 + 1
4   2
5   2 + 1
6   2 + 1 + 1
7   2 + 1 + 1 + 1
8   2 + 2
9   3
10  3 + 1
11  3 + 1 + 1       or      2 + 2 + 1 + 1 + 1

자연수 n을 제곱수의 합으로 표현할떄, 항의 최소값을 구하라
'''
'''
# 처음 짠 코드 , 실패    
# 이유 = 반례 43에서 5^2 + 3^2 + 3^2 으로 최소 3이 나와야 하는데 36에서 걸려져서 5가 나옴
n = int(input())
cnt = 0
for i in range(int(n**0.5)+1 , -1, -1):
    while True:
        if n - i*i >= 0:
            n -= i*i
            cnt += 1
        else:
            break
    if n == 0:
        break
print(cnt)
'''
# 아래부터는 성공코드
'''
# 성공코드, 시간 매우 오래걸림
n = int(input())
dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = i
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1
        print(dp)
print(dp[n])
'''
#   그러나 위에 채점하면서 느낀것이 너무 시간이 오래 걸려서
#   이게 맞나 싶어서 이 제곱수 합으로 표현되는것 관련해서 검색해보았다.
#   2가지가 나오는데, 라그랑주의 네 제곱수 정리와, 페르마의 두 제곱수 정리가 나온다.
'''
        < 라그랑주 의 4 제곱수 원리 >

        음 ... 어렵다






        < 페르마의 2 제곱수 원리 >
            소수 p 에 대해  p mod 4 = 1   <=(동치)=>   p = x^2 + y^2
                            이 부분에서 p = 2 인경우는 자명하므로 제외 ( 자명하다 = 굳이 증명 안해도 1^2 + 1^2 = 2 인것이 뻔하다)
            2   =   1   +   1
            5   =   2   +   1
            13  =   3   +   2
            17  =   4   +   1
            29  =   5   +   2
            37  =   6   +   1
            41  =   5   +   4
            53  =   7   +   2
            ...
            그러나 이것이 모든 소수에 대해 해당하는 것은 아니라는 문제가 있다.
'''
def solution(n):
    # n이 제곱수인 경우
    if int(n**0.5)**2 == n:
        return 1
    # 2개 제곱수의 합으로 표현되는 경우 = 페르마의 2제곱수 원리에 따라 이떄의 n = x^2 + y^2 이므로 x in sq_num  에 대해 n-x^2 = y^2 인것을 이용
    for s in sq_nums:
        if n < s:#
            break
        x = int((n-s)**0.5)**2
        if x == n-s:
            return 2
    # 3개 제곱수의 합으로 표현되는 경우 페르마의 2제곱수원리에 +a로, (x, y, z in sq_nums) n - x^2 = y^2 z^2 이면 <==> n = x^2 + y^2 + z^2 이므로 3개의 제곱수의 합으로 표현 가능하다.
    for s in sq_nums:
        if n < s:
            break
        for k in sq_nums:
            if n < s+k:
                break
            if int( (n-s-k)** 0.5 )**2 == n-s-k:
                return 3 
    # 이외의 경우 4개로 표현한다.
    return 4

n = int(input())
sq_nums = [ i*i for i in range(1, int(n**0.5)+1) ]
print(solution(n))