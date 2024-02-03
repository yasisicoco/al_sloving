N = int(input())  # 5
card_1 = set(map(int, input().split()))  # 6 3 2 10 -10
M = int(input())  # 8
card_2 = list(map(int, input().split()))  # 10 9 -5 2 3 4 5 -10

result = []  # 출력값을 받을 리스트
for i in range(M):
    if card_2[i] in card_1:
        result.append(1)
    else:
        result.append(0)

print(*result)