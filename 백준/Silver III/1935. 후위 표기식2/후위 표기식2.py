N = int(input())
postfix = input() # 문자열 받기
num = []
st = []

for _ in range(N):
    num.append(int(input()))

for dus in postfix:
    if dus in '*/+-':
        if len(st) <= 1:
            break
        else:
            a = st.pop()
            b = st.pop()
            if dus == '*':
                st.append(b * a)
            elif dus == '/':
                st.append(b / a)
            elif dus == '+':
                st.append(b + a)
            elif dus == '-':
                st.append(b - a)
    else:
        st.append(num[ord(dus) - ord('A')]) # idx == 0 1 2 3 4
    
result = st.pop()
print(f'{result:.2f}')