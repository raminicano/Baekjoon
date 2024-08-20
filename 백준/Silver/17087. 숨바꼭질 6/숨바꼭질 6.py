from functools import reduce

# 입력받기
N, S = map(int, input().split())
li = list(map(int, input().split()))

# 동생들의 위치와 수빈이의 위치 사이의 거리 계산
distances = [abs(S - A) for A in li]

# 거리들의 최대 공약수(GCD) 계산
def gcd(a, b):
    while b !=0:
        a, b = b, a % b
    return a

answer = reduce(gcd, distances)

print(answer)