def solution(num, k):
    temp = [data for data in str(num)]
    
    for i in range(len(temp)):
        if temp[i] == str(k):
            return i + 1
    return -1