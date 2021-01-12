# 셀프 넘버
'''
n -> n + n의 각 자릿수들의 합 = d(n)
이때 n을 d(n)의 생성자라고 한다.
! -> 1+1 = 2
2 -> 2 + 2 = 4
3 -> 3 + 3 = 6
4 -> 4 + 4 = 8
5 -> 5 + 5 = 10
셀프넘버는 생성자가 없는 숫자를 말한다.
ex) 1, 3, 5, 7, 9 와 같은 숫자들은 n과 n의 자릿수들의 합으로 표현할 수 없다.
1만보다 작거나 같은 셀프넘버를 모두 출력하는 프로그램을 작성하라
'''

'''
def d(n):
    dn = n
    while n > 0:
        dn += n % 10
        n /= 10
    return int(dn)

n_list = [True] * 10040
for i in range(1, 10001):
    n_list[d(i)] = False
for i in range(1, 10001):
    if n_list[i] == True:
        print(i)
# 이런식으로 함수를 통해 구현하면 출력 초과 발생하므로 함수를 쓰지 않고 푸는것이 더 좋음
'''

nums = [True] * 10040
for i in range(1, 101):
    temp = i
    while temp:
        i += temp % 10
        temp //= 10
    nums[i] = False
for i in range(1, 101):
    if nums[i]:
        print(i)

# 감명깊었던 좋은 코드
#print('\n'.join(map(str, sorted( {i for i in range(1, 10001) } - { i + i%10 + (i//10) % 10 + (i//100) % 10 + (i//1000) % 10 + (i//10000)%10 for i in range(1, 10001)} ))))


