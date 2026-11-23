def solution(number):
    result = 0
    
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            for t in range(j + 1, len(number)):
                # print(number[i], number[j], number[t])
                if number[i] + number[j] + number[t] == 0:
                    result += 1
    
    return result