#12917
def sumone(r):
    if r > N:
        return 0 
    if heap[r]: # True
        return heap[r]
    return sumone(r*2) + sumone(r*2+1)

T = int(input())    
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # N: 노드의개수, M: 리프노드의개수, L: 값을출력할 노드의번호
    
    heap = [0] * (N+1)
    for _ in range(M): # 리프노드의 개수만큼 반복 
        a, b = map(int, input().split()) # a번 heap에 b를 입력
        heap[a] = b
    result = sumone(L)
    print(f'#{tc} {result}')