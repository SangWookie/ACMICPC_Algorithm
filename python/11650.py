import sys
input = sys.stdin.readline

N = int(input())
node = []
for _ in range(N):
    (a, b) = map(int, input().split())
    node.append((a,b))
node.sort()
for (a, b) in node:
    print(a, b)