'''
두 개의 문자열 str1과 str2가 주어진다. 
문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 
그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.
예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, 
str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.
파이썬의 경우 딕셔너리를 이용할 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어진다. 
5≤N≤100, 10≤M≤1000, N≤M
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
import sys
sys.stdin = open('D2문자열글자수.txt')

T = int(input())
for tc in range(1, T+1):
    strlst = input()
    str1 = set()
    for char in strlst:
        str1.add(char)
    str2 = input()
    str1_dict = {}
    str2_dict = {}
    for j in str2:
        str2_dict.setdefault(j, 0)
    for i in str1: #str1의 i를
        for k in str2: #str2 dict를 돌면서 확인
            if i == k:
                str2_dict[i] += 1
    # print(str1_dict)
    # str2 디렉 키값을 돌면서 밸류를 비교해서 제일 높은 얘를 출력
    max_val = 0
    for value in str2_dict.values():
        if max_val < value:
            max_val = value
    print(f'#{tc} {max_val}')
    
    
    
    
    
# state 2 / 240225
# T = int(input())
# for tc in range(1, T+1):
#     str1 = ''.join(list(set(input()))) # 중복제거
#     str2 = input()
    
#     result = 0 # 최대값 저장
#     for i in str1: # 문자열 1의 문자를 순회
#         cnt = 0 # 각 문자열 길이 비교용
#         for j in str2: # 문자열 2의 문자를 전부순회
#             if i == j: # 만약 둘이 같다면 +1를 카운트
#                 cnt += 1
#             if result <= cnt:
#                 result = cnt
    
#     # 다돌고 최대값 출력
#     print(f'#{tc} {result}')