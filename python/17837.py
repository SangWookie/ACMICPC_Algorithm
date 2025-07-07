import sys
input = sys.stdin.readline

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 각 칸에 말이 쌓여있는 상태 저장
chess = [[[] for _ in range(N)] for _ in range(N)]

# 방향: →, ←, ↑, ↓
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
reverse_dir = [1, 0, 3, 2]

# 말 정보: [x, y, dir]
pieces = []
for i in range(K):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1
    pieces.append([x, y, d])
    chess[x][y].append(i)

def move_piece(i):
    x, y, d = pieces[i]
    nx, ny = x + dx[d], y + dy[d]

    # 현재 말이 쌓여있는 위치에서 어디부터 위로 이동해야 하는지 찾기
    idx = chess[x][y].index(i)
    moving_stack = chess[x][y][idx:]
    chess[x][y] = chess[x][y][:idx]  # 나머지 남기기

    # 다음 위치가 벗어나거나 파란색인 경우 → 방향 반대로 바꿔서 재시도
    if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 2:
        d = reverse_dir[d]
        pieces[i][2] = d  # 방향 갱신
        nx, ny = x + dx[d], y + dy[d]
        if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 2:
            # 다시 파란색이거나 범위 밖이면 이동하지 않음
            chess[x][y].extend(moving_stack)
            return False

    # 이동 가능한 경우
    if board[nx][ny] == 1:  # 빨간색이면 뒤집어서 이동
        moving_stack.reverse()

    for pid in moving_stack:
        pieces[pid][0], pieces[pid][1] = nx, ny
    chess[nx][ny].extend(moving_stack)

    # 종료 조건: 말이 4개 이상 쌓이면 True
    return len(chess[nx][ny]) >= 4

turn = 1
while turn <= 1000:
    for i in range(K):
        if move_piece(i):
            print(turn)
            sys.exit(0)
    turn += 1

print(-1)
