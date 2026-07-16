def solution(n):
    tmp = ['수','박']
    result = []
    for i in range(n):
        result.append(tmp[i % 2])
    
    return "".join(result)