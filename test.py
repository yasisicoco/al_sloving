# 시험이 24 x N 시간 후에 시작, 쉬는 시간없이 24 x N 시간동안 공부가능
# 기말고사 과목이 총 M개, 시험시간이 빠른 과목부터 1~M 까지의 번호


N, M = map(int, input().split())

# 주어진 시간
max_val = 24 * N
# 최초 점수
score = list(map(int, input().split()))
# 24 x N 시간 공부할때 마다 높아지는 점수
upscore = list(map(int, input().split()))
    
def study(i, j, sumtime):
    global max_val
    
    cnt = 0
    while score[i] <= 100:
        score[i] += upscore[i] 
        cnt += 1
    
