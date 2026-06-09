def solution(numLog):
    result = []
    for i in range(1, len(numLog)):
        if numLog[i-1] + 1 == numLog[i]:
            result.append('w')
        elif numLog[i-1] - 1 == numLog[i]:
            result.append('s')
        elif numLog[i-1] + 10 == numLog[i]:
            result.append('d')
        else:
            result.append('a')
    
    return "".join(result)