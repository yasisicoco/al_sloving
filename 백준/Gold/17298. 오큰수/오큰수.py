import sys
input = sys.stdin.readline
    
N = int(input())
nge = list(map(int, input().split()))
st = [0]
ans = [-1] * N

for i in range(1, N): # 오른쪽에 있는 큰 수들중 제일 왼쪽 고르기
    while st and nge[st[-1]] < nge[i]:
        ans[st.pop()] = nge[i]
    st.append(i)

print(*ans)