from sys import stdin
n = int(stdin.readline())
for i in range(n):
    cnt = 0
    nums = list(map(int, stdin.readline().split()))
    avg = sum(nums[1:]) / nums[0]
    for j in nums[1:]:
        if j > avg:
            cnt += 1
    answer = cnt * 100 / nums[0]
    print("%.3f" % answer + "%")