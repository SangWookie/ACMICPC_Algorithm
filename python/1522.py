# 슬라이딩 윈도우
import sys
input = sys.stdin.readline()
string = str(input.strip())
# 원래 입력 길이
length = len(string)

# a의 개수를 윈도우의 크기로 잡는다
aCnt = string.count('a')

# 원형 문자열을 처리하기 위함
string += string

minVal = 10000
for i in range(length):
    cnt = string[i : i + aCnt].count('b')
    if cnt < minVal:
        minVal = cnt

print(minVal)