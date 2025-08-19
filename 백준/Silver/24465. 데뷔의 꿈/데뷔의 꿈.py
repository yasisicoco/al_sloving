import sys
input = sys.stdin.readline

horoscope_ranges = {
    '물병자리': ((1, 20), (2, 18)),
    '물고기자리': ((2, 19), (3, 20)),
    '양자리': ((3, 21), (4, 19)),
    '황소자리': ((4, 20), (5, 20)),
    '쌍둥이자리': ((5, 21), (6, 21)),
    '게자리': ((6, 22), (7, 22)),
    '사자자리': ((7, 23), (8, 22)),
    '처녀자리': ((8, 23), (9, 22)),
    '천칭자리': ((9, 23), (10, 22)),
    '전갈자리': ((10, 23), (11, 22)),
    '사수자리': ((11, 23), (12, 21)),
    '염소자리': ((12, 22), (1, 19)),
}

def findStar(month, day):
    for sign, (start, end) in horoscope_ranges.items():
        if sign == '염소자리':
            if (month == start[0] and day >= start[1]) or \
               (month == end[0] and day <= end[1]):
                return sign
        elif (month == start[0] and day >= start[1]) or \
             (month == end[0] and day <= end[1]) or \
             (month > start[0] and month < end[0]):
            return sign
    return None

exist = set()

for _ in range(7):
    m, d = map(int, input().split())
    exist.add(findStar(m, d))

N = int(input())
applyer = []

for _ in range(N):
    m, d = map(int, input().split())
    Star = findStar(m, d)
    
    if Star not in exist:
        applyer.append((m, d))

applyer.sort()

if not applyer:
    print("ALL FAILED")
else:
    for m, d in applyer:
        print(m, d)

