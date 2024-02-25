# state 1
# stack, ''.join() method

T = 10
for tc in range(1, T+1):
    leng, num = map(str, input().split())
    leng = int(leng)
    
    st = []
    for i in range(leng): # num의 길이만큼 순회
        # 스택안에 아무것도 없을때, 스택의 맨뒤와 문자열의i번째가 다를때 추가
        if st == [] or st[-1] != num[i]:
            st.append(num[i])
        
        else: # 스택의 맨뒤와 문자열의 i번째가 같을 때
            st.pop() # 스택 후입을 선출시킨다.
    
    # 다 돌고 스택 프린트
    print(f'#{tc}', ''.join(st))