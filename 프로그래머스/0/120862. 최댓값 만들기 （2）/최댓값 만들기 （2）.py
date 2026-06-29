def solution(numbers):
    # N은 최대 100 O(N^2) 가능
    max_value = -999999999 # numbers 원소 최소값이 -10000
    length = len(numbers)
    for i in range(length):
        for j in range(length):
            if i != j:
                if numbers[i] * numbers[j] > max_value:
                    max_value = numbers[i] * numbers[j]
    
    return max_value