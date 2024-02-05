color_1, color_2 = input().split()
color_3, color_4 = input().split()

s = set([color_1, color_2, color_3, color_4])
lst = list(s)
lst.sort()

for i in lst:
    for j in lst:
        print(i, j)