def solution(quiz):
    result = []
    for vals in quiz:
        L, R = vals.split(' = ')
        a, nd, b = L.split()
        print(a, nd, b, R)
        if nd == '+':
            if int(a) + int(b) == int(R):
                result.append('O')
            else:
                result.append('X')
        elif nd == '-':
            if int(a) - int(b) == int(R):
                result.append('O')
            else:
                result.append('X')
    # print(result)
            
    return result
