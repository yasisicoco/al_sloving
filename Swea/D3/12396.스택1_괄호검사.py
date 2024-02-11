# state 1
T = int(input())
for tc in range(1, T+1):
    text = input()
    emp = []

    result = 1
    for i in text:
        if i == '(' or i == '{':
            emp.append(i)
        elif i == ')' or i == '}':
            if emp == []:
                result = 0
                break
            if emp[-1] == '(' and i == ')' or \
                emp[-1] == '{' and i == '}':
                emp.pop()
            else:
                result = 0
                break
    else:
        if not emp == []:
            result = 0
    print(f'#{tc} {result}')





# state 2 아영신 코드
for tc in range(1, 1 + int(input())):
    def push(item):
        global top
        top += 1
        stack[top] = item
 
    def pop():
        global top
        stack[top] = 0
        top -= 1
 
    arr = list(input())
    result = 1
 
    stack = [0] * len(arr)
    top = -1
 
    for i in arr:
        if i == '(' or i == '{':
            push(i)
        elif i == ')':
            if stack[top] == '(':
                pop()
            else:
                result = 0
        elif i == '}':
            if stack[top] == '{':
                pop()
            else:
                result = 0
 
    for j in stack:
        if j != 0:
            result = 0
 
    print(f'#{tc} {result}')