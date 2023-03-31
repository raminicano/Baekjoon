
N, B = input().split()

# B는 숫자로 바꾸기
B = int(B)
# 진법 계산을 위해 문자열 뒤집기
N = N[::-1]

# 진법
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0

for i in range(len(N)):
    # N에 해당되는 위치의 숫자 구하기
    for j in range(len(num)):
        if N[i] == num[j]:
            sum += (B**i) * j

print(sum)