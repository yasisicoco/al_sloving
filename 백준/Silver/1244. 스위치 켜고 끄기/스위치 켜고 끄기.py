# 남학생 : 자기가 받은 수의 배수의 스위치상태를 바꿈
# 여학생 : 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장많은 스위치를 포함하는 구간을 찾아서, 그 구간의 스위치 상태를 변경

# 스위치 개수: 100 이하인 양의 정수
sw_num = int(input())

# 각 스위치의 상태
sw_stat = list(map(int, input().split()))

# 학생 수 100이하인 양의 정수
student = int(input())

# 남학생은 1, 여학생은 2 / 학생 수 만큼 순회
for i in range(student):
    gen, n = map(int, input().split())
    
    # 남학생이면
    if gen == 1:
        for j in range(1, 101):
            posi = n * j - 1
            if 0 <= posi < sw_num:
                if sw_stat[posi] == 1:
                    sw_stat[posi] = 0
                else:
                    sw_stat[posi] = 1
    # 여학생이면
    elif gen == 2:
        # 먼저 받은 자리의 수 바꾸고
        if sw_stat[n-1] == 1:
            sw_stat[n-1] = 0
        else:
            sw_stat[n-1] = 1

        for k in range(1, 101):
            front, rear = n-k-1, n+k-1
            if 0 <= front < sw_num and 0 <= rear < sw_num: # 범위 안쪽일때
                if sw_stat[front] == sw_stat[rear]: # 같을때
                    if sw_stat[front] == 1:
                        sw_stat[front] = 0
                        sw_stat[rear] = 0
                    else:
                        sw_stat[front] = 1
                        sw_stat[rear] = 1
                else: # 다를 때
                    break 

for i in range(0, sw_num, 20):
    print(*sw_stat[i:i+20])