def solution(n_str):
    temp = [data for data in n_str] # O(N) 최대 10

    while True:
        if temp[0] == "0":
            temp = temp[1:]
        else:
            break
    
    result = "".join(temp)
    return result
    
        
            