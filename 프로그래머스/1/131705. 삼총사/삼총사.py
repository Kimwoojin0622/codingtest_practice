def solution(number):
    # number의 길이가 13! O(N^3)도 가능할듯..
    result = []

    for i in range(len(number) - 1):
        for j in range(i + 1, len(number)):
            for t in range(j + 1, len(number)):
                tmp = number[i] + number[j] + number[t]
                if tmp == 0:
                    result.append([number[i], number[j], number[t]])
    
    return len(result)
                    
            
