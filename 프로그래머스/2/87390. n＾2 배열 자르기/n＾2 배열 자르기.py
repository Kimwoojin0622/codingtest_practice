def solution(n, left, right):
    # O(N^2) 불가
    result = []
    for i in range(left, right + 1):
        tmp = max(i % n, i // n) + 1
        result.append(tmp)
    
    return result