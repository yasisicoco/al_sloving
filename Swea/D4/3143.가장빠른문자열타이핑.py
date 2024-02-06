import sys
sys.stdin = open('3143.txt')


T = int(input())
def maching():
    cnt = 0
    for i in range(len(A)-len(B)+1):
        for j in range(len(B)):
            if A[i+j] != B[j]:
                break
        else:
            cnt += 1

for tc in range(1, T+1):
    A, B = input().split()
    result = maching() # cnt
    print(f'#{tc} {result}')
    # A길이 - (B길이*cnt) + cnt

    # A_len = len(A) #banana
    # B_len = len(B) #bana
