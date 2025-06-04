from collections import defaultdict, deque
key = input().split(" ")
n = int(key[0])
m = int(key[1])
v = int(key[2])

graph = defaultdict(list)

for i in range(m) :
    line = input().split(" ")
    a = int(line[0])
    b = int(line[1])
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visited = [False] * (n + 1)

def dfs(start) :
    if(visited[start]) :
        return 0
    visited[start] = True
    print(start, end=" ")
    for i in graph[start] :
        if(visited[i] == False) :
            dfs(i)

dfs(v)
print()

visited = [False] * (n + 1)

def bfs(start) :
    queue = deque()
    queue.append(start)
    
    while queue :
        now = queue.popleft()
        if(visited[now]) :
            continue
        visited[now] = True
        print(now, end=" ")
        for i in graph[now] :
            if(visited[i] == False) :
                queue.append(i)
bfs(v)
