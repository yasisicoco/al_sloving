# 버블정렬 (O(n^2))
def BubbleSort(a, N):       # 정렬할 List, N 원소 수
    for i in range(N-1, 0, -1): # 범위의 끝 위치
        for j in range(0, i):   # 비교할 왼쪽 원소
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

# 카운팅 정렬 (O(n+k))
# 정수로 표현할 수 있는 자료형에 대해서만 적용 가능
def Counting_Sort(DATE, TEMP, k):
# DATE [] -- 입력배열 (0 to k)
# TEMP [] -- 정렬된 배열
# COUNT [] -- 카운트 배열
    
    COUNTS = [0] * (k+1)

    for i in range(0, len(DATA)):
        COUNTS[DATA[i]] += 1

    for i in range(1, k+1):
        COUNTS[i] += COUNTS[i-1]
    
    for i in range(len(TEMP)-1, -1, -1):
        COUNTS[DATA[i]] -= 1
        TEMP[COUNTS[DATA[i]]] = DATA[i]

# 순열
# {1, 2, 3}을 포함하는 모든 순열을 생성하는 함수
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i1 != i2:
            for i3 in range(1, 4):
                if i3 != i2 and i3 != i1:
                    print(i1, i2, i3)

# Greedy 알고리즘으로 Baby gin 풀기
num = 456789 # 확인할 6자리 수
c = [0] * 12 # 6자리 수로부터 각 자리수를 추출하여 개수를 누적할 리스트
for i in range(6):
    c[num % 10] += 1
    num //= 10
    
i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue;
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2: print('Baby Gin')
else: print('Lose')