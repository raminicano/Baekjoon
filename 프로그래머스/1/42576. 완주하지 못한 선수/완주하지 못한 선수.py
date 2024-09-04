from collections import Counter

def solution(participant, completion):
    answer = ''
    # 두 리스트를 Counter로 변환 후, 차집합 구하기
    par = Counter(participant)
    com = Counter(completion)
    
    # par - com 하면 완주하지 못한 사람만 남음
    not_completed = par - com
    # 남은 key가 완주하지 못한 사람
    li = list(not_completed.keys())
    if len(li) == 0:
        answer = ''
    else:
        answer = li[0]
    
    
    return answer
    
    
