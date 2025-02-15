def solution(quiz):
    result = []
    for vals in quiz:
        a = vals.split('=')
        # prevs = a[0].replace(" ","")
        Prev = eval(a[0])
        Next = eval(a[1])
        # Prev = eval(Prev.replace(" ",""))
        # Next = eval(Next.replace(" ",""))
        if Prev == Next:
            result.append("O")
        else:
            result.append("X")
    print(result)
    return result
