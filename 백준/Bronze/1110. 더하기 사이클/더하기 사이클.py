N = int(input())
sto = N
count = 0

while True:
    one = sto // 10 
    two = sto % 10 
    new = (one + two) % 10  
    sto = two * 10 + new 
    
    count += 1

    if sto == N:
        break

print(count)