import sys
input = sys.stdin.readline

a = str(input())
b = str(input())

counts = [[0] * (len(b)) for _ in range(len(a))]

maxVal = 0
for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i-1] == b[j-1] :
            counts[i][j] = max(counts[i-1][j-1] + 1, counts[i - 1][j])
        else :
            counts[i][j] = max(counts[i][j-1], counts[i-1][j])
        maxVal = max(maxVal, counts[i][j])

# for i in counts:
#     for j in i:
#         print(j, end=" ")
#     print()
print(maxVal)