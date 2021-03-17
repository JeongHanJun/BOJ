# 6603 로또
from itertools import combinations
while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break
    
    t = line[0]
    line = line[1:]
    c = combinations(line, 6)
    for i in c:
        print(*i)
    print()