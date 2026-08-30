def solution(N):
    is_True, count = True, 1
    while is_True:
        if N == 2 or N == 1:
            is_True = False
            continue
        
        if N % 2 == 0:
            N = N // 2
        else:
            N = N // 2
            count += 1
    
    return count