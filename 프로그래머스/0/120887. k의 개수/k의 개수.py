def solution(i, j, k):
    result = 0
    for n in range(i, j+1):
        temp = str(n).count(str(k))
        result += temp
    
    return result