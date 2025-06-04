'''
dfs를 사용하여 문제 풀기
큐에다 넣는 조건을 잘 생각해서 넣어야 정확한 답을 구할 수 있음

사다리(뱀)가 있는 경우 무조건 타야하며 주사위는 사다리의 목적지부터
굴릴 수 있음.
'''

from collections import deque
n, m = map(int, input().split(" "))

ladder = {}
for i in range(n+m) :
    start, dest = map(int, input().split(" "))
    ladder[start] = dest

arr = [100] * 101

queue = deque()

queue.append((1, 0))

while queue:
    node = queue.popleft()
    location = node[0]
    count = node[1]
    if location > 100 or arr[location] <= count:
        continue
    
    arr[location] = count
    
    if location in ladder:
        queue.append((ladder[location], count))
    
    else:
        for i in range(1, 7, 1) :
            queue.append((location + i, count + 1))

print(arr[100])
