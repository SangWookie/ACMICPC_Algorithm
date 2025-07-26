R, C, N = map(int, input().split())

bombMap = []
for i in range(R):
    row = input()
    bombMap.append(row)

def makeFullMap():
    """폭탄으로 가득 찬 맵 생성"""
    fullMap = []
    for i in range(R):
        fullMap.append('O'*C)
    return fullMap

bombRange = [(-1, 0), (0, -1), (1, 0), (0, 1), (0, 0)]
def makeReverseMap(bombMap):
    """폭탄이 터진 이후 만들어지는 맵
    Args:
        bombMap (list): 폭탄 터지기 이전 맵
    Returns:
        list: 폭탄 터지고 나서 맵
    """
    reversedMap = []
    for i in range(R):
        row = ""
        for j in range(C):
            flag = False
            for (dx, dy) in bombRange:
                if 0 <= i + dx < R and 0 <= j + dy < C and \
                    bombMap[i + dx][j + dy] == 'O':
                    flag = True
            if flag:
                row += "."
            else:
                row += "O"
        reversedMap.append(row)
    return reversedMap

if N == 1:
    result = bombMap
elif N % 2 == 0:
    result = makeFullMap()
elif N % 4 == 3:
    result = makeReverseMap(bombMap)
elif N % 4 == 1:
    result = makeReverseMap(makeReverseMap(bombMap))

for row in result:
    print(row)