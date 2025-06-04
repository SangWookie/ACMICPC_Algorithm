import sys
from collections import deque
import heapq
input = sys.stdin.readline

n, m = map(int, input().strip().split())

inputMap = []
for _ in range(n):
    l = list(map(int, input().strip().split()))
    inputMap.append(l)
    
# find 2
destI, destJ = 0, 0
for i in range(n):
    for j in range(m):
        if inputMap[i][j] == 2:
            destI = i
            destJ = j
            
# create map for answer
outputMap = [[10000 for _ in range(m)] for _ in range(n)]
q = []
heapq.heappush(q, (0, destI, destJ))
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while q:
    cnt, i, j= heapq.heappop(q)
    # print(i, j, cnt)
    if outputMap[i][j] <= cnt:
        continue
    if cnt < outputMap[i][j]:
        outputMap[i][j] = cnt
    for di, dj in directions:
        nextI = di + i
        nextJ = dj + j
        if (nextI >= 0 and nextI <= n-1 
            and nextJ >= 0 and nextJ <= m-1 
            and outputMap[nextI][nextJ] > cnt + 1
            and inputMap[nextI][nextJ] != 0):
            heapq.heappush(q, (cnt+1, nextI, nextJ))

for i in range(n):
    for j in range(m):
        if outputMap[i][j] == 10000:
            if inputMap[i][j] == 0:
                outputMap[i][j] = 0
            else:
                outputMap[i][j] = -1
        print(outputMap[i][j], end=" ")
    print()