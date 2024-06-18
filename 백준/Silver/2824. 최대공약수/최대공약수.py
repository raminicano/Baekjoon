from functools import reduce

n = int(input())
lin = list(map(int, input().split()))
m = int(input())
lim = list(map(int, input().split()))


def multiply_list(lst):
    return reduce(lambda x, y: x*y, lst)

a = multiply_list(lin)
b = multiply_list(lim)


# 대소 비교
def gcd(a, b):
    if a > b:
        while b != 0:
            a, b = b, a % b
        return a
    else:
        while a != 0:
            b, a = a, b % a
        return b

str_num = str(gcd(a, b))
print(str_num[-9:])