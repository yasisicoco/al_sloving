import sys

# 입력 받기
input = sys.stdin.readline
N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

# 크레인과 박스를 내림차순으로 정렬
cranes.sort(reverse=True)
boxes.sort(reverse=True)

# 예외 처리
if max(cranes) < max(boxes):
    print(-1)
    sys.exit()

# 박스를 처리한 개수를 세는 변수
count = 0

# 박스를 처리하는 데 걸리는 시간을 계산하는 함수
def time_required():
    time = 0
    while boxes:
        time += 1
        for crane in cranes:
            # 크레인으로 옮길 수 있는 박스 중에서 가장 큰 것을 찾음
            for i in range(len(boxes)):
                if boxes[i] <= crane:
                    del boxes[i]
                    break
    return time

# 처리하는 데 걸리는 시간 출력
print(time_required())
