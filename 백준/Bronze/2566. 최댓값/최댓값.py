data = 0
col = 0
row = 0

li = []

for i in range(9):
    li.append(list(map(int, input().split())))


for i in range(9):
    for j in range(9):
        if li[i][j] > data:
            data = li[i][j]
            col = j
            row = i
        
print(data)
print(row+1, col+1)