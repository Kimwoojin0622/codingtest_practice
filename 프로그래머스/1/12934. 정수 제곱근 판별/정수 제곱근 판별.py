def solution(n):
    # n을 1천만까지 돌려도 괜찮을듯
    tmp = 10000000
    for i in range(1, tmp + 1):
        if i * i == n:
            return (i + 1) ** 2
    
    return -1