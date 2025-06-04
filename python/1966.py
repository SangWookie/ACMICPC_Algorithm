import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    N, M = map(int, input().strip().split())
    
    nums = list(map(int, input().strip().split()))
    q = []
    for i in range(N):
        q.append((nums[i], i))
    q = deque(q)

    rank = 0
    while True:
        num, ind = q.popleft()
        if q and max(q, key=lambda x: x[0])[0] > num:
            q.append((num, ind))
            continue
        else :
            rank += 1
        if ind == M:
            print(rank)
            break
