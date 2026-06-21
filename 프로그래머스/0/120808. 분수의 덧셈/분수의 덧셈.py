import math
def solution(numer1, denom1, numer2, denom2):
    # step 1. 분모 중 작은 값을 구한다.
    denom = min(denom1, denom2)
    
    is_True = True
    # step 2. 분모 중 작은 값으로부터 시작해, 공통으로 나눠지는 분모의 값을 구한다.
    # 구한 뒤, 통분한 분수를 구한다.(약분 전임)
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
