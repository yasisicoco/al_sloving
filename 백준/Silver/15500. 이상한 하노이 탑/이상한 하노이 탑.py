import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

pole1 = lst
pole2 = []   
moves = [] 

for i in range(N):
    target = N - i

    if target in pole1:
        while True:
            disk = pole1.pop()
            if disk == target:
                moves.append("1 3")
                break
            else:
                moves.append("1 2")
                pole2.append(disk)
    else:
        while True:
            disk = pole2.pop()
            if disk == target:
                moves.append("2 3")
                break
            else:
                moves.append("2 1")
                pole1.append(disk)

print(len(moves))
for move in moves:
    print(move)
