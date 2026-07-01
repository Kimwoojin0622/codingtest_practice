def solution(chicken):
    remain, result = 0, 0
    while True:
        if chicken >= 10:
            remain = remain + (chicken % 10)
            chicken = chicken // 10
            result += chicken
        elif chicken <= 9:
            remain += chicken
            break
    
    while True:
        if remain >= 10:
            result += (remain // 10)
            remain = (remain % 10) + (remain // 10) 
        else:
            break
    
    return result
