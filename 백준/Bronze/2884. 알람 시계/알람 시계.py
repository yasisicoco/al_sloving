H, M = map(int, input().split())
if 0 <= H <= 23 and 0 <= M <= 59:
    if M <= 44:
        H = H - 1
        M = M + 15
        if H < 0:
            H = H + 24
        else:
            pass
    else:
        M = M - 45
    print(f"{H} {M}")
else:
    pass