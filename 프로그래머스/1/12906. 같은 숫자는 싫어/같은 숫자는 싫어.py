

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]: # 현재 위치에 있는 값이 그 전에 있던 위치의 값과 같다면
            continue
        else:
            answer.append(arr[i])
    return answer