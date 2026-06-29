def solution(polynomial):
    # polynomial은 일차항과 상수항만 존재
    # 계수 1은 생략, 결과값에 상수항은 마지막에 둡니다.
    temp = polynomial.split(" + ")
    
    x_plus, num_plus = 0, 0
    for data in temp:
        if data[-1] == 'x':
            if len(data) == 1:
                x_plus += 1
            else:
                x_plus += int(data[:-1])
        else:
                num_plus += int(data)
    
    if x_plus and num_plus:
        if x_plus == 1:
            return 'x' + ' + ' + str(num_plus)
        else:
            return str(x_plus) + 'x' + ' + ' + str(num_plus)
    elif x_plus:
        if x_plus == 1:
            return 'x'
        else:
            return str(x_plus) + 'x'
    else:
        return str(num_plus) 
    
    # 엣지 케이스 추가
    # "x + 1"
    # "1"
    # "9 + 10"
    # "5x + 6x"
    # "3x + 5"
