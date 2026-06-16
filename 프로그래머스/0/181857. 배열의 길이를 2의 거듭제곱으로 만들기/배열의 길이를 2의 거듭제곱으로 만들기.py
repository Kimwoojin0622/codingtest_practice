def solution(arr):
    sq_2 = [2**i for i in range(1001)] # O(N) 1000
    temp = 0
    for n in sq_2: # O(N)
        if len(arr) <= n: # O(1)
            temp = n
            break
    
    if temp == len(arr):
        return arr
    else:
        length = temp - len(arr)
        for _ in range(length):
            arr.append(0)
    
    return arr