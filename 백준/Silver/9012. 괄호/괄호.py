T = int(input())
for i in range(T):
    # 문자열 입력받기
    lst = input()
    
    st = []
    for k in lst:
        if k == '(':
            st.append(k)
        elif k == ')':
            if st and st[-1] == '(':
                st.pop()
            else:
                st.append(k)
                break
    
    if st:
        print('NO')
    else:
        print('YES')