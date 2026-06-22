def solution(numbers, k):
    cnt, i = 1, 0
    length = len(numbers)
    while cnt != k:
        i = i + 2
        cnt = cnt + 1
    
    return numbers[i % length]
        