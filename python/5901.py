import sys
from collections import defaultdict
import heapq
from itertools import permutations

input = sys.stdin.readline

N, M, K = map(int, input().split())

# 시장인지 판별하기 위한 변수
markets = []
for i in range(K):
    marketNode = int(input())
    markets.append(marketNode)

# map 구축
roads = defaultdict(list)
for _ in range(M):
    st, ed, L = map(int, input().split())
    roads[st].append((ed, L))
    roads[ed].append((st, L))

fromMarket = defaultdict(list)
def dijkstra(st):
    dists = [10_000_000_000 for _ in range(N+1)]
    queue = []
    dists[st] = 0
    for nextRoad in roads[st]:
        heapq.heappush(queue, (nextRoad[1], nextRoad[0]))
    
    while queue:
        dist, nextNode = heapq.heappop(queue)
        if dists[nextNode] < dist :
            continue
        dists[nextNode] = dist
        for (ed, L) in roads[nextNode]:
            if dist + L < dists[ed]:
                heapq.heappush(queue, (dist+L, ed))
    fromMarket[st] = dists
    
# 시장 노드들에서 각 노드들까지의 거리
for market in markets:
    dijkstra(market)
    
# permutation으로 각 순서쌍 조회, 최솟값 탐색
minTotal = 10_000_000_000
for marketOrder in permutations(markets):
    total = 0
    # market 내부 거리 총합
    for i in range(len(marketOrder) - 1):
        st = marketOrder[i]
        ed = marketOrder[i+1]
        total += fromMarket[st][ed]
    
    for i in range(1, N + 1):
        if i in markets:
            continue
        thisTotal = total
        # 첫 번째 market과 시작점과의 거리
        first = marketOrder[0]
        thisTotal += fromMarket[first][i]
        
        # 마지막 market과 시작점과의 거리
        last = marketOrder[-1]
        thisTotal += fromMarket[last][i]
        minTotal = min(minTotal, thisTotal)

print(minTotal)