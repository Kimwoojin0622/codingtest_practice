import math
def solution(number, limit, power):
    # O(N^2)은 무리
    knight = [0] * number
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            knight[j-1] += 1
        
    result = 0
    for k in knight:
        if k <= limit:
            result += k
        else:
            result += power
    
    return result
