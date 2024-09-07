from collections import deque

def solution(priorities, location):
    # 프로세스의 인덱스와 우선순위를 함께 저장
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    order = 0  # 실행 순서
    
    while queue:
        # 현재 실행되어야할 프로세스
        current = queue.popleft()
        # 만약 현재 프로세스보다 높은 우선순위가 큐에 있으면 다시 뒤로 보냄
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            # 현재 프로세스를 실행함
            order += 1
            # 실행된 프로세스가 우리가 찾는 프로세스라면
            if current[0] == location:
                return order
