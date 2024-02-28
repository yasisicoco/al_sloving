import sys
sys.setrecursionlimit(10 ** 6)
# 재귀 허용 깊이를 수동으로 늘려주는 코드

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(i, j):
    global cnt

    if len(st) == 6: # 길이가 6일때
        cnt += 1
        return

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < 6 and 0 <= nj < 6:
            if visited[ni][nj]:
                continue
            visited[ni][nj] = True
            st.append(v[ni][nj])
            dfs(ni, nj)
            st.pop()
            visited[ni][nj] = False


v = [list(map(int, input().split())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
print(visited)
st = []
cnt = 0
dfs(0, 0)

print(cnt)