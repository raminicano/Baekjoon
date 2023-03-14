
# 바구니 N개 왼쪽부터 1번
# begin mid end -> mid end begin

N, M = map(int, input().split()) # M개의 바구니 바꾸는 순서

li = [x+1 for x in range(N)]

# 순서 회전시키기
for _ in range(M):
    i, j, k = map(int, input().split()) # begin, end, mid
    i, j, k = i-1, j-1, k-1
    li = li[:i] + li[k:j+1] + li[i:k] + li[j+1:]

print(*li)