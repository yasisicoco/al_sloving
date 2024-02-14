# 11613
import sys
sys.stdin = open('11613.txt')

# state 1
T = int(input())
for tc in range(1, T+1):

    stack = []
    fx = input().split()

    result = 'error'
    for i in fx:
        if i == '.':
            if len(stack) == 1:
                result = stack.pop()

        elif i in '*/+-': # 연산자일때
            if len(stack) < 2: # 스택안에 하나만있을때
                break # 멈춰서 그냥 나옴
            a = stack.pop()
            b = stack.pop()

            if i == '*':
                c = a * b
                stack.append(c)
            elif i == '/':
                c = b / a
                stack.append(int(c)) # 나누기는 실수이므로
            elif i == '+': 
                c = a + b
                stack.append(c)
            elif i == '-':
                c = b - a
                stack.append(c)
        
        else: # 숫자면
            stack.append(int(i)) # 문자열을 정수로바꿔서 계산
    
    print(f'#{tc} {result}')