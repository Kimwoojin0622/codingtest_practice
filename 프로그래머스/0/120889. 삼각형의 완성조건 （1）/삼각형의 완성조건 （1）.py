def solution(sides):
    temp = sorted(sides)
    
    if temp[-1] < temp[0] + temp[1]:
        return 1
    else:
        return 2