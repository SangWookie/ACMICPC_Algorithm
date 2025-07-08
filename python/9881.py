# min max 값을 구한 뒤 
# sliding window처럼 범위 값 바꿔가면서 최솟값 찾기

import sys
input = sys.stdin.readline

N = int(input())
hills = []
minVal = 1000
maxVal = 0
for _ in range(N):
    hill = int(input())
    minVal = min(minVal, hill)
    maxVal = max(maxVal, hill)
    hills.append(hill)

minCost = 1_000_000_000
if maxVal - minVal < 18:
    print("0")
else:
    # sliding window
    for i in range(minVal, maxVal-(minVal+17) + 1):
        thisCost = 0
        thisMin = i         # 이번 윈도우의 최솟값
        thisMax = i + 17    # 이번 윈도우의 최댓값
        for hill in hills:
            if thisMin <= hill <= thisMax:
                continue
            elif hill < thisMin:
                thisCost += (thisMin-hill)**2
            elif hill > thisMax:
                thisCost += (hill-thisMax)**2
        minCost = min(thisCost, minCost)    # 이번 윈도우 경우 cost값 업데이트
    print(minCost)