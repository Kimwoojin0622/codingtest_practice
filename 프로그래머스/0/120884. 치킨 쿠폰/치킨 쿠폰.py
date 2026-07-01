def solution(chicken):
    remain, is_True = 0, True
    result = []
    while is_True:
        if chicken >= 10:
            remain = remain + (chicken % 10)
            chicken = chicken // 10
            result.append(chicken)
        elif chicken <= 9:
            remain += chicken
            is_True = False
    
    remain
    while True:
        if remain >= 10:
            result.append(remain // 10)
            remain = (remain % 10) + (remain // 10) 
        else:
            break
    
    return sum(result)