n = int(input())
count = 0

cols = [0] * n
d1 = [0] * (2 * n - 1)  # row + col
d2 = [0] * (2 * n - 1)  # row - col + (n - 1)

def dfs(row):
    global count
    if row == n:
        count += 1
        return
    for col in range(n):
        if not cols[col] and not d1[row + col] and not d2[row - col + n - 1]:
            cols[col] = d1[row + col] = d2[row - col + n - 1] = 1
            dfs(row + 1)
            cols[col] = d1[row + col] = d2[row - col + n - 1] = 0

dfs(0)
print(count)
