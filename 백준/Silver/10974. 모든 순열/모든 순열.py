N = int(input())
temp = []

def dfs():
    if len(temp) == N:
        print(*temp)
        return
    
    for i in range(1, N+1):
        if i not in temp:
            temp.append(i)
            dfs()
            temp.pop()

dfs()