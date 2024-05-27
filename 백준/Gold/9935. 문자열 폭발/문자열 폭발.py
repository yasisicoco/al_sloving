import sys
input = sys.stdin.readline

strlst = input().strip()
bomb = input().strip()

st = []
for i in strlst:
    st.append(i) # 넣기
    leng = len(bomb)
    if bomb == ''.join(st[-leng:]):
        while leng: # 스택털기
            st.pop()
            leng -= 1

if st: # 스택이 남아있다면
    print(''.join(st))
else: # 다 없어졌다면
    print('FRULA')
