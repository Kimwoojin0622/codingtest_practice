def solution(N):
    stN = str(N)
    
    result = []
    for data in stN:
        result.append(int(data))
    
    return sum(result)