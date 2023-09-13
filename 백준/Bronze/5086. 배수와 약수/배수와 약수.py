

while 1:
    # 입력데이터
    one, two = map(int, input().split())
    if one == 0 and two == 0: # 첫번째 두번째 숫자 모두 0 이면 종료함
        break
    if two % one == 0:# 첫번째 숫자가 두번째 숫자의 약수
        print('factor')
    elif one % two == 0:# 첫번째 숫자가 두번째 숫자의 배수
        print('multiple')
    else:# 첫번째 숫자가 두번째 숫자의 약수, 배수 모두 아님
        print('neither')
    


