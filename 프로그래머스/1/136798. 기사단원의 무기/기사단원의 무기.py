def solution(number, limit, power):
    # O(N^2) 불가
    tmp = [1] * number
    for i in range(1, number):
        num = i + 1
        for i in range(i, number, num):
            tmp[i] += 1
    
    result = 0
    for j in range(number):
        if tmp[j] > limit:
            tmp[j] = power
            result += tmp[j]
        else:
            result += tmp[j]
    
    return result