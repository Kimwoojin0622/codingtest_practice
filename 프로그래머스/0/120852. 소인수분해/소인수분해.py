def decimal(t):
    if t == 2:
        return t
    else:
        num = 0
        for j in range(2, t + 1):
            if t % j == 0:
                num += 1
                        
            if t == j and num == 1:
                return t
            elif num >= 1:
                break
    return 0


def solution(n):
    # N의 최대값이 10,000이므로 O(N^2) 가능
    temp = []
    
    for i in range(2, n + 1):
        if n % i == 0:
            de = decimal(i)
            if de:
                temp.append(de)
            
    return temp