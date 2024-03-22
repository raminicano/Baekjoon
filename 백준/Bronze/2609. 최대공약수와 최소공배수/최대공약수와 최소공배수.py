def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

n, m = map(int, input().split(' '))

# 최대공약수와 최소공배수 계산
maxnum = gcd(n, m)
minnum = lcm(n, m)

print(maxnum)
print(minnum)
