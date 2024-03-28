import sys

input = sys.stdin.readline


def solution():
    # 에라토스테네스의 체
    goldbach = [True for _ in range(1000001)]
    for i in range(2, 1001):  # 100000의 제곱근
        if goldbach[i]:
            for j in range(i*i, 1000001, i):
                goldbach[j] = False

    while True:
        n = int(input())
        if n == 0:
            break

        for i in range(3, n):
            if goldbach[i] and goldbach[n - i]:
                print("%d = %d + %d" % (n, i, n - i))
                break
        else:
            print("Goldbach's conjecture is wrong.")


solution()