def solution(strings, n):
    tmp = sorted(strings, key = lambda x : (x[n], x))
    return tmp