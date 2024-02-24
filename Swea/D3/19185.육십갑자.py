# N개의 문자열 s1, s2, ..
# M개의 문자열 t1, t2, .. 알파벳 소문자들..
# 매 해 문자열 순서로 이름이 바뀐다
# 다음 순서의 문자열이 없으면 순회 (% 연산)
# 이름을 알고싶은 년도의 숫자가 주어짐 > 반환

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 문자열 리스트의 길이
    s = input().split()
    t = input().split()
    Q = int(input()) # Q개의 알고싶은 년도

    ans = []
    for _ in range(Q):
        year = int(input()) # year은 list의 순서
        year = year - 1 # idx: 1부터
        a = s[year%N] # 2018 % 10 == 8 > mu
        a += t[year%M]
        ans.append(a) 
    
    print(f'#{tc}', end=' ')
    for i in range(Q):
        print(ans[i], sep='', end=' ')
    print()