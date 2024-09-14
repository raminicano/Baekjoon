from functools import cmp_to_key

def solution(numbers):
    answer = ''
    
    # 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 문자열을 이어붙였을 때 큰 값이 앞에 오도록 정렬
    # 비교함수 정의 : 두 숫자를 이어붙였을 때 큰 값이 앞에 오도록 함
    def compare(a,b):
        if a + b > b + a:
            return -1 # a를 먼저
        else:
            return 1 # b를 먼저
    
    # 정렬 (cmp_to_key를 사용해 커스텀 비교 함수로 정렬)
    numbers.sort(key=cmp_to_key(compare))
    
    # 정렬된 리스트를 이어붙임
    result = ''.join(numbers)
    
    # 만약 '0'으로 시작하면 (즉 모든 숫자가 0일 경우 '0'을 반환)
    return result if result[0] != '0' else '0'