import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
cables = []

for _ in range(N):
    n = int(input())
    cables.append(n)
    
cables.sort()

leftPiv = 1
rightPiv = cables[N-1]
piv = 0
while leftPiv <= rightPiv:
    # print(rightPiv, leftPiv)
    piv = (leftPiv + rightPiv) // 2
    slices = 0
    for c in cables:
        slices += c//piv
    if slices < K:
        rightPiv = piv - 1
    elif slices > K:
        leftPiv = piv + 1
    else:
        leftPiv = piv + 1
    # print(slices)

print(rightPiv)