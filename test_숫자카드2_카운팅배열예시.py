import sys

def countingCard(card, N, checklist, M):

    card_min = card[0]
    card_max = card[0]

    for i in range(1, N):
        if card_min > card[i]:
            card_min = card[i]
        if card_max < card[i]:
            card_max = card[i]

    for i in range(N):
        card[i] -= card_min
    for i in range(M):
        checklist[i] -= card_min
    card_max -= card_min

    cnts = [0] * (card_max + 1)
    output = [0] * M

    for elem in card:
        cnts[elem] += 1

    for i in range(M):
        if 0 <= checklist[i] <= card_max:
            output[i] = cnts[checklist[i]]
        else:
            output[i] = 0

    return output

N = int(input())
card = list(map(int, sys.stdin.readline().split()))

M = int(input())
checklist = list(map(int, sys.stdin.readline().split()))

output = countingCard(card, N, checklist, M)

print(*output)