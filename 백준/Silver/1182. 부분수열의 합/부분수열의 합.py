N, S = map(int, input().split(" "))
li =  list(map(int, input().split(" ")))

# 부분수열의 개수
cnt = 0
# 부분수열 리스트
ans = []

def solve(start):
    global cnt
    # 리스트가 합쳐서 S가 된다면 그리고 원소가 0개보다 크면
    if sum(ans) == S and len(ans) > 0:
        # 부분수열의 개수를 더한다
        cnt += 1

    # 0부터 N까지의 원소를 돈다.
    for i in range(start, N):
        ans.append(li[i])
        solve(i+1)
        ans.pop()

solve(0)
print(cnt)