import sys

T = int(sys.stdin.readline())
for _ in range(T):
    stack = []
    s = list(sys.stdin.readline().rstrip())
    
    for i in s:
        # 열린 괄호의 경우 스택에 추가
        if i == '(':
            stack.append(i)
        # 닫힌 괄호의 경우 스택 길이가 0넘으면 pop
        else:
            if len(stack) > 0:
                stack.pop()
            # 스택에 열린괄호가 존재하지 않는데 닫힌 괄호를 추가하련느 경우
            else:
                # print("NO")
                stack.append(i) # 올바르지 않은 조건임을 알리기 위해 추가
                break
    
    # for문에서 stack 을 다 검사했을 때 
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
