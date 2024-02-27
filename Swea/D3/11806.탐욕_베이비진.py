# player 1 win : 1
# player 2 win : 2
# else         : 0

# run : 연속인 숫자가 3개 이상
# triplet : 같은 숫자가 3개 이상
    
def check(player1, player2):
    global result
    for i in range(0, 12, 2): # 카드 번갈아서 가져가기
        player1.append(card[i])   
        player2.append(card[i+1])


        for j in range(10):
            if player1.count(j) >= 3:
                result = 1
                return result
            elif j in player1 and j+1 in player1 and j+2 in player1: # 연속된 숫자
                result = 1
                return result

        for k in range(10):
            if player2.count(k) >= 3:
                result = 2
                return result
            elif k in player2 and k+1 in player2 and k+2 in player2: # 연속된 숫자
                result = 2
                return result
            
    return result
T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))

    result = 0
    player1 = []
    player2 = []
    

    print(f'#{tc} {check(player1, player2)}')