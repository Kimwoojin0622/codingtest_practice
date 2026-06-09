def solution(num_list):
    even_result = ''
    odd_result = ''
    for n in num_list:
        if n % 2 == 0:
            even_result += str(n)
        else:
            odd_result += str(n)
    
    result = int(even_result) + int(odd_result)
    
    return result