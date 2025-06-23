import sys
from collections import defaultdict
input = sys.stdin.readline

N, C = map(int, input().split())

coordinates = []
for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

edges = []
# 먼저 네트워크 구축
for i in range(N):
    xi, yi = coordinates[i]
    for j in range(i+1, N):
        xj, yj = coordinates[j]
        dist = (xi - xj) ** 2 + (yi - yj) ** 2
        if dist >= C:
            edges.append((dist, i, j))

# kruskal 알고리즘
parent = defaultdict()
for i in range(N):
    parent[i] = i

def find(i):
    if i != parent[i]:
        parent[i] = find(parent[i])
    return parent[i]

def union(i, j):
    rootI = find(i)
    rootJ = find(j)
    if rootI != rootJ:
        parent[rootJ] = rootI
        return True
    return False
    
edges.sort()
totalCost = 0
nodes = set()
for d, i, j in edges:
    if union(i, j):
        totalCost += d
        nodes.add(i)
        nodes.add(j)
        if len(nodes) == N:
            break

if len(nodes) != N:
    print("-1")
else:
    print(totalCost)