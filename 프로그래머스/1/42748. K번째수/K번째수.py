def solution(array, commands):
    result = []
    for i in range(len(commands)):
        i, j, k = commands[i]
        
        arr = sorted(array[i-1:j])
        result.append(arr[k-1])

    return result