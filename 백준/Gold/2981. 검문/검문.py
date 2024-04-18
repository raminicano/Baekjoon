N = int(input())
num = sorted([int(input()) for _ in range(N)])
re_num = []

# B-A, C-B, D-C... 차이를 계산
for i in range(1, N):
    re_num.append(num[i] - num[i-1])

# 최대공약수를 계산하는 함수
def findGCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 차이들의 최대공약수를 계산
GCD = re_num[0]
for idx in range(1, len(re_num)):
    GCD = findGCD(GCD, re_num[idx])

# GCD의 약수를 구하고 출력
result = set()
for i in range(2, int(GCD**0.5) + 1):
    if GCD % i == 0:
        result.add(i)
        result.add(GCD // i)
result.add(GCD)
print(*sorted(list(result)))
