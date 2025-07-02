import copy
N = int(input())

# 초기 경우의 수(1~9까지 가능)
arr = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for _ in range(N-1):
    orig = copy.deepcopy(arr)
    for i in range(10):
        thisSum = 0
        if i >= 1:
            thisSum += orig[i - 1]
        if i <= 8:
            thisSum += orig[i + 1]
        arr[i] = thisSum %1_000_000_000

print(sum(arr)%1_000_000_000)