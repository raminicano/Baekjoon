N, M = map(int, input().split(" "))

# N은 수열의 값
# M은 수열의 개수
tu = []

def backtrack(N, M, result, visited):
    if len(result) == M:
        # visited 리스트가 tud에 있다면 이미 갔던 경로의 조합이니까 return
        if visited in tu:
            return
        # 아직 못간던 경로의 조합이므로 tu리스트에 추가함
        tu.append(visited[:])
        print(' '.join(map(str, result)))
        # temp = [result[0], result[1]]
        # tu.append(temp)
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            result.append(i)
            visited[i] = True
            backtrack(N, M, result, visited)
            result.pop()
            visited[i] = False
        
visited = [False] * (N+1)

backtrack(N, M, [], visited)
