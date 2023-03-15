li = list(input())
N = len(li)
mid = N // 2
dom = "1"

for i in range(mid):
    if li[i] == li[N-1-i]:
        pass
    else:
        dom = "0"
        break

print(dom)