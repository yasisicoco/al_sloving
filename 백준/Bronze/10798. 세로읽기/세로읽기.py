strlst = []

for _ in range(5): # 5번 반복
    text = input()
    strlst.append(text) # 리스트에 str문자열추가

lst = []
for i in range(15): # 5번 돌면서
    for j in range(5):
        try:
            lst.append(strlst[j][i])
        except:
            continue
    else:
        continue

print(''.join(lst))