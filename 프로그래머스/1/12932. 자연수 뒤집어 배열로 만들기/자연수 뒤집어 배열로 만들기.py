def solution(n):
    stN = str(n)
    
    result = []
    for i in range(len(stN) - 1, -1, -1):
        tmp = int(stN[i])
        result.append(tmp)
    
    return result