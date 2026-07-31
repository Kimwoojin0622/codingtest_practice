def solution(name, yearning, photo):
    dict = {}
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    
    result = []
    for p in photo: # O(N^2) 가능
        tmpsum = 0
        for remember in p:
            if remember in dict.keys():
                # print(remember, dict[remember])
                tmpsum += dict[remember]
        result.append(tmpsum)
    
    return result