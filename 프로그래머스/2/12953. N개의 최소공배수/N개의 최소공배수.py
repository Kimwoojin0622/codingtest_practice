import math
def solution(arr):
    start = 0
    is_True = True
    while True:
        start = start + arr[-1]
        count = 0
        for num in arr:
            if start % num == 0:
                count += 1
            else:
                break
        
        if count == len(arr):
            break
    
    return start