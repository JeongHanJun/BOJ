# 1550 16진수
# 파이썬에서는 16진수 입력 받기 위해 앞에 0x 를 붙인다. 8진수는 0o를 붙인다.
# int함수에서 1번째인자로 2, 8, 16진수를 문자열타입으로 넣고, 뒤에 이에 맞게 2, 8, 16을 넣어서 출력하면 정수형으로 변환이 된다.
n = '0x'+input()
print(int(n, 16))

'''
# 위와 같은 코드
#print(int(input(), 16))
'''