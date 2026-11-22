def solution(n):
    # n의 값이 최대 50000000000000
    # 10000000을 제곱 했을 시, n의 최대 값을 뛰어넘음
    
    tmp = 10000000
    result = 0
    for i in range(1, tmp):
        if (i ** 2) == n:
            return (i+1) ** 2
    
    return -1