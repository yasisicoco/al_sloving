# 12916

# 부모 노드의 값 < 자식 노드의 값 
# 최소 힙
def enq(n):
    global last
    last += 1       # 마지막 노드 추가
    hip[last] = n   # 마지막 노드에 데이터 삽입
    c = last        # 자식이 마지막 노드
    p = c//2        # 부모번호 계산
    while hip and hip[p] > hip[c]: # 부모가 있고 부모가 자식보다 크면,
        hip[p], hip[c] = hip[c], hip[p] # 교환(자식이 더 커짐)
        c = p
        p = c//2

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 필요한 노드 수
    hip = [0] * (N+1)   # 힙의 개수
    last = 0            # 힙의 마지막 노드 번호
    inst = list(map(int, input().split()))   # 각 인덱스에 부여될 값
    
    for k in inst:
        enq(k)

    result = 0
    while last:
        last //= 2
        result += hip[last]
    print(f'#{tc} {result}')