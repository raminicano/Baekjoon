def solution(prices):
    n = len(prices)
    answer = [0] * n  # 결과를 저장할 리스트 (가격이 떨어지지 않은 기간)
    stack = []  # 스택에 (가격의 인덱스)를 저장
    
    for i in range(n):
        # 스택에 있는 가격보다 현재 가격이 낮으면 떨어진 기간 계산
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()  # 스택에서 인덱스 꺼냄
            answer[idx] = i - idx  # 현재 시점에서 떨어졌으므로 기간 계산
        stack.append(i)  # 현재 인덱스를 스택에 추가
    
    # 스택에 남아있는 인덱스는 끝까지 가격이 떨어지지 않은 경우
    while stack:
        idx = stack.pop()
        answer[idx] = n - idx - 1  # 끝까지 가격이 유지된 기간 계산
    
    return answer
