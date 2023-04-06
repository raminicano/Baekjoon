

# 일단 제일 큰 수로 나누기

li = [25, 10, 5, 1]
quarter = 25
dime = 10
nickel = 5
penny = 1
output = []

# 입력 받는 테스트 케이스의 개수
T = int(input())

for i in range(T):   
    num = int(input())
    # 각 케이스마다 초기화된 리스트
    temp = []
    for j in range(len(li)):
        # 몫
        share = num // li[j]
        temp.append(share)
        # 몫에서 나온 나머지를 num으로 업데이트 함
        if num != 0:
            num = num % li[j]
    # temp리스트가 출력 값을 가지고 있으니 output에 추가
    output.append(temp)

for i in range(len(output)):
    print(*output[i])
