def solution(polynomial):
    # polynomial은 일차항과 상수항만 존재
    # 계수 1은 생략
    # 결과값에 상수항은 마지막에 둡니다.
    temp = polynomial.split(" + ")
    
    x_plus = []
    num_plus = []
    for s in temp:
        if 'x' in s:
            if len(s) == 1:
                x_plus.append('1x')
            else:
                x_plus.append(s)
        else:
            num_plus.append(s)
    
    chk = x_plus + num_plus
    x_tmp = 0
    num_tmp = 0
    for data in chk:
        if 'x' in data:
            x_tmp = x_tmp + int(data[:-1])
        else:
            num_tmp = num_tmp + int(data)
    
    if x_tmp > 0 and num_tmp > 0:
        if x_tmp == 1:
            return 'x' + ' + ' + str(num_tmp)
        else:
            return str(x_tmp) + 'x' + ' + ' + str(num_tmp)
    elif x_tmp > 0:
        if x_tmp == 1:
            return "x"
        else:
            return str(x_tmp) + 'x'
    else:
        return str(num_tmp)