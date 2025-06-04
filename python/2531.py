import sys
inputs = sys.stdin.readline
N, d, k, c = map(int, inputs().split(" "))

arr = []
for i in range(N):
    arr.append(int(inputs()))
    
arr.extend(arr[:])

maximum = 0
for i in range(N):
    thisWind = arr[i : i+k]
    distinct = len(set(thisWind))
    if c not in thisWind:
        distinct += 1
    maximum = max(distinct, maximum)
    
print(maximum)