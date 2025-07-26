H, W, X, Y = map(int, input().split())

result = []
for _ in range(H + X):
    result.append(list(map(int, input().split())))
    
original = [[-1 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        # 좌상단, 우하단 코너 값들은 그대로 들고오기
        if i < X or j < Y:
            original[i][j] = result[i][j]
        elif i >= H-X or j >= W-Y:
            original[i][j] = result[i+X][j+Y]
        # 연산을 통해 기존값 복원
        else:
            original[i][j] = result[i][j] - original[i-X][j-Y]

for r in original:
    for n in r:
        print(n, end=" ")
    print()