ans = list(input())
eng = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(eng)):
    # 만약 eng에서 ans가 나왔을 때, ans의 문자열 위치를 출력
    if eng[i] in ans:
        for j in range(len(ans)):
            # 입력값의 위치 찾기
            if eng[i] == ans[j]: # a 0 == a 1
                # 문자열 위치값 출력하고 바깥 포문으로
                
                print(j, end=' ')
                break
    else:
        print('-1', end=' ')
    
