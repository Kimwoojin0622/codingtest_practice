def solution(numbers):
    # O(N^2) 가능
    
    chk = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if i != j:
                tmp = numbers[i] + numbers[j]
                chk.add(tmp)
    result = list(chk)
    result.sort()
    return result