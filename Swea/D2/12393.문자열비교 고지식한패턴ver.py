import sys
sys.stdin = open('D2문자열문자열비교.txt')

# T = int(input())    
# for tc in range(1, T+1):
#     result = 0
#     str_1 = input() 
#     str_2 = input()
#     if str_1 in str_2:
#         result = 1
#     print(f'#{tc} {result}')

T = int(input())
def maching(string, checking):
    for i in range(len(str_2)-len(str_1)+1):
        for j in range(len(str_1)):
            if str_2[i+j] != str_1[j]:
                break
        else:
            return 1
    return 0

for tc in range(1, T+1):
    str_1 = input()
    str_2 = input()
    # M = len(str_1) # 찾을 패턴의 길이
    # N = len(str_2) # 전체 텍스트의 길이
    result = maching(str_1, str_2)
    print(f'#{tc} {result}')

# p = 찾을 패턴
# t = 전체 텍스트
# M = len(p) 찾을 패턴의 길이
# N = len(t) 전체 텍스트의 길이

    # i = 0 # 전체 텍스트 인덱스
    # j = 0 # 찾을 패턴 인덱스
    # while j < M and i < N:
    #     if str_2[i] != str_1[j]: # 전체인덱스와 패턴 인덱스가 다를경우
    #         i = i - j # 전체 텍스트 인덱스 = 전체 - 패턴
    #         j = -1 # 뒤에서 다시 더해서 0
    #     i = i + 1 # 같으면 한칸 전진 비교
    #     j = j + 1
    # if j == M:
    #     result = 1 # 패턴을 다 돌았다면 1
    # else:
    #     result = 0 # 못찾았으면 0
    # print(f'#{tc} {result}')