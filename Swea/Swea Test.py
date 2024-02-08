T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # arr = list(map(int, input().split()))
    
    G = [[] for _ in range(V + 1)]
    for i in range(0, E*2, 2):
        u, v = G[i], G[i+1]
        G[u].append(V) # 유향그래프

    S, G = map(int, input().split())
    for j in range(1, V+1):
        print(j, '-->', G[j])
    