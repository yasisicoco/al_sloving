def solution(places):
    
    def keep_distance(i, j):
        #십자
        ci = [0, 1, -1, 0]
        cj = [1, 0, 0, -1]
        #대각
        di = [-1, -1, 1, 1]
        dj = [-1, 1, -1, 1]
        
        for k in range(4):
            #십자 확인
            ni, nj = i+ci[k], j+cj[k]
            if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'P':
                return False
            
            #2십자 확인
            nni, nnj = i+ci[k]*2, j+cj[k]*2
            if 0 <= nni < 5 and 0 <= nnj < 5 and place[nni][nnj] == 'P' and place[ni][nj] != 'X':
                return False
            
            #대각확인
            ndi, ndj = i+di[k], j+dj[k]
            if 0 <= ndi < 5 and 0 <= ndj < 5 and place[ndi][ndj] == "P":
                if place[ndi][j] != 'X' or place[i][ndj] != 'X':
                    return False
        
        return True
    
    answer = []
    for place in places:
        flag = 1
        for i in range(5):
            if 'P' not in place[i]:
                continue
            for j in range(5):
                if not flag: break
                if place[i][j] == 'P':
                    if keep_distance(i, j):
                        continue
                    else:
                        flag = 0
                        break
                    
        answer.append(flag)
    print(answer)
    return answer