from collections import Counter

def solution(clothes):
    # 카테고리별로 의상의 수를 세기
    counter = Counter([category for name, category in clothes])
    
    # 각 카테고리별로 (아이템 개수 + 1) 만큼 선택할 수 있는 경우의 수를 모두 곱함
    answer = 1
    for count in counter.values():
        answer *= (count + 1)
    
    # 모든 카테고리에서 아무것도 선택하지 않은 경우는 제외해야 하므로 1을 빼줌
    return answer - 1
