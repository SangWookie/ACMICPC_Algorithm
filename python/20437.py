import sys
from collections import defaultdict

t = int(sys.stdin.readline())


for _ in range(t):
    
    w = sys.stdin.readline()
    k = int(sys.stdin.readline())
    dic = defaultdict(list)
    i = 0
    for c in w:
        dic[c].append(i)
        i+=1

    # print(dic)
    short = 100000
    long = 0
    for key, val in dic.items():
        # val.sort()
        if len(val) < k :
            continue
        for i in range(0, len(val) - k + 1, 1) :
            if short > val[i+k-1] - val[i] + 1 :
                short = val[i+k-1] - val[i] + 1
            if long < val[i+k-1] - val[i] + 1 :
                long = val[i+k-1] - val[i] + 1
    if short == 100000 or long == 0:
        sys.stdout.write(f"-1\n")
    else:
        sys.stdout.write(f"{short} {long}\n")