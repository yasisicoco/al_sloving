A = int(input())
B = int(input())
C = int(input())

zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ABCD = A * B * C
ABC = str(ABCD)
for i in ABC:
    if i == '0':
        zero += 1
    elif i == '1':
        one += 1
    elif i == '2':
        two += 1
    elif i == '3':
        three += 1
    elif i == '4':
        four += 1
    elif i == '5':
        five += 1
    elif i == '6':
        six += 1
    elif i == '7':
        seven += 1
    elif i == '8':
        eight += 1
    elif i == '9':
        nine += 1

print(zero)
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)
print(nine)