import sys
from collections import defaultdict
input = sys.stdin.readline

N, Q = map(int, input().split())

mooMap = defaultdict(lambda: defaultdict(int))
for _ in range(N-1) :
    src, dest, w = map(int, input().split())
    mooMap[src][dest] = w
    mooMap[dest][src] = w

visited = [0]

def dfs_iterative(k, start):
    stack = [(start, 1000000000)]
    visited = [0] * (N + 1)
    visited[start] = 1
    count = 0

    while stack:
        node, minVal = stack.pop()
        for neighbor, weight in mooMap[node].items():
            if not visited[neighbor]:
                newMin = min(minVal, weight)
                if newMin >= k:
                    count += 1
                    stack.append((neighbor, newMin))
                visited[neighbor] = 1
    return count

for _ in range(Q):
    k, v = map(int, input().split())
    print(dfs_iterative(k, v))
