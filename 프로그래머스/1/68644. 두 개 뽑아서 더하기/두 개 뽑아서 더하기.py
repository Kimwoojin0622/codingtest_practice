def solution(numbers):
    # O(N^2) 가능
    multiple = set()
    
    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            if i == j:
                continue
            multiple.add(numbers[i] + numbers[j])
    
    result = sorted(list(multiple))
    
    return result