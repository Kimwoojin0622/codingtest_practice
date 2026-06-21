import math
def solution(numer1, denom1, numer2, denom2):
    
    denom = min(denom1, denom2)
    
    is_True = True
    while is_True:
        if denom % denom1 == 0 and denom % denom2 == 0:
            is_True = False
            numer1 = numer1 * (denom // denom1)
            numer2 = numer2 * (denom // denom2)
            
            numer = numer1 + numer2
        else:
            denom = denom + 1

    # step 3. 약분 코드
    while True:
        n = min(numer, denom)
        cnt = 0
        for i in range(2, n + 1):
            if numer % i == 0 and denom % i == 0:
                divide_value = i
                cnt += 1
        if cnt < 1:
            break
        else:
            numer = numer // divide_value
            denom = denom // divide_value
    
    return [numer, denom]