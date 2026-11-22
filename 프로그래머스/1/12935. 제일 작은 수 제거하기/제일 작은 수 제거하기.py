def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        tmp = min(arr)
        location = arr.index(tmp)
        arr.pop(location)
        return arr