from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
n, m = map(int, input().split(" "))

graph = defaultdict(list)
pq = []
dist = [10000000000000000] * (n+1)
dist[1] = 0
    
for i in range(m) :
    start, end, weight = map(int, input().split(" "))
    
    graph[start].append((end, weight))
    graph[end].append((start, weight))

heapq.heappush(pq, (0, 1))
while pq:
    weight, node = heapq.heappop(pq)
    
    if weight > dist[node]:
        continue
    
    for inode, iweight in graph[node]:
        if dist[inode] > iweight+weight:
            dist[inode] = weight+iweight
            heapq.heappush(pq, (iweight+weight, inode))

print(dist[n])