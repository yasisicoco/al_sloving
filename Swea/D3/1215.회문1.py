import sys
sys.stdin = open('1215.txt')

T = 10
for tc in range(1, T+1):
    N = int(input()) # 회문의 길이 4
    arr = [list(input()) for _ in range(8)] # 글자 판
    # for line in arr:
    #     print(*line)

    cnt = 0
    # 세로회문검사
    for i in range(8): 
        for j in range(8-N+1):
            e = j+N-1 # 세로회문 마지막 str
            for k in range(N//2): # 길이의 반만큼 실행
                if arr[j+k][i] != arr[e-k][i]:
                    break
            else:
                cnt += 1

    # 가로회문검사
    for i in range(8):
        for j in range(8-N+1):
            e = j+N-1
            for k in range(N//2):
                if arr[i][j+k] != arr[i][e-k]:
                    break
            else:
                cnt += 1
    print(f'#{tc} {cnt}')



'''

# 보충 강사님 코드

    # 🛰️ 코드
T = 10  # 테스트 케이스의 수를 설정합니다.
N = 8  # 보드의 크기를 설정합니다.
for tc in range(1, T+1):  # 각 테스트 케이스에 대해
    length = int(input())  # 팰린드롬의 길이를 입력받습니다.
    board = [list(input()) for _ in range(N)]  # N x N 크기의 보드를 입력받습니다.
    result = 0  # 팰린드롬의 개수를 저장할 변수를 초기화합니다.
    for i in range(N):  # 보드의 각 행에 대해
        for j in range(N - length +1):  # 팰린드롬의 길이를 고려하여 각 열에 대해
            h = board[i][j:j+length]  # 가로 방향의 문자열을 추출합니다.
            if h == h[::-1]:  # 추출한 문자열이 팰린드롬이라면
                result += 1  # 결과에 1을 더합니다.
            v = [k[i] for k in board[j:j+length]]  # 세로 방향의 문자열을 추출합니다.
            if v == v[::-1]:  # 추출한 문자열이 팰린드롬이라면
                result += 1  # 결과에 1을 더합니다.

    print(f'#{tc} {result}')  # 테스트 케이스 번호와 팰린드롬의 개수를 출력합니다.
    
    
브루트 포스
T = 10  # 테스트 케이스의 수입니다.

def bf(pattern, text):
    len_p = len(pattern)  # 패턴 문자열의 길이를 계산합니다.
    len_t = len(text)  # 텍스트 문자열의 길이를 계산합니다.
    i = j = 0  # 텍스트와 패턴을 순회하는 인덱스입니다.
    cnt = 0  # 패턴이 텍스트에서 등장하는 횟수입니다.
    while i < len_t and j < len_p:  # 텍스트와 패턴을 동시에 순회합니다.
        if text[i] != pattern[j]:  # 만약 현재 위치의 문자가 서로 다르다면
            i = i - j  # 텍스트의 인덱스를 되돌립니다.
            j = - 1  # 패턴의 인덱스를 초기화합니다. < 여기까지탐색
        i += 1  # 텍스트의 인덱스를 증가시킵니다.
        j += 1  # 패턴의 인덱스를 증가시킵니다. < 계속진행
        if j == len_p:  # 만약 패턴을 모두 순회했다면
            cnt += 1  # 카운트를 증가시킵니다.
            i = i - j + 1  # 텍스트의 인덱스를 패턴의 길이만큼 되돌립니다.
            j = 0  # 패턴의 인덱스를 초기화합니다. < 성공
    return cnt  # 패턴이 텍스트에서 등장하는 횟수를 반환합니다.

for _ in range(T):  # 각 테스트 케이스에 대해
    tc = input()  # 테스트 케이스 번호를 입력받습니다.
    result = 0  # 결과를 저장할 변수를 초기화합니다.
    pattern = input()  # 패턴 문자열을 입력받습니다.
    text = input()  # 텍스트 문자열을 입력받습니다.
    result = bf(pattern, text)  # bf 함수를 사용하여 결과를 계산합니다.
    print(f'#{tc} {result}')  # 테스트 케이스 번호와 결과를 출력합니다.

'''