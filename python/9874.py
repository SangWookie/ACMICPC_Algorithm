import sys
from collections import defaultdict
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
holes = []
for _ in range(N):
    x, y = map(int, input().split())
    holes.append((x,y))

# 가능한 웜홀 쌍 경우의 수 모두 도출
wormhole = []
selected = [False for _ in range(N)]
pairSet = defaultdict()
def backtrack():
    # 사용 가능한 웜홀 찾기
    first = -1
    for i in range(N):
        if not selected[i]:
            selected[i] = True
            first = i
            break
    if first == -1:
        pairSetCopy = deepcopy(pairSet)
        wormhole.append(pairSetCopy)
        return
    
    # 목적지 웜홀 찾기
    for j in range(N):
        if selected[j]:
            continue
        selected[j] = True
        pairSet[first] = j
        pairSet[j] = first
        
        # 다음 웜홀쌍 찾기
        backtrack()
        
        # 원래대로 복구시키기
        selected[j] = False
        pairSet.pop(first)
        pairSet.pop(j)
    selected[first] = False

# 가능한 웜홀쌍 경우의 수 모두 구함
backtrack()

# 각 웜홀쌍 경우에서 무한 루프가 일어나는지 확인
cnt = 0
for dict in wormhole:
    isLoop = False
    # 처음 나오는 웜홀을 바꿔가며 확인
    for i in range(N):
        visited = [False for _ in range(N)]
        holeNow = i
        for j in range(N):
            if visited[holeNow]:
                isLoop = True
                break
            visited[holeNow] = True
            
            # 다음 웜홀이 어딘지 찾기
            nextHole = -1
            diff = 1_000_000_000
            for k in range(N):
                if holeNow != k \
                and holes[holeNow][1] == holes[k][1]\
                and 0 < holes[k][0] - holes[holeNow][0] < diff:
                    diff = holes[k][0] - holes[holeNow][0]
                    nextHole = k
            # 다음으로 들어갈 웜홀이 없으면
            if nextHole == -1:
                break

            holeNow = dict[nextHole]
    if isLoop:
        cnt += 1
        
print(cnt)