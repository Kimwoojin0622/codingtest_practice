def solution(n):
    tmp = [0] * n

    for i in range(n):
        if i == 0:
            tmp[i] = 0
            continue
        if i == 1:
            tmp[i] = 1
            continue
        
        tmp[i] = tmp[i-1] + tmp[i-2]
    
    return (tmp[-1] + tmp[-2]) % 1234567
        