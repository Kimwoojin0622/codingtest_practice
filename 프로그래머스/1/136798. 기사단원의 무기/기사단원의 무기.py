def solution(number, limit, power):
    # O(N^2) 불가
    tmp = [1] * number
    for i in range(1, number):
        for j in range(i, number, i+1):
            tmp[j] += 1
    
    result = 0
    for t in tmp:
        if t > limit:
            result += power
        else:
            result += t
    
    return result