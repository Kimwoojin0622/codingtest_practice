def solution(s):
    tmp = s.split(" ")
    min_n = 9999999999999
    max_n = -9999999999999
    
    for num in tmp:
        if int(num) < min_n:
            min_n = int(num)
            
    for num in tmp:
        if int(num) > max_n:
            max_n = int(num)
    
    return str(min_n) + " " + str(max_n)