
# input
N, K = map(int, input().split())
li = []

for i in range(N // 2): # 약수니까 이정도 범위까지
    if N % (i+1) == 0: # 나누어 떨어진다면 약수임
        li.append(i+1)

# 자기자신은 디폴트로 추가해놓음
li.append(N)

if len(li) < K:
    print(0)
else:
    print(li[K-1])
