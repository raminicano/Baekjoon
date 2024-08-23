# 연산자
operator = ['+', '-', '*', '/']
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alpha_num = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

# 입력
N = int(input())
li = list(input())
num_list = [0] * N
stack = []

for i in range (N):
    alpha_num[alpha[i]] = str(input())

for i in range(len(li)):
    if li[i] in operator:
        # 오퍼레이터가 있다면 예전 두개를 뽑음
        cal = stack[-2] + li[i] + stack[-1]
        stack.pop()
        stack.pop()
        cal_eval = eval(cal)
        stack.append(str(cal_eval))
    else:
        stack.append(alpha_num[li[i]])

print("%0.2f" %float(stack[0]))