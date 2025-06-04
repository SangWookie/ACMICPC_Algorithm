import sys
from collections import defaultdict
input = sys.stdin.readline
N, D = map(int, input().strip().split())

road = []
for i in range(N):
    st, ed, length = map(int, input().strip().split())
    road.append((st, ed, length))

road.sort()

distance = defaultdict()
distance[D] = D

for st, ed, length in road:
    if st not in distance:
        distance[st] = st
    if ed not in distance:
        distance[ed] = ed
    
    for key, value in distance.items():
        if key > st:
            continue
        if distance[key] + (st-key) < distance[st]:
            distance[st] = distance[key] + (st-key)
            
    if distance[st] + length < distance[ed]:
        distance[ed] = distance[st] + length

for ed, length in distance.items():
    if ed > D:
        continue
    if distance[ed] + (D - ed) < distance[D]:
        distance[D] = distance[ed] + (D - ed)

print(distance[D])