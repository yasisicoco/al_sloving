

# player 1 win : 1
# player 2 win : 2
# else         : 0

# run : 연속인 숫자가 3개 이상
# triplet : 같은 숫자가 3개 이상
    
def run(player):

    run_num = -1 # 이전 카드
    cnt = 0
    for k in player: # 카드를 뽑는 도중
        if k == run_num: # 방금 뽑은 카드 k와 이전 카드를 비교
            cnt += 1 # 같다면 cnt += 1
        run_num = k  # 방금 뽑은거 저장
        
        if cnt >= 3: # 3번 연속이면 승리
            return 1
    
    return 0

def triplet(player):

    arr = [0] * 10
    for l in player:
        arr[l] += 1
        if arr[l] >= 3:
            return 1
    
    return 0
            
    
    
    
T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))

    result = 0
    player1 = []
    player2 = []
    for i in range(0, 12, 2): # 카드 번갈아서 가져가기
        player1.append(card[i])   
        if run(player1) == 1 or triplet(player1) == 1:
            result = 1
            break     # 9 5 5 1 4 2  // case 1
        player2.append(card[i+1])    # 9 6 6 1 2 1   
        if run(player2) == 1 or triplet(player1) == 1:
            result = 2
            break

    
    print(f'#{tc} {result}')
