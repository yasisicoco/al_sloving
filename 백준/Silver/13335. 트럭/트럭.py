from collections import deque

# 리스트 안에 무게확인
def check(lst, addTrcuk):
    # 기존 다리위 트럭무게 + 추가된 트럭 무게
    if sum(lst) - lst[0] + addTrcuk <= L:
        return True
    return False

# n트럭수, w다리길이, L다리최대하중
n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
# 단위 시간
time = 0
bridge = deque([0] * w)
for truck in trucks:
    # 길이확인부터
    if len(bridge) <= w:
        # 다리 위에 올라갈수 있는지?
        if check(bridge, truck):
            bridge.append(truck)
            if len(bridge) > w:
                bridge.popleft()
            time += 1
            continue
        # 못올라간다면 올라갈때까지
        else:
            while True:
                if check(bridge, truck): # 다음 트럭들어갔을때 확인
                    bridge.append(truck)
                    if len(bridge) > w:
                        bridge.popleft()
                    time += 1
                    break
                bridge.append(0) # 오른쪽에 0 더하기
                if len(bridge) > w:
                    bridge.popleft()
                time += 1 # 단위시간 더하기
while bridge:
    bridge.popleft()
    time += 1
print(time)