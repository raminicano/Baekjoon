N = int(input())
num = 0

for i in range(N):
    word = input()  
    data =True
    for j in range(len(word)-1):
        if word[j]!=word[j+1]:
            if word[j] in word[j+1:]:
                data=False
                break
    if data:
        num+=1
print(num)