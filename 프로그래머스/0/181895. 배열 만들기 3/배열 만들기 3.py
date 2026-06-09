def solution(arr, intervals):
    result = []
    for data in intervals:
        result = result + arr[data[0]:data[1] + 1]
    
    return result