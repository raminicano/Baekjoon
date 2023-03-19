
N, M = map(int, input().split())    # N개의 줄, M개의 원소

# 첫번째 리스트
first = []
for i in range(N):
    row = list(map(int, input().split()))   # M개의 원소를 받기
    first.append(row)


# 두번째 리스트
second = []
for i in range(N):
    row = list(map(int, input().split()))   # M개의 원소를 받기
    second.append(row)

    
for i in range(N):
    for j in range(M):
        print(first[i][j] + second[i][j], end=' ') # 스페이스 공백 주기
    # 한줄 출력이 끝나면 줄 바꿈
    print()
