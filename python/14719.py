import sys
input = sys.stdin.readline

H, W = map(int, input().strip().split())
blocks = list(map(int, input().strip().split()))

waterCnt = 0
for i in range(1, H+1):
    wall = False
    tmpCnt = 0
    for j in range(W):
        if blocks[j] >= i:
            waterCnt += tmpCnt
            tmpCnt = 0
            wall = True
        elif blocks[j] < i and wall:
            tmpCnt += 1

print(waterCnt)