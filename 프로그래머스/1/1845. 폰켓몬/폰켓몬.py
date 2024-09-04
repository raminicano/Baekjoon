def solution(nums):
    # 중복을 제거한 종류의 수
    unique_types = len(set(nums))
    # 선택할 수 있는 숫자의 최대 수
    N = len(nums) // 2
    # 가능한 최대 종류의 수는 unique_types와 N 중 작은 값
    return min(unique_types, N)
