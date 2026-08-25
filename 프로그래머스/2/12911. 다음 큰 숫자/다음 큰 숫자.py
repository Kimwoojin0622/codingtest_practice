def solution(n):
    ntobin = bin(n).replace("0b","")
    n_one_count = ntobin.count("1")
    
    i = n + 1
    while True:
        itobin = bin(i).replace("0b","")
        i_one_count = itobin.count("1")
        
        if i_one_count == n_one_count:
            break
        else:
            i += 1
    
    return i