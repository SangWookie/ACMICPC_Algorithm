import sys
input = sys.stdin.readline

# 방향: 1:→, 2:←, 3:↑, 4:↓ (1-based)
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
reverse_dir = [0, 2, 1, 4, 3]

class Piece:
    def __init__(self, x: int, y: int, d: int):
        self.x = x
        self.y = y
        self.d = d

N, K = map(int, input().split())
board = [[0] * (N+1)]
for _ in range(N):
    board.append([0] + list(map(int, input().split())))

pieces = [None]  # 1-based index, pieces[1] ~ pieces[K]
cell = [[[] for _ in range(N+1)] for _ in range(N+1)]  # 1-based

for i in range(1, K+1):
    x, y, d = map(int, input().split())
    pieces.append(Piece(x, y, d))
    cell[x][y].append(i)

def move():
    for idx in range(1, K+1):
        piece = pieces[idx]
        x, y, d = piece.x, piece.y, piece.d
        stack = cell[x][y]
        # 가장 아래에 있는 말만 이동
        if stack[0] != idx:
            continue
        h = stack.index(idx)
        moving = stack[h:]
        cell[x][y] = stack[:h]

        nx = x + dx[d]
        ny = y + dy[d]

        # 범위 밖이거나 파란색
        if not (1 <= nx <= N and 1 <= ny <= N) or board[nx][ny] == 2:
            nd = reverse_dir[d]
            pieces[idx].d = nd
            nx = x + dx[nd]
            ny = y + dy[nd]
            if not (1 <= nx <= N and 1 <= ny <= N) or board[nx][ny] == 2:
                cell[x][y].extend(moving)
                continue
            d = nd
            pieces[idx].d = d  # 방향 갱신

        # 이동한 칸의 색에 따라 처리
        if board[nx][ny] == 0:
            cell[nx][ny].extend(moving)
            for m in moving:
                pieces[m].x = nx
                pieces[m].y = ny
        elif board[nx][ny] == 1:
            rev_moving = list(reversed(moving))
            cell[nx][ny].extend(rev_moving)
            for m in rev_moving:
                pieces[m].x = nx
                pieces[m].y = ny

        if len(cell[nx][ny]) >= 4:
            return True
    return False

turn = 0
while turn <= 1000:
    turn += 1
    if move():
        print(turn)
        break
else:
    print(-1)