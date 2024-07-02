


def is_prime(n):
    primes = [True] * (n+1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
            
        p += 1
    
    return primes


def goldbach(n, primes):
    partitions = []
    for i in range(2, n //2 + 1):
        if primes[i] and primes[n - i]:
            partitions.append((i, n-i))
    return partitions

# T 입력받기
T = int(input())

li = [True] * T
# 정수 N 입력받기
li = [int(input()) for i in range(T)]

max_num = max(li)
primes = is_prime(max_num)

for num in li:
    if num % 2 != 0 or num <=2:
        continue
    else:
        partitions = goldbach(num, primes)
        print(len(partitions))