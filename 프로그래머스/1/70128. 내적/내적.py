def solution(a, b):
    temp = 0
    for i in range(len(a)):
        temp = temp + (a[i]*b[i])
    
    return temp