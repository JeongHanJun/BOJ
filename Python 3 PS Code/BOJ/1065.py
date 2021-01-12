# 한수 
# 각 자리의 숫자가 등차수열
# 100 미만의 수들은 자동적으로 한수 99
# 100 이상의 경우 111, 123, 135, 147, 159, 210 등
'''
def hansu(n):
    cnt = 99
    if n < 100:
        return n
    elif n >= 999:
        return 144
    else:
        for i in range(100, n+1):
            nums = list(map(int, str(i)))
            if nums[2] - nums[1] == nums[1] - nums[0]:
                cnt += 1
            else:
                pass
        return(cnt)
from sys import stdin
n = int(stdin.readline())
print(hansu(n))
'''
# 한줄 간략 코드
print( sum( i < 100 or i // 10 % 10 * 2 == i % 10  + i // 100 for i in range(1, int(input())+1 ) ) )
# 나머지, 곱셉, 나누기 연산자 우선순위는 동일하므로
# i // 10 = (백의자릿수)(십의자릿수) -> i // 10 % 10 * 2 = 십의자릿수 * 2
# i % 10 = 1의자릿수, 1의자릿수 + 100의자릿수
# 등차수열의 경우 a, a+n, a+2n 이므로 a + a+2n = 2(a+n)인 점을 이용한 기가막힌 코드
# 단, 시공간복잡도는 위 함수를 사용한 코드와 거의 차이나지 않음