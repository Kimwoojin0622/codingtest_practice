def solution(num_list, n):
    result = []
    for i in range(n, len(num_list) + 1, n):
        result.append(num_list[i-n : i])
    
    return result