def solution(n):
    # n의 최대값이 1,000,000이라서 n^2하면 시간 초과
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    
    return len(result)
        
    