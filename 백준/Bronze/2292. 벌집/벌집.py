
# 숫자 N이 벌집에서 몇 겹째에 있는지를 출력하는 문제
# 벌집의 개수가 6의 배수로 증가하고 있음

N = int(input())
ans = 1
num = 1

while N > num:
    num += 6 * ans
    ans += 1

print(ans)