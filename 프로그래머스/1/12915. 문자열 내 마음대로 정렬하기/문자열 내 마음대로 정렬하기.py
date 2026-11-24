def solution(strings, n):
    r = sorted(strings, key = lambda x:(x[n], x))
    
    return r