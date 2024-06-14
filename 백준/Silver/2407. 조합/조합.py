n, m = list(map(int, input().split()))
sum = 1
div = 1
for i in range(m):
    div = div* (m-i)
    sum = sum * (n-i)

print(sum // div)