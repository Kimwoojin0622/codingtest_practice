def solution(numbers):
    result = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            num = numbers[i] + numbers[j]
            result.add(num)
    
    answer = sorted(list(result))
    
    return answer