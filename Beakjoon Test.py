def recur(cur):
    if len(password) == 4:
        for k in password:
            if k in 'aeiou':
                password.sort()
                print(*password, sep='')
            break    
        return
    
    for i in range(cur, C):
        if visited[i]:
            continue
        visited[i] = True
        password.append(str_lst[i])
        recur(i)
        password.pop()
        visited[i] = False


L, C = map(int, input().split())
str_lst = list(input().split())
str_lst.sort()
visited = [False] * (C+1)
password = []
recur(0)