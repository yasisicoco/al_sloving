# N = int(input())
#
# lst = [[0] * 7 for _ in range(2)]
#
# t1 = N
# for i in range(4):
#     lst[0][i] = t1
#     t1 += 1
#
# t2 = N
# for i in range(6, 2, -1):
#     lst[1][i] = t2
#     t2 -= 1
#
# print(lst)

# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
#
# n, m = map(int, input().split())
# print(n+m, n*m)

dic = {
    0: '0000',
    1: '0001',
    2: '0010',
    3: '0011',
    4: '0100',
    5: '0101',
    6: '0110',
    7: '0111',
    8: '1000',
    9: '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}
print(dic[1])
print(dic[5])
print(dic[4])
print(dic[3])
print(dic[2])