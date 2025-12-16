import sys
input = sys.stdin.readline

# 입장 시 새로운 방 생성, 처음 입장한 플레이어 기준 +-10 입장가능
# 입장 가능한 방 존재시 입장 후 모두 찰 때까지 대기
# 입장 가능한 방이 여러개라면 먼저 생성된 방에 입장
# 방의 정원이 차면 진행

# player p, nickname n, player_level l, room_max m
# 최종적으로 만들어진 방의 상태와 입장 플레이어들을 출력

p, m = map(int, input().split())
player = []
for _ in range(p):
    l, n = input().split()
    l = int(l)
    player.append((l, n))

room = []
for per in player:
    enter = False

    for r in room:
        bj_level = r[0][0]
        room_max = len(r)
        if bj_level-10 <= per[0] <= bj_level+10 and room_max < m:
            r.append(per)
            enter = True
            break
    
    if not enter:
        room.append([per])

for ans in room:
    if len(ans) == m:
        print("Started!")
    else:
        print("Waiting!")

    ans.sort(key=lambda x: x[1])
    for a in ans:
        print(*a)
    