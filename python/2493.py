import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().strip().split()))

ans = [0] * N
stack = []
for i in range(N-1, -1, -1):
    if stack and stack[-1][0] < towers[i]:
        while stack and stack[-1][0] < towers[i]:
            height, ind = stack.pop()
            ans[ind] = i+1
    stack.append((towers[i], i))

for i in ans:
    print(i, end=" ")