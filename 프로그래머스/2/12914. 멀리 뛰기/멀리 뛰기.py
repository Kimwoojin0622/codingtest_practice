def solution(n):
    combi = [0] * (n+1)
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    combi[1], combi[2] = 1, 2
    
    for i in range(3, n+1):
        combi[i] = combi[i-1] + combi[i-2]
    
    return combi[-1] % 1234567


