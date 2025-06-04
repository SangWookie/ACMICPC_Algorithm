import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
table = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    for i in range(len(row)-1):
        row[i+1] += row[i]
    table.append(row)
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().strip().split())
    total = 0
    for i in range(x1 - 1, x2):
        subVal = 0
        if y1 != 1:
            subVal = table[i][y1 - 2]
        total += table[i][y2 - 1] - subVal
    print(total)

# for i in table:
#     for j in i:
#         print(j, end=" ")
#     print()