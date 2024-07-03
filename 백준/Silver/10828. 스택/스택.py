import sys
input = sys.stdin.read

li = []

# push
def push(x):
    li.append(x)

# size
def size():
    return len(li)

# empty
def empty():
    if li:
        return "0"
    else:
        return "1"

# top
def top():
    if li == []:
        return "-1"
    else:
        return li[-1]

# 명령어 입력 받기
commands = input().splitlines()
N = int(commands[0])

for i in range(1, N + 1):
    M = commands[i]
    if len(M.split()) == 2:
        a, b = M.split()
        push(int(b))  # b를 정수로 변환하여 저장
    else:
        if M == 'pop':
            if li == []:
                print("-1")
            else:
                print(li.pop())
        elif M == 'size':
            print(size())
        elif M == 'empty':
            print(empty())
        elif M == 'top':
            print(top())
