def solution(numbers, target):
    
    def dfs(index, curNum):
        if index == len(numbers):
            if curNum == target: # 목표숫자 완성
                return 1
            else: return 0 # 목표숫자가 완성실패
        
        
        plus = dfs(index + 1, curNum + numbers[index]) # 다음 1 , numbers[0] ==> 5, numbers[4] 
        minus = dfs(index + 1, curNum - numbers[index])
        return plus + minus
    
    return dfs(0, 0)