arr = '0A7C'
#     '0000 1010 0111 1101'
#     [0, 0, 0, 0, 1, 0, 1, 0, ...]
#16진수 문자열 -> 2진수 문자열(리스트)
hex_dict = {
    '0': '0000', '7': '0111', 'A': '1010', 'C': '1100'
}
bin_str = ''
for val in arr:
    bin_str += hex_dict[val]

print(bin_str)
# ---------------------------------------
hex_dict = {
    '0': [0,0,0,0], '7': [0,1,1,1], 'A': [1,0,1,0], 'C': [1,1,0,0]
}
bin_str = []
for val in arr:
    # bin_str += hex_dict[val]
    bin_str.extend(hex_dict[val])
print(bin_str)

# ---------------------------------------
# bit 연산 활용
bin_str = []
for val in arr:
    num = int(val, 16)
    bin_str.append(1 if num & 8 else 0)
    bin_str.append(1 if num & 4 else 0)
    bin_str.append(1 if num & 2 else 0)
    bin_str.append(1 if num & 1 else 0)
print(bin_str)