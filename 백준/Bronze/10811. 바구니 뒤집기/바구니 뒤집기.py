N, M = map(int, input().split())
bagu = list(range(1, N + 1))
for _ in range(M):
    i, j = map(int, input().split())
    i = i - 1 # bagu의 1은 리스트 0번이라서 i-1
    basket = bagu[i:j] # 새로운 변수에 슬라이싱 할당
    basket.reverse() # 거꾸로
    bagu[i:j] = basket # 거꾸로한거 다시 원래슬라이싱에 할당
        
print(*bagu)