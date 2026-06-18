def solution(array, height):
    temp = 0
    for num in array:
        if num > height:
            temp += 1
    
    return temp