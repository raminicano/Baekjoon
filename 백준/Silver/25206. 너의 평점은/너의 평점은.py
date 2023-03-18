
# 전공평 = sum(학점 * 과목평점) / 학점의 총합

score = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0, 'P' : 0.0 }
# 전체 수강한 평점
total = 0
# 학점 * 과목평점, 실제 점수
sub_score = 0


for i in range(20): # 20줄에 걸쳐 데이터가 주어진다고 제시됨
    name, num, alp = input().split()
    if alp == 'P':  # 등급이 P인 과목은 계산에서 제외
        continue
    num = float(num)  # 숫자형으로 바꿔줌
    total += num
    sub_score += num * score[alp]

print(sub_score / total)