import math

def solution(n):
    tmp = int(math.sqrt(n)) + 1
    for i in range(1, tmp + 1):
        if i * i == n:
            return 1
    
    return 2
