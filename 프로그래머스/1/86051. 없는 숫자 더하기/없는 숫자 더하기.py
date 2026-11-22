def solution(numbers):
    check = {}
    for i in range(0, 10):
        if i not in check:
            check[i] = 0
    
    for n in numbers:
        check[n] = 1

        
    result = 0
    for data in check.items():
        if data[1] == 0:
            result += data[0]
    
    return result