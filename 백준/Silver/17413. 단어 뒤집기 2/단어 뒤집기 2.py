import sys
input = sys.stdin.readline

char = input().rstrip()

# < 태그를 만난 경우 > 를 만날때까지 lst에 추가
result = []
flag = False
lst = []
for c in char:
    if c == '<':
        result += lst[::-1] # 태그열기전 단어처리
        lst = []
        flag = True
        lst.append(str(c))

    elif c == '>':
        flag = False
        lst.append(str(c))
        result += lst
        lst = [] #초기화

    elif flag:
        lst.append(str(c))

    elif c == ' ':
        result += lst[::-1]
        result.append(' ')
        lst = [] 

    else:
        lst.append(str(c))

result += lst[::-1]

print(''.join(result))