def solution(n):
    result = 0
    tmp = []
    while n != 0:
        num = n % 3
        tmp.append(num)
        n = n // 3
    
    tmp = tmp[::-1]
    for i in range(len(tmp)):
        num = tmp[i] * (3 ** i)
        result += num
    
    return result