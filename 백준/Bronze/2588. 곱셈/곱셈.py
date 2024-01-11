A = int(input())
B = int(input())

while True:
    bvalue = list(str(B))
    bvalue.reverse()
    for i in bvalue:
        ib = int(i)
        print(ib * A)
    print(A * B)
    break