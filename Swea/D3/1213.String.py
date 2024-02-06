import sys
sys.stdin = open('D3String.txt', 'r', encoding='utf-8')

T = 10

def maching(str_sear, serf):
    cnt = 0
    for i in range(len(serf) - len(str_sear) + 1):
        for j in range(len(str_sear)):
            if serf[i+j] != str_sear[j]:
                break
        else:
            cnt += 1
    return cnt

for _ in range(T):
    tc = int(input())
    str_sear = input()   # 찾을 단어
    serf = input()  # 주어진 긴문장
    result = maching(str_sear, serf)
    print(f'#{tc} {result}')