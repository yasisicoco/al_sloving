from collections import deque

N = int(input())
lst = list(map(int, input().split()))

lst = deque(lst)
st = []
cnt = 1
while lst or st:
    if lst and st:
        if lst[0] == cnt:
            lst.popleft()
            cnt += 1
        if st[-1] == cnt:
            st.pop()
            cnt += 1
    if lst or st:
        if lst[0] == cnt: # 순서가 맞으면
            lst.popleft()
            cnt += 1
        else: # 순서가 아니라면
            st.append() # 왼쪽에 줄세우기
    if st:
        if st[-1] == cnt:
            anx = st.pop()
            
    elif not lst and st: # 기존 줄 끝났을 때
        k = st.pop() # 왼쪽 줄에서 후입선출
        if k == cnt: # k가 순서라면
            cnt += 1 # 줄 += 1

if cnt-1 == N:
    print('Nice')
else:
    print('Sad')