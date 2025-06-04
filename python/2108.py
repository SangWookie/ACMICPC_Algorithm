import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())

nums = []
pres = defaultdict()
total = 0
for i in range(N):
    n = int(input())
    if n not in pres:
        pres[n] = 1
    else:
        pres[n] += 1
    total += n
    nums.append(n)
    
nums.sort()
# print(nums)
freqVal = max(pres.values())
freqNum = 0
for n in nums:
    if pres[n] == freqVal:
        if freqNum != 0 and freqNum != n:
            freqNum = n
            break
        else:
            freqNum = n

    
print(int(round(total/N, 0)))
print(nums[N//2])
print(freqNum)
print(nums[-1] - nums[0])