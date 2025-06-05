import sys
input = sys.stdin.readline

n = int(input())
costs = []
for _ in range(n):
    thisCost = list(map(int, input().split()))
    costs.append(thisCost)

for i in range(1, len(costs)):
    costs[i][0] += min(costs[i-1][1], costs[i-1][2])
    costs[i][1] += min(costs[i-1][0], costs[i-1][2])
    costs[i][2] += min(costs[i-1][0], costs[i-1][1])

print(min(costs[n-1]))