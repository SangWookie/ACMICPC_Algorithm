import itertools
n = int(input())

a = []

for i in range(n):
    x = int(input())
    a.append(x)
a.sort()

cnt = 0

for i in range(0, n-2):
    for j in range(i+1, n-1) :
        count = 0
        for k in range(j+1, n):
            if(a[i] + a[j] > a[k]):
                count += 1
        cnt += 2**count -1

print(cnt)