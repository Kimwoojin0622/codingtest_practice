def solution(n):
    result = []
    for i in range(n):
        result.append([0] * n)
    
    for j in range(n):
        result[j][j] = 1
        
    return result