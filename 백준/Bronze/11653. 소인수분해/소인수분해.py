num = int(input())

li = []
for i in range(2, num+1):
    while num % i == 0:
        num = num // i
        li.append(i)
        if num ==1:
            break

for i in range(len(li)):
    print(li[i])