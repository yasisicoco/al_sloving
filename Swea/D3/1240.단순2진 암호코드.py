from pprint import pprint
import sys
# sys.stdin = open('swea\\input\\1240.txt', 'r') # 일반
sys.stdin = open('al_sloving\\swea\\input\\1240.txt', 'r') # 디버깅

# 암호코드는 8개의 숫자
# 홀수자리의 합x3 + 짝수자리의 합 = 10의 배수
num = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 암호코드 받기 1이 있는 1줄 받고 word변수에 한줄만 저장
    arr = [input() for _ in range(N)]
    for i in range(N):
        if '1' in arr[i]:
            word = arr[i]
            break
    
    for j in range(M-1, -1, -1): # 뒤에서부터 순회
        if word[j] == '1': # 뽑아낸 줄에서 1을 찾음
            k = j # 찾아낸 1의 자리를 저장
            break

    code = [] # 8개의 값
    for s in range(k-55, k+1, 7): # 찾아낸 1의 자리는 맨 뒤 이므로 range에 넣을땐 k+1이고 따라서 k-55가 시작점이 된다.
        code.append(num[word[s:s+7]]) # code에 7자리의 딕셔너리 키값을 입력하고 벨류값을 저장

    check = 0 # 유효 암호인지 확인할 변수
    for l in range(4): # 4번돌면 8개 확인가능
        check += code[l*2]*3 + code[l*2+1] # 홀수*3 + 짝수*2
    if not check%10: # 10의 배수인가?
        print(f'#{tc} {sum(code)}')
    else:
        print(f'#{tc} {0}')