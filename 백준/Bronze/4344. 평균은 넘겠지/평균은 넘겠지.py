
C = int(input())
# 평균 비율을 담을 list변수 선언
truth = []

for i in range(C):
    li = list(map(int, input().split()))
    data = li[1:] #1~ 까지는 점수
    num = li[0]    # 입력받은 데이터의 첫번째 문자는 리스트의 길이
    avg = sum(data) / num
    temp = len([i for i in data if i > avg]) / num  # 평균이 넘는다면 추가하고 그 추가된 리스트의 길이를 구하고 본래 리스트의 길이로 나눔
    truth.append(temp)  # 진실을 알려주는 리스트에 추가

# % 단위 변경하기
for i in truth:
    print("%.3f%%" %(i*100))

