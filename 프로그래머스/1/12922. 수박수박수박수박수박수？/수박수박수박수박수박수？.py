def solution(n):
    result = ''
    watermelon = ['수', '박']
    
    for i in range(n):
        tmp = i % 2
        result += watermelon[tmp]
    
    return result