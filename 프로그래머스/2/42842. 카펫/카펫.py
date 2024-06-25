def solution(brown, yellow):
    area = brown + yellow  # 전체 영역의 넓이
    for y in range(3, area): # area의 세로의 길이가 3 부터인 이유 -> 안에 들어가는 노란색이 1이상이므로 최소 노란색이 한 개인 경우 area의 세로는 3부터 시작
        if area % y == 0: # 영역을 세로로 나눈 값이 나누어 떨어질 때 x의 값도 자연수가 됨
            x = area // y # 그 x값 저장
            if (x - 2) * (y - 2) == yellow: # 전체 영역의 가로, 세로에서 양 옆의 길이 1씩 빼야 yellow의 가로, 세로길이가 되고 그 값을 만족하는 x, y를 리턴한다.
                return [x, y]