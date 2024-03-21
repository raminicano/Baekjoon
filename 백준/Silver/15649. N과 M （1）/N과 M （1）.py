def backtrack(N, M, result, visited):
    # 결과의 길이가 M일 때 출력
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    # 1부터 N까지의 자연수 중에서 선택
    for i in range(1, N + 1):
        # 이미 선택한 숫자인지 확인
        if not visited[i]:
            # 선택한 숫자를 결과에 추가하고 방문 표시
            result.append(i)
            visited[i] = True
            # 다음 단계로 진행
            backtrack(N, M, result, visited)
            # 백트래킹: 선택한 숫자를 다시 제거하고 방문 표시를 해제
            result.pop()
            visited[i] = False

# 입력 받기
N, M = map(int, input().split())

# 방문 여부를 저장하는 배열
visited = [False] * (N + 1)

# 백트래킹 함수 호출
backtrack(N, M, [], visited)
