import sys
inputs = sys.stdin.readline
N = int(inputs().strip())
ball = str(inputs().strip())

cnt = []
explore = ball.rstrip('R')
cnt.append(explore.count('R'))
explore = ball.rstrip('B')
cnt.append(explore.count('B'))
explore = ball.lstrip('R')
cnt.append(explore.count('R'))
explore = ball.lstrip('B')
cnt.append(explore.count('B'))

print(min(cnt))