import sys
input = sys.stdin.readline

N = int(input().strip())
minVal = [10, 10, 10]
maxVal = [-1, -1, -1]
for i in range(N):
    a, b, c = map(int, input().strip().split())
    if i == 0:
        minVal = [a, b, c]
        maxVal = [a, b, c]
        continue
    prevMax = maxVal[:]
    prevMin = minVal[:]
    minVal[0] = min(prevMin[0], prevMin[1]) + a
    minVal[1] = min(prevMin[0], prevMin[1], prevMin[2]) + b
    minVal[2] = min(prevMin[1], prevMin[2]) + c
    
    maxVal[0] = max(prevMax[0],prevMax[1]) + a
    maxVal[1] = max(prevMax[0],prevMax[1],prevMax[2]) + b
    maxVal[2] = max(prevMax[1],prevMax[2]) + c

print(max(maxVal), min(minVal))