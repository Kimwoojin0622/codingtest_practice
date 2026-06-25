def solution(s):
    ssplit = s.split(" ")
    for i in range(len(ssplit)):
        if ssplit[i] == 'Z':
            ssplit[i] = 2000
    
    temp, result = 0, 0
    
    for data in ssplit:
        if int(data) < 1000:
            temp = int(data)
            result = result + int(data)
        else:
            result = result - temp
    
    return result