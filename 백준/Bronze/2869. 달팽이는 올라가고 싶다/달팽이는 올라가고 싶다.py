
# 입력데이터
A, B, V = map(int, input().split())

# 날짜
day = 0 # 디폴트

C = A - B
D = V - A

F = D // C

if D % C == 0:
    day += F + 1
else:
    day += F +2

print(day)