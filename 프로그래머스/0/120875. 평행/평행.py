def solution(dots):
    a, b, c, d = dots[0], dots[1], dots[2], dots[3]

    # ab cd
    if abs((a[0]-b[0]) / (a[1]-b[1])) == abs((c[0]-d[0]) / (c[1]-d[1])):
        print('abcd')
        return 1
    # ac bd
    elif abs((a[0]-c[0]) / (a[1]-c[1])) == abs((b[0]-d[0]) / (b[1]-d[0])):
        print('acbd')
        return 1
    # ad bc
    elif abs((a[0]-d[0]) / (a[1]-d[1])) == abs((b[0]-c[0]) / (b[1]-c[1])):
        print('adbc')
        return 1
    else:
        return 0