strr = input().strip()
if strr != '':
    cnt = 1
    for i in strr:
        if i == ' ':
            cnt += 1
else:
    cnt = 0
print(cnt)