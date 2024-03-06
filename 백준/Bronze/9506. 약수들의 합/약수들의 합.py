# 완전수 -> n을 n이 아닌 약수들의 합으로 나타내어 출력, 약수들 오름차순 나열
# 완전수X -> n is NOT perfect. 출력
test = []
n = 2
while(n<10000):
    num = int(input())
    if num == -1:
        break
    test.append(num)
    n +=1


for j in range(len(test)):
    li = []
    for i in range(1,test[j]):
        if test[j] % i == 0:
            li.append(i)

    if test[j] == sum(li):
        print(str(test[j]) + ' = ', end='')
        for i in range(len(li)):
            if i == len(li) -1:
                print(li[i])
            else:
                print(str(li[i]) + ' +', end=" ")
    else:
        print(str(test[j]) + " is NOT perfect.")