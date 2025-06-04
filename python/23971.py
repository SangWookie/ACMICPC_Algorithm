keyboard = input().split(" ")
h = int(keyboard[0])
w = int(keyboard[1])
n = int(keyboard[2])
m = int(keyboard[3])

col = h // (n + 1)
if(h % (n + 1) != 0):
    col += 1
    
row = w // (m + 1)
if(w % (m + 1) != 0):
    row += 1
    
print(col * row)