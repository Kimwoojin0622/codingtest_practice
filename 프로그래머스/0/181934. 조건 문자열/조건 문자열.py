def solution(ineq, eq, n, m):
    ineqeq = ineq + eq
    if ineqeq == '<=':
        if n <= m:
            return 1
    elif ineqeq == '>=':
        if n >= m:
            return 1
    elif ineqeq == '>!':
        if n > m:
            return 1
    else:
        if n < m:
            return 1
    
    return 0