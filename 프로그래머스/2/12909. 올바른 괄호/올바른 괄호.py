from collections import deque
def solution(s):
    answer = True
    openq = deque()
    for i in s:
        # 열려있는 큐가 없다면 닫혀있는게 나오면 false
        isEmpty = len(openq) == 0
        isClose = i == ")"
        if isEmpty & isClose:
            return False
        # 닫혀있는게 나오면 열려있는 것 pop
        elif isClose:
            openq.pop()
        else:
            openq.append(i)
    
    # 두개의 큐가 비어있다면 true반환하도록
    if len(openq) == 0:
        answer = True
    else:
        answer = False

    return answer