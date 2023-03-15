
li = list(input().lower())
max = 0
se = set(li)
dic = {}

for i in se:
    num = li.count(i)
    dic[i] = num
    if num > max:   # 계산된 숫자가 max보다 크면
        max = num   # max로 변경함
        data = i.upper()    # 해당 데이터도 대문자로 담아놓음
    elif num == max:
        data = "?"

print(data)