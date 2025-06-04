t = int(input())

arr = [1] * 10001

for i in range(2, 10001):
    arr[i] += arr[i-2]

for i in range(3, 10001):
    arr[i] += arr[i-3]


for i in range(t) :
    n = int(input())
    
    print(arr[n])
        