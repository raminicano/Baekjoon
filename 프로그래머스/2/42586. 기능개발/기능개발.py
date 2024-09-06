import math

def solution(progresses, speeds):
    answer = []
    check = []
    
    # 각 기능이 완료되는 데 걸리는 일수를 계산
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        check.append(day)
    
    # 첫 번째 기능이 완료되는 데 걸리는 일수를 기준으로 배포
    before_max = check[0]
    count = 1  # 첫 번째 기능은 무조건 배포 대상이므로 초기값을 1로 설정
    
    for i in range(1, len(check)):
        if before_max >= check[i]:
            # 이전에 기준이 된 기능보다 빨리 완료되면 함께 배포
            count += 1
        else:
            # 이전 기능보다 오래 걸리면 이전까지의 기능을 배포하고 새로운 기준 설정
            answer.append(count)
            count = 1  # 새로운 기능은 단독 배포 예정
            before_max = check[i]
    
    # 마지막 남은 기능 배포
    answer.append(count)
    
    return answer
