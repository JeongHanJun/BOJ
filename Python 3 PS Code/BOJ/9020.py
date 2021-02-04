# 골드바흐의 추측
'''
골드바흐의 추측이란,
2보다 큰 모든 짝수는 두개의 소수의 합으로 표현할 수 있다.
ex ) 4 = 2+2
     6 = 3+3
     8 = 3+5
     10= 5+5
     12= 5+7
     14= 7+7   or 3+11
testcase의 수 t번에 대해 주어진 n에 대해 골드바흐 파티션출력, 14처럼 여러개일시, 소수의 차이가 적은 것을 출력

'''
# 1번 풀이, n이 1만 이하이므로 이에 해당하는 소수리스트를 만든후, 골드바흐 파티션을 출력
'''
def get_prime_numbers(n):
    if n < 2:
        return []
    else:
        n += 1
        save = [True] * (n//2)
        for i in range(3, int(n**0.5)+1, 2):
            k = i*i
            if save[i//2]:
                save[k//2::i] = [False] * ( (n-k-1) // (2*i)+1 )
    return [2] + [ (2*i+1) for i in range(1, n//2 ) if save[i] ]

prime_numbers = get_prime_numbers(10000)
t = int(input())
for _ in range(t):
    n = int(input())
    if n//2 in prime_numbers:# 제곱수인경우, 같은소수2개로 분해되는경우
        print(n//2, n//2)
    else:
        gap = []
        i_list = []
        for i in range(n//2, 1, -1):
            #if n - prime_numbers[i] in prime_numbers:
                 #print(prime_numbers[i], n-prime_numbers[i])
                 #break
                if i not in prime_numbers:
                     continue
                else:
                    if n-i in prime_numbers:
                        print(i, n-i)
                        break
'''
# 1만개까지의 소수 리스트를 만들지 않고, 주어진 input중 최댓값만큼 만드는 방법, 그러나 이 방법은 stdin.read()를 사용해서 입력의 끝에 ctrl+z를 붙여야 테스트가 가능, 암튼 이게 1번풀이보다 시간은 빠름

from sys import stdin
def get_prime_numbers(n):
    if n < 2:
        return []
    else:
        n += 1
        save = [True] * (n//2)
        for i in range(3, int(n**0.5)+1, 2):
            k = i*i
            if save[i//2]:
                save[k//2::i] = [False] * ( (n-k-1) // (2*i)+1 )
    return [2] + [ (2*i+1) for i in range(1, n//2 ) if save[i] ]
inputs = list(map(int, stdin.read().split()))
max_num = max(inputs)
prime_numbers = get_prime_numbers(max_num+1)
for a in range(inputs[0]):
    n = inputs[a+1]
    if n//2 in prime_numbers:
        print(n//2, n//2)
    else:
        gap = []
        i_list = []
        for i in range(n//2, 1, -1):
                if i not in prime_numbers:
                     continue
                else:
                    if n-i in prime_numbers:
                        print(i, n-i)
                        break
