def solution(left, right):
    # O(N^3)은 위태
    check = {}
    for i in range(left, right+1):
        if i not in check:
            check[i] = 0
    
    for data in check.items():
        for i in range(1, data[0]+1):
            if data[0] % i == 0:
                check[data[0]] += 1

    result = 0
    for data in check.items():
        if data[1] % 2 == 0:
            result += data[0]
        else:
            result -= data[0]
    
    return result